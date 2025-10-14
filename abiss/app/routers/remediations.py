from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.db import get_db
from app.models import Remediation
from app.schemas import RemediationExecute, RemediationResponse

router = APIRouter(prefix="/remediations", tags=["remediations"])


@router.post("/execute", response_model=RemediationResponse)
async def execute_remediation(remediation: RemediationExecute, db: Session = Depends(get_db)):
    """Remediation'ı idempotent olarak çalıştır"""
    # Aynı request_id ile daha önce çalıştırılmış mı kontrol et
    existing_remediation = db.query(Remediation).filter(
        Remediation.request_id == remediation.request_id
    ).first()
    
    if existing_remediation:
        return existing_remediation
    
    # Yeni remediation oluştur
    db_remediation = Remediation(
        **remediation.dict(),
        status="pending",
        started_at=datetime.utcnow()
    )
    db.add(db_remediation)
    db.commit()
    db.refresh(db_remediation)
    
    return db_remediation


@router.get("/{remediation_id}", response_model=RemediationResponse)
async def get_remediation(remediation_id: int, db: Session = Depends(get_db)):
    """ID'ye göre remediation getir"""
    remediation = db.query(Remediation).filter(Remediation.id == remediation_id).first()
    if remediation is None:
        raise HTTPException(status_code=404, detail="Remediation bulunamadı")
    return remediation


@router.get("/", response_model=list[RemediationResponse])
async def list_remediations(
    endpoint_id: int = None,
    status: str = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Remediation'ları listele"""
    query = db.query(Remediation)
    
    if endpoint_id:
        query = query.filter(Remediation.endpoint_id == endpoint_id)
    if status:
        query = query.filter(Remediation.status == status)
    
    remediations = query.offset(skip).limit(limit).all()
    return remediations
