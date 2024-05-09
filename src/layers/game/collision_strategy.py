from typing import Any, Callable

from .objects.world_object import WorldObject
from .physics import Physics
from .force import Force

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
        # in the x axis, we have four sides in total, from both objects
        # two sides delimit the x intersection, the two in the middle
        sides_x = [self._owner.left, self._owner.right, obj.left, obj.right]
        sides_x.sort()
        penetration_x = sides_x[2] - sides_x[1]
        normalized_penetration_x = penetration_x / obj.width

        # same logic from above, but for y axis
        sides_y = [self._owner.top, self._owner.bottom, obj.top, obj.bottom]
        sides_y.sort()
        penetration_y = sides_y[2] - sides_y[1]
        normalized_penetration_y = penetration_y / obj.height

        if normalized_penetration_y > normalized_penetration_x:
            # move outwards in the x direction to the closest border from the center
            distance_to_left_border = abs(obj.center.x - self._owner.left)
            distance_to_right_border = abs(obj.center.x - self._owner.right)
            if distance_to_left_border < distance_to_right_border:
                # set obj x to left border - width
                obj.x = self._owner.left - obj.width
            else:
                # set obj x to right border
                obj.x = self._owner.right
        else:
            # move outwards in the y direction to the closest border from the center
            distance_to_top_border = abs(obj.center.y - self._owner.top)
            distance_to_bottom_border = abs(obj.center.y - self._owner.bottom)
            if distance_to_top_border < distance_to_bottom_border:
                # set obj y to top border - height
                obj.y = self._owner.top - obj.height
            else:
                # set obj y to bottom border
                obj.y = self._owner.bottom

class GhostCollisionStrategy(CommonCollisionStrategy):
    def __init__(self, owner: WorldObject) -> None:
        super().__init__(owner)

    def apply(self, obj: WorldObject, on_collision: Callable[[], Any]=lambda: None) -> None:
        return