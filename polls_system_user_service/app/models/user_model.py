from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(255))
    joining_date = Column(Date)
    is_registered = Column(Boolean, default=False)

    # # Relationships (Cascade Delete)
    # answers = relationship("Answer", back_populates="user", cascade="all, delete-orphan")
