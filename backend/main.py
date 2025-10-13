from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import crud
from database import SessionLocal, engine, Base
from models import Ambulatorio, ParteCorpo, Esame

# crea le tabelle se non esistono
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS per React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # cambia in produzione
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

@app.get("/ambulatori")
def read_ambulatori(db: Session = Depends(get_db)):
    return crud.get_ambulatori(db)

@app.get("/parti_corpo/{ambulatorio_id}")
def read_parti_corpo(ambulatorio_id: int, search_ids: str = None, db: Session = Depends(get_db)):
    return crud.get_parti_corpo(db, ambulatorio_id, search_ids)

@app.get("/esami")
def read_esami(ambulatorio_id: int, parte_corpo_id: int, search_ids: str = None, db: Session = Depends(get_db)):
    return crud.get_esami(db, ambulatorio_id, parte_corpo_id, search_ids)

@app.get("/search")
def search(campo: str, text: str, db: Session = Depends(get_db)):
    return crud.search_esami(db, campo, text)
