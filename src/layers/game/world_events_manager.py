from typing import Any, Callable

from .world_event import WorldEvent

class WorldEventsManager:
    def __init__(self) -> None:
        pass

    def add_event_listener(event_type: str, notify: Callable[[WorldEvent], Any]) -> None:
        pass

    def send(event_type: str, event: WorldEvent) -> None:
        pass