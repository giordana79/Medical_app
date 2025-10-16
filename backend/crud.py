from sqlalchemy.orm import Session
from models import Ambulatorio, ParteCorpo, Esame
from sqlalchemy import or_

def get_ambulatori(db: Session):
    return db.query(Ambulatorio).all()

def get_parti_corpo(db: Session, ambulatorio_id: int, search_ids: str = None):
    # join con Esame e filtra per ambulatorio
    query = db.query(ParteCorpo).join(Esame).filter(Esame.ambulatorio_id == ambulatorio_id)
    if search_ids:
        try:
            ids = [int(x) for x in search_ids.split(",") if x.strip()]
            if ids:
                query = query.filter(Esame.id.in_(ids))
        except ValueError:
            # se id non validi, ritorna nessuna parte
            return []
    # distinct sui campi di ParteCorpo
    return query.distinct(ParteCorpo.id).all()

def get_esami(db: Session, ambulatorio_id: int, parte_corpo_id: int, search_ids: str = None):
    query = db.query(Esame).filter(
        Esame.ambulatorio_id == ambulatorio_id,
        Esame.parte_corpo_id == parte_corpo_id
    )
    if search_ids:
        try:
            ids = [int(x) for x in search_ids.split(",") if x.strip()]
            if ids:
                query = query.filter(Esame.id.in_(ids))
        except ValueError:
            return []
    return query.all()

def search_esami(db: Session, campo: str, text: str):
    if not text:
        return []
    pattern = f"%{text.strip().lower()}%"
    q = db.query(Esame)
    # supporta ricerca su singolo campo o su tutti
    if campo == "descrizione":
        q = q.filter(Esame.descrizione.ilike(pattern))
    elif campo == "codice_ministeriale":
        q = q.filter(Esame.codice_ministeriale.ilike(pattern))
    elif campo == "codice_interno":
        q = q.filter(Esame.codice_interno.ilike(pattern))
    elif campo == "all":
        q = q.filter(
            or_(
               Esame.descrizione.like(pattern),
               Esame.codice_ministeriale.like(pattern),
               Esame.codice_interno.like(pattern),
            )
        )
    else:
        # campo non riconosciuto -> nessun risultato
        return []
    return q.all()
