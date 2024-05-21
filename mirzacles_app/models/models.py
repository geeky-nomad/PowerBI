from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    firstname = Column(String, unique=True)
    lastname = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)
    created_at = Column(Date)
    modified_at = Column(Date)
    # payment_customer_id = Column(String, null=True, blank=True)
    # slug = Column(String, max_length=150)
