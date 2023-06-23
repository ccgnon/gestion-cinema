from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Film(Base):
    id = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    label = Column(String(256), nullable=False)
    url = Column(String(256), index=True, nullable=True)
    summary = Column(String(256), nullable=True)
    submitter_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    submitter = relationship("User", back_populates="films")
