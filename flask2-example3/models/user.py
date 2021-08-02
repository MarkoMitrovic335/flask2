import uuid
import datetime
import bcrypt

from .base import Base

from sqlalchemy import (
    Column, String, DateTime, Date
)

class User(Base):
    __tablename__ = 'users'

    uid = Column(String(36), default=lambda: str(uuid.uuid4()), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(12), unique=True)
    password = Column(String(120), nullable=False)
    
  
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
