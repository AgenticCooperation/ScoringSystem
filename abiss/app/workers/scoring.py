from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Endpoint, Telemetry, Finding, Score
from app.utils.policy import PolicyEngine
from datetime import datetime
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class ScoringEngine:
    """Endpoint scoring engine"""
    
    def __init__(self):
        self.policy_engine = PolicyEngine()
    
    def calculate_score(self, endpoint_id: int, db: Session) -> Dict[str, Any]:
        """Endpoint için skor hesapla"""
        try:
            # Endpoint'i getir
            endpoint = db.query(Endpoint).filter(Endpoint.id == endpoint_id).first()
            if not endpoint:
                raise ValueError(f"Endpoint {endpoint_id} bulunamadı")
            
            # Son telemetry verilerini getir
            latest_telemetry = db.query(Telemetry).filter(
                Telemetry.endpoint_id == endpoint_id
            ).order_by(Telemetry.collected_at.desc()).first()
            
            if not latest_telemetry:
                logger.warning(f"Endpoint {endpoint_id} için telemetry verisi bulunamadı")
                return {"value": 0, "breakdown": {"reason": "no_telemetry"}}
            
            # Policy engine ile değerlendirme yap
            findings = self.policy_engine.evaluate_telemetry(
                endpoint_id, latest_telemetry.payload, db
            )
            
            # Finding'leri kaydet
            for finding_data in findings:
                finding = Finding(**finding_data)
                db.add(finding)
            
            # Skor hesapla
            score_value = self._calculate_score_from_findings(findings)
            breakdown = self._create_score_breakdown(findings)
            
            # Score kaydını oluştur
            score = Score(
                endpoint_id=endpoint_id,
                value=score_value,
                breakdown=breakdown
            )
            db.add(score)
            
            # Endpoint'in current_score'unu güncelle
            endpoint.current_score = score_value
            endpoint.risk_level = self._determine_risk_level(score_value)
            endpoint.last_seen_at = datetime.utcnow()
            
            db.commit()
            
            logger.info(f"Endpoint {endpoint_id} için skor hesaplandı: {score_value}")
            return {"value": score_value, "breakdown": breakdown}
            
        except Exception as e:
            logger.error(f"Scoring hatası endpoint {endpoint_id}: {str(e)}")
            db.rollback()
            raise
    
    def _calculate_score_from_findings(self, findings: list) -> int:
        """Finding'lerden skor hesapla (0-100)"""
        if not findings:
            return 100  # Hiç finding yoksa mükemmel skor
        
        total_weight = 0
        weighted_score = 0
        
        severity_weights = {
            "critical": 10,
            "high": 7,
            "medium": 4,
            "low": 1
        }
        
        for finding in findings:
            weight = finding.get("weight", 1)
            severity = finding.get("severity", "low")
            severity_weight = severity_weights.get(severity, 1)
            
            # Finding'in skora etkisi (severity'ye göre)
            finding_impact = severity_weight * weight
            
            total_weight += finding_impact
            weighted_score += finding_impact * (100 - severity_weight * 10)  # Her severity için farklı skor düşüşü
        
        if total_weight == 0:
            return 100
        
        final_score = max(0, 100 - (weighted_score / total_weight))
        return int(final_score)
    
    def _create_score_breakdown(self, findings: list) -> Dict[str, Any]:
        """Skor breakdown'u oluştur"""
        breakdown = {
            "total_findings": len(findings),
            "by_severity": {},
            "by_rule": {}
        }
        
        for finding in findings:
            severity = finding.get("severity", "low")
            rule_id = finding.get("rule_id", "unknown")
            
            breakdown["by_severity"][severity] = breakdown["by_severity"].get(severity, 0) + 1
            breakdown["by_rule"][rule_id] = breakdown["by_rule"].get(rule_id, 0) + 1
        
        return breakdown
    
    def _determine_risk_level(self, score: int) -> str:
        """Skora göre risk seviyesi belirle"""
        if score >= 90:
            return "low"
        elif score >= 70:
            return "medium"
        elif score >= 40:
            return "high"
        else:
            return "critical"


def evaluate_and_score_endpoint(endpoint_id: int):
    """Background task olarak endpoint'i değerlendir ve skorla"""
    db = SessionLocal()
    try:
        scoring_engine = ScoringEngine()
        result = scoring_engine.calculate_score(endpoint_id, db)
        logger.info(f"Background scoring tamamlandı endpoint {endpoint_id}: {result}")
    except Exception as e:
        logger.error(f"Background scoring hatası endpoint {endpoint_id}: {str(e)}")
    finally:
        db.close()
