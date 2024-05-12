from typing import Any, Callable

from .world_event import WorldEvent
from ..utils.errors import EventNotFoundError

class WorldEventsManager:
    def __init__(self) -> None:
        self._observers: dict[str, list[Callable[[WorldEvent], Any]]] = dict()

    def add_event_listener(self, event_type: str, notify: Callable[[WorldEvent], Any]) -> None:
        if event_type not in self._observers:
            self._observers[event_type] = []
        self._observers[event_type].append(notify)

    def send(self, event_type: str, event: WorldEvent) -> None:
        if event_type not in self._observers:
            raise EventNotFoundError(event_type)
        for notify in self._observers[event_type]:
            notify(event)