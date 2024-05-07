from .scoreboard import Scoreboard
from .world_builder import WorldBuilder

class Game:
    def __init__(
        self,
        world_builder: WorldBuilder,
        scoreboard: Scoreboard
    ) -> None:
        self._world = world_builder.build()
        self._scoreboard = scoreboard
        self._world.add_event_listener("score", self._scoreboard.notify)

    def start(self) -> None:
        pass

    def notify(self, char: str) -> None:
        # receives keypress events
        pass
