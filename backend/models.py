from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Ambulatorio(Base):
    __tablename__ = "ambulatori"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, nullable=False)
    esami = relationship("Esame", back_populates="ambulatorio")

class ParteCorpo(Base):
    __tablename__ = "parti_corpo"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, nullable=False)
    esami = relationship("Esame", back_populates="parte_corpo")

class Esame(Base):
    __tablename__ = "esami"
    id = Column(Integer, primary_key=True, index=True)
    codice_ministeriale = Column(String(10))
    codice_interno = Column(String(10))
    descrizione = Column(String(100))
    parte_corpo_id = Column(Integer, ForeignKey("parti_corpo.id"))
    ambulatorio_id = Column(Integer, ForeignKey("ambulatori.id"))

    parte_corpo = relationship("ParteCorpo", back_populates="esami")
    ambulatorio = relationship("Ambulatorio", back_populates="esami")
