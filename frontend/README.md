E' un’applicazione full-stack con una soluzione moderna e modulare:

- Backend: Python con FastAPI e database SQLite (facile da testare, ma scalabile a PostgreSQL).

- Frontend: React con CSS puro per i layout e gestione dei pannelli affiancati.

Funzionalità principali:

- Seleziona un ambulatorio si aggiorna le parti del corpo disponibili.
- Seleziona una parte del corpo si aggiornano gli esami disponibili.
- Seleziona un esame si aggiunge alla griglia in basso.

Nella griglia è possibile:

- Riordinare gli esami con drag & drop
- Usare i pulsanti ↑↓ per spostarli
- Usare ✕ per eliminare
- Ricerca testuale
- Tutti gli esami selezionati vengono salvati in localStorage, quindi rimangono anche dopo il refresh della pagina.

- Tutti i pannelli funzionano a cascata.
- Gli esami selezionati possono essere trascinati, riordinati o eliminati.
- Appaiono notifiche automatiche ogni volta che aggiungi, rimuovi o riordini un esame.

---

**Frontend**

creazione progetto React:

- npx create-react-app fronted

- cd /Users/giordanapandolfo/Desktop/frontend
- npm install axios #serve per comunicare con il backend
- npm install # solo la prima volta
- npm start

Il browser:
[link](http://localhost:3000)

**Estensioni future:**

- Multiutente con autenticazione
- Paginazione o infinite scroll sugli esami
- Ordinamento e filtri avanzati nella griglia
- Validazioni più robuste sugli esami

In localStorage:

```
selectedExams
[{"id":3,"descrizione":"Eco Addome","ambulatorio_id":2,"codice_ministeriale":"EC001","codice_interno":"INT003","parte_corpo_id":3}]
```
