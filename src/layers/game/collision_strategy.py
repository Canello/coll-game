from __future__ import annotations
from typing import Any, Callable, TYPE_CHECKING

from .physics import Physics
from .force import Force
if TYPE_CHECKING: # avoid circular import bacause of type annotation
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
        fx = Physics.SPRING_CONSTANT * penetration_x
        fy = Physics.SPRING_CONSTANT * penetration_y
        collision_force = Force(fx, fy)
        obj.add_external_force(collision_force)

class WallCollisionStrategy(CollisionStrategy):
    def __init__(self, owner: WorldObject) -> None:
        super().__init__(owner)

    def apply(self, obj: WorldObject, on_collision: Callable[[], Any]=lambda: None) -> None:
        normalized_penetration_x = self._get_normalized_penetration_x(obj)
        normalized_penetration_y = self._get_normalized_penetration_y(obj)
        if normalized_penetration_y > normalized_penetration_x:
            self._move_outwards_to_closest_x_border(obj)
        else:
            self._move_outwards_to_closest_y_border(obj)

    def _get_normalized_penetration_x(self, obj: WorldObject) -> float:
        # in the x axis, we have four sides in total from both objects
        # two of them delimit the x intersection between the objects - the two sides in the middle
        sides_x = [self._owner.left, self._owner.right, obj.left, obj.right]
        sides_x.sort()
        penetration_x = sides_x[2] - sides_x[1]
        normalized_penetration_x = penetration_x / obj.width
        return normalized_penetration_x
    
    def _get_normalized_penetration_y(self, obj: WorldObject) -> float:
        # in the y axis, we have four sides in total from both objects
        # two of them delimit the y intersection between the objects - the two sides in the middle
        sides_y = [self._owner.top, self._owner.bottom, obj.top, obj.bottom]
        sides_y.sort()
        penetration_y = sides_y[2] - sides_y[1]
        normalized_penetration_y = penetration_y / obj.height
        return normalized_penetration_y
    
    def _move_outwards_to_closest_x_border(self, obj: WorldObject) -> None:
        distance_to_left_border = abs(obj.center.x - self._owner.left)
        distance_to_right_border = abs(obj.center.x - self._owner.right)
        if distance_to_left_border < distance_to_right_border:
            obj.x = self._owner.left - obj.width
        else:
            obj.x = self._owner.right
        obj.sx = 0
        obj.ax = 0

    def _move_outwards_to_closest_y_border(self, obj: WorldObject) -> None:
        distance_to_top_border = abs(obj.center.y - self._owner.top)
        distance_to_bottom_border = abs(obj.center.y - self._owner.bottom)
        if distance_to_top_border < distance_to_bottom_border:
            obj.y = self._owner.top - obj.height
        else:
            obj.y = self._owner.bottom
        obj.sy = 0
        obj.ay = 0

class GhostCollisionStrategy(CommonCollisionStrategy):
    def __init__(self, owner: WorldObject) -> None:
        super().__init__(owner)

    def apply(self, obj: WorldObject, on_collision: Callable[[], Any]=lambda: None) -> None:
        return