from typing import Any, Callable

from .world_events_manager import WorldEventsManager
from .collision_handler import CollisionHandler
from .world_event import WorldEvent
from .objects.world_object import WorldObject
from .objects.player import Player
from .input_handler import InputHandler

class World:
    def __init__(
        self,
        world_events_manager: WorldEventsManager,
        collision_handler: CollisionHandler,
        input_handler: InputHandler,
        player: Player,
    ) -> None:
        self._world_events_manager = world_events_manager
        self._collision_handler = collision_handler
        self._input_handler = input_handler
        self.player = player
        self._objects = [self.player]

    def add_object(self, object: WorldObject) -> None:
        self._objects.append(object)

    def add_event_listener(self, event_type: str, notify: Callable[[WorldEvent], Any]) -> None:
        self._world_events_manager.add_event_listener(event_type, notify)

    def apply_input(self, char: str) -> None:
        # TODO
        # this probably will have some weird behaviour
        # as this is being called from another thread, two things might happen:
        # 1 - forces will be added multiple times before resetting, then, it will be much stronger than it should
        # 2 - forces will be added once every many ticks, so it will be intermittent
        self._input_handler.handle(char, self.player)

    def tick(self) -> None:
        self._handle_collisions()
        self._apply_movements()
        self._reset_forces()

    def _handle_collisions(self) -> None:
        self._collision_handler.handle(self._objects, self._world_events_manager.send)

    def _apply_movements(self) -> None:
        for object in self._objects:
            object.move()

    def _reset_forces(self) -> None:
        for obj in self._objects:
            obj.reset_external_forces()