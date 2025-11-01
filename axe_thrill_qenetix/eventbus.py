from __future__ import annotations

from collections import defaultdict
from typing import Callable, DefaultDict, List

Handler = Callable[[dict], None]


class EventBus:
    """Minimal publish/subscribe bus."""

    def __init__(self) -> None:
        self._subscribers: DefaultDict[str, List[Handler]] = defaultdict(list)

    def subscribe(self, topic: str, handler: Handler) -> None:
        self._subscribers[topic].append(handler)

    def publish(self, topic: str, event: dict) -> None:
        for handler in list(self._subscribers.get(topic, [])):
            handler(event)
