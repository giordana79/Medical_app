from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional

import crud
from database import SessionLocal, engine, Base
from models import Ambulatorio, ParteCorpo, Esame
from schemas import AmbulatorioSchema, ParteCorpoSchema, EsameSchema

# crea tabelle se non esistono
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Medical App API")

# CORS - in produzione specificare origin preciso
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#restituire oggetti validati dai tuoi schema Pydantic
#garantisce output coerenti con gli schemi
@app.get("/ambulatori", response_model=List[AmbulatorioSchema])
def read_ambulatori(db: Session = Depends(get_db)):
    return crud.get_ambulatori(db)

@app.get("/parti_corpo/{ambulatorio_id}", response_model=List[ParteCorpoSchema])
def read_parti_corpo(
    ambulatorio_id: int,
    search_ids: Optional[str] = Query(None, description="Comma separated esami ids"),
    db: Session = Depends(get_db),
):
    result = crud.get_parti_corpo(db, ambulatorio_id, search_ids)
    return result or []

@app.get("/esami", response_model=List[EsameSchema])
def read_esami(
    ambulatorio_id: int,
    parte_corpo_id: int,
    search_ids: Optional[str] = Query(None, description="Comma separated esami ids"),
    db: Session = Depends(get_db),
):
    result = crud.get_esami(db, ambulatorio_id, parte_corpo_id, search_ids)
    return result or []

@app.get("/search", response_model=List[EsameSchema])
def search(
    campo: str = Query(..., description="descrizione | codice_ministeriale | codice_interno | all"),
    text: str = Query(...),
    db: Session = Depends(get_db),
):
    if campo not in ("descrizione", "codice_ministeriale", "codice_interno", "all"):
        raise HTTPException(status_code=400, detail="campo non valido")
    return crud.search_esami(db, campo, text)
