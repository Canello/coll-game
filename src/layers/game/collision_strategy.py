from typing import Any, Callable

from .objects.world_object import WorldObject

class CollisionStrategy:
    def __init__(self, owner: WorldObject) -> None:
        self._owner = owner

    def apply(self, obj: WorldObject, on_collision: Callable[[], Any]=lambda: None) -> None:
        pass

class CommonCollisionStrategy(CollisionStrategy):
    def __init__(self, owner: WorldObject) -> None:
        super().__init__(owner)

    def apply(self, obj: WorldObject, on_collision: Callable[[], Any]=lambda: None) -> None:
        penetration_x = obj.center.x - self._owner.center.x
        penetration_y = obj.center.y - self._owner.center.y
        # apply elastic force based on penetration
        pass

class WallCollisionStrategy(CollisionStrategy):
    def __init__(self, owner: WorldObject) -> None:
        super().__init__(owner)

    def apply(self, obj: WorldObject, on_collision: Callable[[], Any]=lambda: None) -> None:
        # check object direction
        # move it to owner border
        pass

class GhostCollisionStrategy(CommonCollisionStrategy):
    def __init__(self, owner: WorldObject) -> None:
        super().__init__(owner)

    def apply(self, obj: WorldObject, on_collision: Callable[[], Any]=lambda: None) -> None:
        return