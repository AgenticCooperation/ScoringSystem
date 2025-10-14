from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.models import Score
from app.schemas import ScoreResponse

router = APIRouter(prefix="/scores", tags=["scores"])


@router.get("/{endpoint_id}", response_model=List[ScoreResponse])
async def get_scores(endpoint_id: int, db: Session = Depends(get_db)):
    """Endpoint'e ait skorları getir"""
    scores = db.query(Score).filter(Score.endpoint_id == endpoint_id).order_by(Score.computed_at.desc()).all()
    return scores


@router.get("/{endpoint_id}/latest", response_model=ScoreResponse)
async def get_latest_score(endpoint_id: int, db: Session = Depends(get_db)):
    """Endpoint'in en son skorunu getir"""
    score = db.query(Score).filter(Score.endpoint_id == endpoint_id).order_by(Score.computed_at.desc()).first()
    if score is None:
        raise HTTPException(status_code=404, detail="Bu endpoint için skor bulunamadı")
    return score
