from sqlalchemy.orm import Session
from app.models import Finding
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class PolicyEngine:
    """Policy evaluation engine"""
    
    def __init__(self):
        self.rules = self._load_default_rules()
    
    def evaluate_telemetry(self, endpoint_id: int, payload: Dict[str, Any], db: Session) -> List[Dict[str, Any]]:
        """Telemetry verisini policy kurallarına göre değerlendir"""
        findings = []
        
        try:
            # Her kural için değerlendirme yap
            for rule_id, rule_func in self.rules.items():
                try:
                    rule_findings = rule_func(endpoint_id, payload)
                    if rule_findings:
                        findings.extend(rule_findings)
                except Exception as e:
                    logger.error(f"Rule {rule_id} değerlendirme hatası: {str(e)}")
                    # Hata durumunda genel bir finding oluştur
                    findings.append({
                        "endpoint_id": endpoint_id,
                        "rule_id": rule_id,
                        "severity": "medium",
                        "weight": 1,
                        "title": f"Rule Evaluation Error: {rule_id}",
                        "details": f"Rule değerlendirme sırasında hata oluştu: {str(e)}",
                        "evidence": {"error": str(e)}
                    })
            
            return findings
            
        except Exception as e:
            logger.error(f"Policy evaluation genel hatası: {str(e)}")
            return [{
                "endpoint_id": endpoint_id,
                "rule_id": "policy_engine_error",
                "severity": "high",
                "weight": 5,
                "title": "Policy Engine Error",
                "details": f"Policy değerlendirme sırasında genel hata: {str(e)}",
                "evidence": {"error": str(e)}
            }]
    
    def _load_default_rules(self) -> Dict[str, callable]:
        """Varsayılan policy kurallarını yükle"""
        return {
            "security_updates": self._check_security_updates,
            "firewall_status": self._check_firewall_status,
            "antivirus_status": self._check_antivirus_status,
            "disk_space": self._check_disk_space,
            "memory_usage": self._check_memory_usage,
            "network_connections": self._check_network_connections,
            "user_accounts": self._check_user_accounts,
            "installed_software": self._check_installed_software
        }
    
    def _check_security_updates(self, endpoint_id: int, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Güvenlik güncellemelerini kontrol et"""
        findings = []
        
        # Windows için
        if payload.get("platform") == "windows":
            updates = payload.get("system", {}).get("updates", [])
            critical_updates = [u for u in updates if u.get("severity") == "critical"]
            
            if critical_updates:
                findings.append({
                    "endpoint_id": endpoint_id,
                    "rule_id": "security_updates",
                    "severity": "critical",
                    "weight": 8,
                    "title": f"Critical Security Updates Pending ({len(critical_updates)})",
                    "details": f"{len(critical_updates)} kritik güvenlik güncellemesi bekliyor",
                    "evidence": {"critical_updates": critical_updates}
                })
        
        return findings
    
    def _check_firewall_status(self, endpoint_id: int, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Firewall durumunu kontrol et"""
        findings = []
        
        firewall = payload.get("security", {}).get("firewall", {})
        if not firewall.get("enabled", False):
            findings.append({
                "endpoint_id": endpoint_id,
                "rule_id": "firewall_status",
                "severity": "high",
                "weight": 6,
                "title": "Firewall Disabled",
                "details": "Firewall devre dışı",
                "evidence": {"firewall_status": firewall}
            })
        
        return findings
    
    def _check_antivirus_status(self, endpoint_id: int, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Antivirus durumunu kontrol et"""
        findings = []
        
        antivirus = payload.get("security", {}).get("antivirus", {})
        if not antivirus.get("enabled", False):
            findings.append({
                "endpoint_id": endpoint_id,
                "rule_id": "antivirus_status",
                "severity": "high",
                "weight": 7,
                "title": "Antivirus Disabled",
                "details": "Antivirus yazılımı devre dışı",
                "evidence": {"antivirus_status": antivirus}
            })
        
        return findings
    
    def _check_disk_space(self, endpoint_id: int, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Disk alanını kontrol et"""
        findings = []
        
        disks = payload.get("system", {}).get("disks", [])
        for disk in disks:
            usage_percent = disk.get("usage_percent", 0)
            if usage_percent > 90:
                findings.append({
                    "endpoint_id": endpoint_id,
                    "rule_id": "disk_space",
                    "severity": "medium",
                    "weight": 3,
                    "title": f"Low Disk Space: {disk.get('mount_point', 'Unknown')}",
                    "details": f"Disk kullanımı %{usage_percent} - kritik seviyede",
                    "evidence": {"disk": disk}
                })
        
        return findings
    
    def _check_memory_usage(self, endpoint_id: int, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Bellek kullanımını kontrol et"""
        findings = []
        
        memory = payload.get("system", {}).get("memory", {})
        usage_percent = memory.get("usage_percent", 0)
        
        if usage_percent > 95:
            findings.append({
                "endpoint_id": endpoint_id,
                "rule_id": "memory_usage",
                "severity": "high",
                "weight": 4,
                "title": "High Memory Usage",
                "details": f"Bellek kullanımı %{usage_percent} - kritik seviyede",
                "evidence": {"memory": memory}
            })
        
        return findings
    
    def _check_network_connections(self, endpoint_id: int, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Ağ bağlantılarını kontrol et"""
        findings = []
        
        connections = payload.get("network", {}).get("connections", [])
        suspicious_ports = [22, 23, 3389, 5900]  # SSH, Telnet, RDP, VNC
        
        for conn in connections:
            port = conn.get("port")
            if port in suspicious_ports and conn.get("state") == "LISTEN":
                findings.append({
                    "endpoint_id": endpoint_id,
                    "rule_id": "network_connections",
                    "severity": "medium",
                    "weight": 3,
                    "title": f"Suspicious Port Open: {port}",
                    "details": f"Şüpheli port {port} açık",
                    "evidence": {"connection": conn}
                })
        
        return findings
    
    def _check_user_accounts(self, endpoint_id: int, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Kullanıcı hesaplarını kontrol et"""
        findings = []
        
        users = payload.get("system", {}).get("users", [])
        admin_users = [u for u in users if u.get("is_admin", False)]
        
        if len(admin_users) > 3:
            findings.append({
                "endpoint_id": endpoint_id,
                "rule_id": "user_accounts",
                "severity": "medium",
                "weight": 2,
                "title": "Too Many Admin Users",
                "details": f"{len(admin_users)} admin kullanıcı bulundu",
                "evidence": {"admin_users": admin_users}
            })
        
        return findings
    
    def _check_installed_software(self, endpoint_id: int, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Yüklü yazılımları kontrol et"""
        findings = []
        
        software = payload.get("system", {}).get("software", [])
        suspicious_software = ["tor", "vpn", "proxy", "remote_access"]
        
        for app in software:
            app_name = app.get("name", "").lower()
            if any(sus in app_name for sus in suspicious_software):
                findings.append({
                    "endpoint_id": endpoint_id,
                    "rule_id": "installed_software",
                    "severity": "low",
                    "weight": 1,
                    "title": f"Suspicious Software: {app.get('name')}",
                    "details": f"Şüpheli yazılım tespit edildi: {app.get('name')}",
                    "evidence": {"software": app}
                })
        
        return findings
