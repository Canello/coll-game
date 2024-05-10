import threading

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
        game_thread = threading.Thread(target=self._game_loop)
        game_thread.start()
    
    def _game_loop(self) -> None:
        while True:
            self._world.tick()

    def notify(self, char: str) -> None:
        self._world.apply_input(char)
