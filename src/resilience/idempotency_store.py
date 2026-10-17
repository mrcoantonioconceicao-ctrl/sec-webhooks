import time

class IdempotencyStore:
    """
    Armazém de Idempotência em memória com TTL (Time-To-Live) para impedir
    o processamento duplicado de eventos de webhooks enviados pela Stripe.
    """
    def __init__(self, ttl_seconds: int = 86400):
        self.store = {} # Formato: { event_id: timestamp_de_processamento }
        self.ttl_seconds = ttl_seconds

    def is_processed(self, event_id: str) -> bool:
        self._cleanup_expired()
        return event_id in self.store

    def mark_as_processed(self, event_id: str):
        self.store[event_id] = time.time()

    def _cleanup_expired(self):
        current_time = time.time()
        expired_keys = [
            ev_id for ev_id, timestamp in self.store.items()
            if current_time - timestamp > self.ttl_seconds
        ]
        for k in expired_keys:
            del self.store[k]
