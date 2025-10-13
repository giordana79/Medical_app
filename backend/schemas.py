from pydantic import BaseModel
from typing import List

class AmbulatorioSchema(BaseModel):
    id: int
    nome: str
    class Config:
        orm_mode = True

class ParteCorpoSchema(BaseModel):
    id: int
    nome: str
    class Config:
        orm_mode = True

class EsameSchema(BaseModel):
    id: int
    codice_ministeriale: str
    codice_interno: str
    descrizione: str
    parte_corpo: ParteCorpoSchema
    ambulatori: List[AmbulatorioSchema]
    class Config:
        orm_mode = True
