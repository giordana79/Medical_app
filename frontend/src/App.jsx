import React, { useEffect, useState } from "react";
import Panel from "./components/Panel";
import SearchBar from "./components/SearchBar";
import SelectedGrid from "./components/SelectedGrid";
import Notification from "./components/Notification";
import { getAmbulatori, getPartiCorpo, getEsami, searchEsami } from "./api";
import "./App.css";

export default function App() {
  const [ambulatori, setAmbulatori] = useState([]);
  const [parti, setParti] = useState([]);
  const [esami, setEsami] = useState([]);
  const [selectedAmb, setSelectedAmb] = useState(null);
  const [selectedParte, setSelectedParte] = useState(null);
  const [selectedExams, setSelectedExams] = useState(
    JSON.parse(localStorage.getItem("selectedExams") || "[]")
  );
  const [searchIds, setSearchIds] = useState(null);
  const [notification, setNotification] = useState({
    message: "",
    type: "info",
  });

  const showNotification = (message, type = "info") => {
    setNotification({ message, type });
  };

  // Carica ambulatori all'avvio
  useEffect(() => {
    getAmbulatori().then((res) => {
      setAmbulatori(res.data);
      if (res.data.length > 0 && !selectedAmb) setSelectedAmb(res.data[0].id);
    });
  }, []);

  // Carica parti del corpo in base all'ambulatorio selezionato
  useEffect(() => {
    if (!selectedAmb) return;
    getPartiCorpo(selectedAmb, searchIds).then((res) => {
      setParti(res.data);
      if (res.data.length > 0 && !selectedParte)
        setSelectedParte(res.data[0].id);
    });
  }, [selectedAmb, searchIds]);

  // Carica esami in base a ambulatorio, parte del corpo e searchIds
  useEffect(() => {
    if (!searchIds && (!selectedAmb || !selectedParte)) return;
    getEsami(selectedAmb, selectedParte, searchIds).then((res) =>
      setEsami(res.data)
    );
  }, [selectedAmb, selectedParte, searchIds]);

  // Gestione ricerca
  const handleSearch = (campo, text) => {
    if (!text) return;
    searchEsami(campo, text).then((res) => {
      if (res.data.length === 0) {
        setSearchIds(null);
        showNotification("Nessun esame trovato", "info");
        return;
      }

      // Aggiorna ambulatorio e parte del corpo in base al primo risultato
      setSelectedAmb(res.data[0].ambulatorio.id);
      setSelectedParte(res.data[0].parte_corpo.id);

      const ids = res.data.map((e) => e.id).join(",");
      setSearchIds(ids);
    });
  };

  const handleReset = () => setSearchIds(null);

  const addExam = (exam) => {
    if (!selectedExams.find((e) => e.id === exam.id)) {
      const newExams = [...selectedExams, exam];
      setSelectedExams(newExams);
      localStorage.setItem("selectedExams", JSON.stringify(newExams));
      showNotification(`Esame "${exam.descrizione}" aggiunto`, "success");
    } else {
      showNotification("Esame già presente", "info");
    }
  };

  const removeExam = (idx) => {
    const newExams = selectedExams.filter((_, i) => i !== idx);
    setSelectedExams(newExams);
    localStorage.setItem("selectedExams", JSON.stringify(newExams));
    showNotification("Esame rimosso", "info");
  };

  const moveUp = (idx) => {
    if (idx === 0) return;
    const newArr = [...selectedExams];
    [newArr[idx - 1], newArr[idx]] = [newArr[idx], newArr[idx - 1]];
    setSelectedExams(newArr);
    localStorage.setItem("selectedExams", JSON.stringify(newArr));
    showNotification("Ordine aggiornato", "info");
  };

  const moveDown = (idx) => {
    if (idx === selectedExams.length - 1) return;
    const newArr = [...selectedExams];
    [newArr[idx], newArr[idx + 1]] = [newArr[idx + 1], newArr[idx]];
    setSelectedExams(newArr);
    localStorage.setItem("selectedExams", JSON.stringify(newArr));
    showNotification("Ordine aggiornato", "info");
  };

  return (
    <div className="app">
      <SearchBar onSearch={handleSearch} onReset={handleReset} />
      <div className="panels">
        <Panel
          title="Ambulatori"
          items={ambulatori}
          selectedId={selectedAmb}
          onSelect={setSelectedAmb}
        />
        <Panel
          title="Parti del corpo"
          items={parti}
          selectedId={selectedParte}
          onSelect={setSelectedParte}
        />
        <div className="panel">
          <h2>Esami</h2>
          <ul>
            {esami.map((e) => (
              <li key={e.id} className="esame-item">
                <span>{e.descrizione}</span>
                <button onClick={() => addExam(e)}>Seleziona</button>
              </li>
            ))}
          </ul>
        </div>
      </div>
      <SelectedGrid
        items={selectedExams}
        removeItem={removeExam}
        moveUp={moveUp}
        moveDown={moveDown}
        setItems={setSelectedExams}
      />
      <Notification
        message={notification.message}
        type={notification.type}
        onClose={() => setNotification({ message: "", type: "info" })}
      />
    </div>
  );
}
