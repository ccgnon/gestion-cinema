from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.base_class import Base


class Reservation(Base):
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(256), nullable=True)
    amount = Column(Integer, nullable=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=True)
    sceance_id = Column(Integer, ForeignKey("sceance.id"), nullable=True)
