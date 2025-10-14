from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db import get_db
from app.models import Endpoint
from app.schemas import EndpointCreate, EndpointResponse, EndpointUpdate

router = APIRouter(prefix="/endpoints", tags=["endpoints"])


@router.post("/", response_model=EndpointResponse)
async def create_endpoint(endpoint: EndpointCreate, db: Session = Depends(get_db)):
    """Yeni endpoint oluştur"""
    db_endpoint = Endpoint(**endpoint.dict())
    db.add(db_endpoint)
    db.commit()
    db.refresh(db_endpoint)
    return db_endpoint


@router.get("/{endpoint_id}", response_model=EndpointResponse)
async def get_endpoint(endpoint_id: int, db: Session = Depends(get_db)):
    """ID'ye göre endpoint getir"""
    endpoint = db.query(Endpoint).filter(Endpoint.id == endpoint_id).first()
    if endpoint is None:
        raise HTTPException(status_code=404, detail="Endpoint bulunamadı")
    return endpoint


@router.get("/", response_model=List[EndpointResponse])
async def list_endpoints(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    platform: Optional[str] = None,
    risk_level: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Endpoint'leri listele"""
    query = db.query(Endpoint)
    
    if platform:
        query = query.filter(Endpoint.platform == platform)
    if risk_level:
        query = query.filter(Endpoint.risk_level == risk_level)
    
    endpoints = query.offset(skip).limit(limit).all()
    return endpoints
