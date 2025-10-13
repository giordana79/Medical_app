import React, { useEffect } from "react";
import "./Notification.css";

export default function Notification({ message, type, onClose }) {
  useEffect(() => {
    if (!message) return;
    const timer = setTimeout(() => onClose(), 3000);
    return () => clearTimeout(timer);
  }, [message, onClose]);

  if (!message) return null;

  return (
    <div className={`notification ${type}`}>
      {message}
      <button onClick={onClose}>&times;</button>
    </div>
  );
}
