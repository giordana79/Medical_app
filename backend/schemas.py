from pydantic import BaseModel
from typing import List, Optional

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
    codice_ministeriale: Optional[str] = None
    codice_interno: Optional[str] = None
    descrizione: Optional[str] = None
    parte_corpo: ParteCorpoSchema
    ambulatorio: AmbulatorioSchema

    class Config:
        orm_mode = True
