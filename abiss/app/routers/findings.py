from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db import get_db
from app.models import Finding
from app.schemas import FindingResponse, FindingQuery

router = APIRouter(prefix="/findings", tags=["findings"])


@router.get("/", response_model=List[FindingResponse])
async def get_findings(
    endpoint_id: Optional[int] = Query(None),
    severity: Optional[str] = Query(None),
    rule_id: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """Finding'leri filtrele ve getir"""
    query = db.query(Finding)
    
    if endpoint_id:
        query = query.filter(Finding.endpoint_id == endpoint_id)
    if severity:
        query = query.filter(Finding.severity == severity)
    if rule_id:
        query = query.filter(Finding.rule_id == rule_id)
    
    findings = query.offset(skip).limit(limit).all()
    return findings


@router.get("/{finding_id}", response_model=FindingResponse)
async def get_finding(finding_id: int, db: Session = Depends(get_db)):
    """ID'ye göre finding getir"""
    finding = db.query(Finding).filter(Finding.id == finding_id).first()
    if finding is None:
        raise HTTPException(status_code=404, detail="Finding bulunamadı")
    return finding
