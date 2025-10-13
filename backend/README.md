**backend**

- python3 --version
- pip3 --version

- pip3 install -r requirements.txt
- pip3 install uvicorn (no nel venv)

_usare sempre un virtual environment per evitare conflitti tra librerie Python._

**virtual environment**

- python3 -m venv venv #solo una volta
- source venv/bin/activate #per attivare il virtual environment
- pip install fastapi uvicorn sqlalchemy pydantic #solo una volta
- python3 populate_db.py #script di popolamento

Avviare il server:

- uvicorn main:app --reload

(Le modifiche al backend si aggiornano automaticamente grazie a --reload)

Per avviare il backend:
[link](http://127.0.0.1:8000)

---

**Per verificare che il backend funzioni senza frontend (fase di test)**

```
- Lista ambulatori: http://127.0.0.1:8000/ambulatori

- Lista parti del corpo per ambulatorio 1: http://127.0.0.1:8000/parti_corpo/1

- Lista esami per ambulatorio 1 e parte corpo 2: http://127.0.0.1:8000/esami?ambulatorio_id=1&parte_corpo_id=2

- Ricerca esame per descrizione “mano”: http://127.0.0.1:8000/search?campo=descrizione&text=mano

```
