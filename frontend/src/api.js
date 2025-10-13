import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const getAmbulatori = () => axios.get(`${API_URL}/ambulatori`);
export const getPartiCorpo = (ambId, ids = null) =>
  axios.get(`${API_URL}/parti_corpo/${ambId}${ids ? `?ids=${ids}` : ""}`);
export const getEsami = (ambId, parteId, ids = null) =>
  axios.get(
    `${API_URL}/esami?ambulatorio_id=${ambId}&parte_corpo_id=${parteId}${ids ? `&ids=${ids}` : ""}`
  );
export const searchEsami = (campo, text) =>
  axios.get(`${API_URL}/search?campo=${campo}&text=${text}`);
