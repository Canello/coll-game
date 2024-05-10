from typing import Any, Callable

from .world_events_manager import WorldEventsManager
from .collision_handler import CollisionHandler
from .world_event import WorldEvent
from .objects.world_object import WorldObject
from .objects.player import Player

class World:
    def __init__(
        self,
        world_events_manager: WorldEventsManager,
        collision_handler: CollisionHandler,
        player: Player
    ) -> None:
        self._world_events_manager = world_events_manager
        self._collision_handler = collision_handler
        self.player = player
        self._objects = [self.player]

    def add_object(self, object: WorldObject) -> None:
        self._objects.append(object)

    def add_event_listener(self, event_type: str, notify: Callable[[WorldEvent], Any]) -> None:
        self._world_events_manager.add_event_listener(event_type, notify)

    def apply_input(self, char: str) -> None:
        # logic to process input char and decide what to do with it
        # ie: do something to player, do something to world objects, etc
        # for now just doing something to player is enough
        # probably will need some input handler object to encpsulate this logic
        pass

    def tick(self) -> None:
        self._handle_collisions()
        self._apply_movements()

    def _handle_collisions(self) -> None:
        self._collision_handler.handle(self._objects, self._world_events_manager.send)

    def _apply_movements(self) -> None:
        for object in self._objects:
            object.move()