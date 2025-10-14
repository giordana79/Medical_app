from database import SessionLocal, engine, Base
from models import Ambulatorio, ParteCorpo, Esame

# crea tabelle se non esistono
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# controlla se database già popolato (semplice check)
if db.query(Ambulatorio).first():
    print("Database già popolato, esco.")
else:
    # Ambulatori
    amb1 = Ambulatorio(nome="Radiologia")
    amb2 = Ambulatorio(nome="EcografiaPrivitera")
    db.add_all([amb1, amb2])
    db.commit()

    # Parti corpo
    p1 = ParteCorpo(nome="Testa")
    p2 = ParteCorpo(nome="Arti superiori")
    p3 = ParteCorpo(nome="Addome")
    db.add_all([p1, p2, p3])
    db.commit()

    # Esami (usa gli id ottenuti)
    esami_list = [
        Esame(codice_ministeriale="RX001", codice_interno="INT001", descrizione="RX mano Dx", parte_corpo_id=p2.id, ambulatorio_id=amb1.id),
        Esame(codice_ministeriale="RM001", codice_interno="INT002", descrizione="RMN cranio", parte_corpo_id=p1.id, ambulatorio_id=amb1.id),
        Esame(codice_ministeriale="EC001", codice_interno="INT003", descrizione="Eco Addome", parte_corpo_id=p3.id, ambulatorio_id=amb2.id),
    ]
    db.add_all(esami_list)
    db.commit()
    print("✅ Database popolato con successo!")

db.close()
