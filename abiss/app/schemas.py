from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime


# Endpoint Schemas
class EndpointBase(BaseModel):
    hostname: str = Field(..., max_length=255)
    platform: str = Field(..., max_length=50)
    owner_label: Optional[str] = Field(None, max_length=100)
    tags: Optional[List[str]] = None
    current_score: Optional[int] = Field(None, ge=0, le=100)
    risk_level: Optional[str] = Field(None, pattern="^(low|medium|high|critical)$")


class EndpointCreate(EndpointBase):
    pass


class EndpointUpdate(BaseModel):
    hostname: Optional[str] = Field(None, max_length=255)
    platform: Optional[str] = Field(None, max_length=50)
    owner_label: Optional[str] = Field(None, max_length=100)
    tags: Optional[List[str]] = None
    last_seen_at: Optional[datetime] = None
    current_score: Optional[int] = Field(None, ge=0, le=100)
    risk_level: Optional[str] = Field(None, pattern="^(low|medium|high|critical)$")


class EndpointResponse(EndpointBase):
    id: int
    last_seen_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Telemetry Schemas
class TelemetryBase(BaseModel):
    endpoint_id: int
    payload: Dict[str, Any]
    schema_version: str = Field(default="1.0", max_length=20)


class TelemetryCreate(TelemetryBase):
    pass


class TelemetryResponse(TelemetryBase):
    id: int
    collected_at: datetime

    class Config:
        from_attributes = True


# Finding Schemas
class FindingBase(BaseModel):
    endpoint_id: int
    rule_id: str = Field(..., max_length=100)
    severity: str = Field(..., pattern="^(low|medium|high|critical)$")
    weight: int = Field(default=1, ge=1, le=10)
    title: str = Field(..., max_length=255)
    details: Optional[str] = None
    evidence: Optional[Dict[str, Any]] = None


class FindingCreate(FindingBase):
    pass


class FindingResponse(FindingBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Score Schemas
class ScoreBase(BaseModel):
    endpoint_id: int
    value: int = Field(..., ge=0, le=100)
    breakdown: Optional[Dict[str, Any]] = None


class ScoreCreate(ScoreBase):
    pass


class ScoreResponse(ScoreBase):
    id: int
    computed_at: datetime

    class Config:
        from_attributes = True


# Remediation Schemas
class RemediationBase(BaseModel):
    endpoint_id: int
    source: str = Field(..., max_length=100)
    actions: List[Dict[str, Any]]
    request_id: str = Field(..., max_length=100)
    audit_log: Optional[Dict[str, Any]] = None


class RemediationCreate(RemediationBase):
    pass


class RemediationUpdate(BaseModel):
    status: Optional[str] = Field(None, pattern="^(pending|running|completed|failed)$")
    audit_log: Optional[Dict[str, Any]] = None
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None


class RemediationResponse(RemediationBase):
    id: int
    status: str
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True


# Query Schemas
class FindingQuery(BaseModel):
    endpoint_id: Optional[int] = None
    severity: Optional[str] = Field(None, pattern="^(low|medium|high|critical)$")
    rule_id: Optional[str] = None


class RemediationExecute(BaseModel):
    endpoint_id: int
    source: str = Field(..., max_length=100)
    actions: List[Dict[str, Any]]
    request_id: str = Field(..., max_length=100)
    audit_log: Optional[Dict[str, Any]] = None
