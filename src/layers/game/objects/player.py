from .world_object import WorldObject
from ..physics import Physics
from ..collision_strategy import CommonCollisionStrategy

class Player(WorldObject):
    def __init__(
        self,
        width: float = 10,
        height: float = 10,
        x: float = 0,
        y: float = 0,
        sx: float = 0,
        sy: float = 0,
        ax: float = 0,
        ay: float = 0,
        mass: float = 1
    ) -> None:
        super().__init__(width, height, x, y, sx, sy, ax, ay, mass)
        self.collision_strategy = CommonCollisionStrategy()