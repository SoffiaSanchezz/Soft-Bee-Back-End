from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, JSON, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.core.database.db import db

class UserModel(db.Model):
    """Modelo SQLAlchemy para usuarios"""
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    is_verified = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=True)
    refresh_tokens = Column(JSON, default=list)
    profile_image_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, username={self.username})>"