from __future__ import annotations

from typing import Any, Callable

from .eventbus import EventBus


class QENETiXAgent:
    """Simple event-driven agent wrapper."""

    def __init__(self, name: str, event_bus: EventBus) -> None:
        self.name = name
        self.event_bus = event_bus
        self.event_bus.subscribe(f"agent.{self.name}.event", self.handle_event)

    def handle_event(self, event: Any) -> None:  # pragma: no cover - stub hook
        print(f"Agent {self.name} received event: {event}")

    def emit(self, topic: str, payload: dict) -> None:
        self.event_bus.publish(topic, payload)


def register_handler(event_bus: EventBus, topic: str, handler: Callable[[dict], None]) -> None:
    event_bus.subscribe(topic, handler)
