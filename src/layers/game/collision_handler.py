from typing import Any, Callable

from .world_event import WorldEvent
from .objects.object import Object

class CollisionHandler:
    def __init__(self) -> None:
        pass

    def handle(self, objects: list[Object], send: Callable[[WorldEvent], Any]) -> None:
        pass