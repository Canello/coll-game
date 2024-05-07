from typing import Any, Callable

from .world_event import WorldEvent
from .objects.world_object import WorldObject

class CollisionHandler:
    def __init__(self) -> None:
        pass

    def handle(self, objects: list[WorldObject], send: Callable[[WorldEvent], Any]) -> None:
        pass