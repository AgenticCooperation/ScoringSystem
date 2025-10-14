from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.settings import settings
from app.db import create_tables
from app.routers import endpoints, telemetry, findings, scores, remediations

# FastAPI uygulaması oluştur
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Advanced Backend Intelligence Scoring System",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router'ları ekle
app.include_router(endpoints.router)
app.include_router(telemetry.router)
app.include_router(findings.router)
app.include_router(scores.router)
app.include_router(remediations.router)


@app.on_event("startup")
async def startup_event():
    """Uygulama başlatıldığında çalışacak"""
    # Geçici olarak tabloları oluştur (Alembic sonrası kaldırılacak)
    create_tables()


@app.get("/")
async def root():
    """Ana endpoint"""
    return {
        "message": "ABISS - Advanced Backend Intelligence Scoring System",
        "version": settings.app_version,
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
async def health_check():
    """Sağlık kontrolü"""
    return {"status": "healthy", "version": settings.app_version}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )
