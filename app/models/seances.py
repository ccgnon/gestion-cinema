from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Seances(Base):
    id = Column(Integer, primary_key=True, index=True)
    date= Column(String(256), nullable=False)
    heure= Column(String(256), index=True, nullable=True)
    tarifs= Column(String(256), nullable=True)
    id_films = Column(String(256), secondary_key=True, index=True)
    id_salle = Column(String(256), secondary_key=True, index=True)
    submitter_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    submitter = relationship("User", back_populates="seances")
