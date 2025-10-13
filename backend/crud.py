from sqlalchemy.orm import Session
from models import Ambulatorio, ParteCorpo, Esame
from sqlalchemy import or_

def get_ambulatori(db: Session):
    return db.query(Ambulatorio).all()

def get_parti_corpo(db: Session, ambulatorio_id: int, search_ids=None):
    query = db.query(ParteCorpo).join(Esame).filter(Esame.ambulatorio_id == ambulatorio_id)
    if search_ids:
        query = query.filter(Esame.id.in_(map(int, search_ids.split(","))))
    return query.distinct().all()

def get_esami(db: Session, ambulatorio_id: int, parte_corpo_id: int, search_ids=None):
    query = db.query(Esame).filter(
        Esame.ambulatorio_id == ambulatorio_id,
        Esame.parte_corpo_id == parte_corpo_id
    )
    if search_ids:
        query = query.filter(Esame.id.in_(map(int, search_ids.split(","))))
    return query.all()

def search_esami(db: Session, campo: str, text: str):
    query = db.query(Esame)
    pattern = f"%{text.lower()}%"
    if campo == "descrizione":
        query = query.filter(Esame.descrizione.ilike(pattern))
    elif campo == "codice_ministeriale":
        query = query.filter(Esame.codice_ministeriale.ilike(pattern))
    elif campo == "codice_interno":
        query = query.filter(Esame.codice_interno.ilike(pattern))
    return query.all()
