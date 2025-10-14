// utility minimale per notifiche globali (optional)
let globalNotify = null;

export function setGlobalNotifier(fn) {
  globalNotify = fn;
}

export function showGlobalNotification(message, type = "info") {
  if (globalNotify) globalNotify(message, type);
  else console.log(`[${type}] ${message}`);
}
