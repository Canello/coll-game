from typing import Any, Callable

from .world_event import WorldEvent
from .objects.world_object import WorldObject

class CollisionHandler:
    def __init__(self) -> None:
        pass

    def handle(self, objects: list[WorldObject], send: Callable[[WorldEvent], Any]) -> None:
        # TODO -> try to make it less than O(n^2)
        for obj1 in objects:
            for obj2 in objects:
                if obj1 is obj2:
                    continue
                if self._is_collision(obj1, obj2):
                    obj1.collision_strategy.apply(obj2, send)

    def _is_collision(self, obj1: WorldObject, obj2: WorldObject):
        x_intercepts = obj1.x + obj1.width > obj2.x and obj1.x < obj2.x + obj2.width
        y_intercepts = obj1.y + obj1.height > obj2.y and obj1.y < obj2.y + obj2.height
        return x_intercepts and y_intercepts