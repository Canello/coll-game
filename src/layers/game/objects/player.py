from .world_object import WorldObject
from ..collision_strategy import CollisionStrategy

class Player(WorldObject):
    def __init__(self, x: int = 0, y: int = 0, sx: int = 0, sy: int = 0, ax: int = 0, ay: int = 0, mass: float = 10) -> None:
        super().__init__(x, y, sx, sy, ax, ay, mass)
        self.collision_strategy = PlayerCollisionStrategy()

    def move() -> None:
        # gravity should be applied
        pass

class PlayerCollisionStrategy(CollisionStrategy):
    pass