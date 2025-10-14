from sqlalchemy import Column, Integer, String, DateTime, Text, JSON, ForeignKey, UniqueConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional, Dict, Any

Base = declarative_base()


class Endpoint(Base):
    __tablename__ = "endpoints"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String(255), nullable=False, index=True)
    platform = Column(String(50), nullable=False)
    owner_label = Column(String(100), nullable=True)
    tags = Column(JSON, nullable=True)  # JSON array of strings
    last_seen_at = Column(DateTime(timezone=True), nullable=True)
    current_score = Column(Integer, nullable=True)  # 0-100
    risk_level = Column(String(20), nullable=True)  # low, medium, high, critical
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    telemetry_data = relationship("Telemetry", back_populates="endpoint")
    findings = relationship("Finding", back_populates="endpoint")
    scores = relationship("Score", back_populates="endpoint")
    remediations = relationship("Remediation", back_populates="endpoint")

    __table_args__ = (
        Index('idx_endpoint_hostname_platform', 'hostname', 'platform'),
    )


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("endpoints.id"), nullable=False, index=True)
    payload = Column(JSON, nullable=False)  # JSONB equivalent
    schema_version = Column(String(20), nullable=False, default="1.0")
    collected_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    endpoint = relationship("Endpoint", back_populates="telemetry_data")

    __table_args__ = (
        Index('idx_telemetry_endpoint_collected', 'endpoint_id', 'collected_at'),
    )


class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("endpoints.id"), nullable=False, index=True)
    rule_id = Column(String(100), nullable=False, index=True)
    severity = Column(String(20), nullable=False)  # low, medium, high, critical
    weight = Column(Integer, nullable=False, default=1)  # 1-10
    title = Column(String(255), nullable=False)
    details = Column(Text, nullable=True)
    evidence = Column(JSON, nullable=True)  # Additional evidence data
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    endpoint = relationship("Endpoint", back_populates="findings")

    __table_args__ = (
        Index('idx_finding_endpoint_rule', 'endpoint_id', 'rule_id'),
        Index('idx_finding_severity', 'severity'),
    )


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("endpoints.id"), nullable=False, index=True)
    value = Column(Integer, nullable=False)  # 0-100
    breakdown = Column(JSON, nullable=True)  # Detailed scoring breakdown
    computed_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    endpoint = relationship("Endpoint", back_populates="scores")

    __table_args__ = (
        Index('idx_score_endpoint_computed', 'endpoint_id', 'computed_at'),
    )


class Remediation(Base):
    __tablename__ = "remediations"

    id = Column(Integer, primary_key=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("endpoints.id"), nullable=False, index=True)
    source = Column(String(100), nullable=False)  # manual, automated, policy
    actions = Column(JSON, nullable=False)  # Array of remediation actions
    status = Column(String(20), nullable=False, default="pending")  # pending, running, completed, failed
    request_id = Column(String(100), nullable=False, unique=True, index=True)
    audit_log = Column(JSON, nullable=True)  # Audit trail
    started_at = Column(DateTime(timezone=True), nullable=True)
    finished_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    endpoint = relationship("Endpoint", back_populates="remediations")

    __table_args__ = (
        Index('idx_remediation_endpoint_status', 'endpoint_id', 'status'),
        Index('idx_remediation_request_id', 'request_id'),
    )
