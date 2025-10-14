import axios from "axios";
import { showGlobalNotification } from "./utils";

const API_URL = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

const client = axios.create({
  baseURL: API_URL,
  timeout: 10000,
});

// interceptor per errori
client.interceptors.response.use(
  (response) => response,
  (error) => {
    const msg =
      error?.response?.data?.detail || error.message || "Errore di rete";
    // notificazione globale opzionale
    try {
      showGlobalNotification(msg, "error");
    } catch (e) {}
    return Promise.reject(error);
  }
);

export const getAmbulatori = () => axios.get(`${API_URL}/ambulatori`);

export const getPartiCorpo = (ambId, searchIds) =>
  axios.get(
    `${API_URL}/parti_corpo/${ambId}${searchIds ? `?search_ids=${searchIds}` : ""}`
  );

export const getEsami = (ambId, parteId, searchIds) =>
  axios.get(
    `${API_URL}/esami?ambulatorio_id=${ambId}&parte_corpo_id=${parteId}${searchIds ? `&search_ids=${searchIds}` : ""}`
  );

export const searchEsami = (campo, text) =>
  axios.get(`${API_URL}/search?campo=${campo}&text=${text}`);
