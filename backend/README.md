**backend**

- python3 --version
- pip3 --version

- pip3 install -r requirements.txt
- pip3 install uvicorn (no nel venv)

_usare sempre un virtual environment per evitare conflitti tra librerie Python._

**virtual environment**

- python3 -m venv venv #solo una volta
- source venv/bin/activate #per attivare il virtual environment
- pip3 install fastapi uvicorn sqlalchemy pydantic #solo una volta
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

---

N.B.

Aprire la documentazione **Swagger**

Aprire nel browser:

http://127.0.0.1:8000/docs

Qui è possibile testare tutti gli endpoint.

**Test endpoint /parti_corpo/{ambulatorio_id}**

Cliccare su GET /parti_corpo/{ambulatorio_id}

Inserire:

ambulatorio_id: ad esempio 1

search_ids: ad esempio 1,2

Premere “Execute”

Controllare che la chiamata generi una richiesta come:

```
GET /parti_corpo/1?search_ids=1,2
```

e che il backend risponda con le parti del corpo associate a quegli esami.

**Test endpoint /esami**

Cliccare su GET /esami

Inserire i parametri:

ambulatorio_id: 1

parte_corpo_id: 2

search_ids: 1,2

Premere: "Execute"

Si dovrebbe vedere nel log del terminale (dove gira uvicorn):

```
INFO:     127.0.0.1:12345 - "GET /esami?ambulatorio_id=1&parte_corpo_id=2&search_ids=1,2 HTTP/1.1" 200 OK
```

E nella risposta, solo gli esami con id 1 e 2.

---

**Test da frontend**

Nel frontend si può aprire DevTools → Network tab e filtrare per “esami” o “parti_corpo” per verificare che le richieste abbiano il formato:

```
http://127.0.0.1:8000/parti_corpo/1?search_ids=1,2
```

Per accedere al db SQLite:

da terminale entrare nella cartella dove c'è il file database.db ed avviare SQLite con
il comando:

- sqlite3 database.db
- .tables
- .schema esami #mostra strutura tabella
- SELECT \* FROM ambulatori;
- SELECT \* FROM esami WHERE codice_ministeriale='EC001';
  .exit
