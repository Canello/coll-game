from .object import Object
from ..collision_strategy import CollisionStrategy

class Ball(Object):
    def __init__(self, x: int = 0, y: int = 0, sx: int = 0, sy: int = 0, ax: int = 0, ay: int = 0, mass: float = 1) -> None:
        super().__init__(x, y, sx, sy, ax, ay, mass)
        self.collision_strategy = BallCollisionStrategy()

    def move() -> None:
        # gravity should be applied
        pass

class BallCollisionStrategy(CollisionStrategy):
    pass