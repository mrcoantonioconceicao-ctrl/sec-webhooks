from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class WebhookEvent:
    event_id: str
    event_type: str
    payload: Dict[Any, Any]
    status_code: int = 500
