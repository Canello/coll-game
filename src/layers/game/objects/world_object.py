from ..force import Force
from ..physics import Physics
from ..collision_strategy import CollisionStrategy
from ..coordinate import Coordinate

class WorldObject:
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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.ax = ax
        self.ay = ay
        self.mass = mass
        self.external_forces: list[Force] = []
        self.collision_strategy: CollisionStrategy = CollisionStrategy(self)

    @property
    def center(self) -> Coordinate:
        return Coordinate(
            self.x + self.width / 2,
            self.y + self.height / 2
        )
    
    @property
    def top(self) -> float:
        return self.y
    
    @property
    def bottom(self) -> float:
        return self.y + self.height
    
    @property
    def left(self) -> float:
        return self.x
    
    @property
    def right(self) -> float:
        return self.x + self.width

    def draw(self) -> None:
        pass

    def move(self) -> None:
        net_force = self._get_net_force()
        self.ax = self.ax + net_force / self.mass
        self.vx = self.vx + self.ax * Physics.DT
        self.x = self.x + self.vx * Physics.DT

    def add_external_force(self, force: Force) -> None:
        self.external_forces.append(force)

    def reset_external_forces(self) -> None:
        self.external_forces = []

    def _get_net_force(self) -> Force:
        fx = 0
        fy = 0
        for force in self.external_forces:
            fx += force.x
            fy += force.y
        return Force(fx, fy)