from ..force import Force
from ..collision_strategy import CollisionStrategy

class Object:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        sx: int = 0,
        sy: int = 0,
        ax: int = 0,
        ay: int = 0,
        mass: float = 1
    ) -> None:
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.ax = ax
        self.ay = ay
        self.mass = mass
        self.external_forces: list[Force] = []
        self.collision_strategy: CollisionStrategy = {"default collision strategy"}

    def draw(self) -> None:
        pass

    def move(self) -> None:
        pass

    def add_external_force(self, force: Force) -> None:
        self.external_forces.append(force)

    def reset_external_forces(self) -> None:
        self.external_forces = []