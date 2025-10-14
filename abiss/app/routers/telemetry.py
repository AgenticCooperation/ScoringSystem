from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Telemetry, Endpoint
from app.schemas import TelemetryCreate, TelemetryResponse
from app.workers.scoring import evaluate_and_score_endpoint

router = APIRouter(prefix="/telemetry", tags=["telemetry"])


@router.post("/", response_model=TelemetryResponse)
async def create_telemetry(
    telemetry: TelemetryCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """Telemetry verisi kaydet ve background'da scoring yap"""
    # Endpoint'in var olduğunu kontrol et
    endpoint = db.query(Endpoint).filter(Endpoint.id == telemetry.endpoint_id).first()
    if endpoint is None:
        raise HTTPException(status_code=404, detail="Endpoint bulunamadı")
    
    # Telemetry kaydını oluştur
    db_telemetry = Telemetry(**telemetry.dict())
    db.add(db_telemetry)
    db.commit()
    db.refresh(db_telemetry)
    
    # Background task olarak scoring'i başlat
    background_tasks.add_task(evaluate_and_score_endpoint, telemetry.endpoint_id)
    
    return db_telemetry
