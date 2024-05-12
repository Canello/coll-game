from .objects.player import Player
from .physics import Physics
from .force import Force

class InputHandler:
    def __init__(self) -> None:
        self._handlers = {
            "w": self._move_up,
            "d": self._move_right,
            "s": self._move_down,
            "a": self._move_left,
        }

    def handle(self, char: str, player: Player) -> None:
        if char in self._handlers:
            handler = self._handlers[char]
            handler(player)

    def _move_up(self, player: Player) -> None:
        force = Force(0, Physics.INPUT_FORCE)
        player.add_external_force(force)

    def _move_right(self, player: Player) -> None:
        force = Force(Physics.INPUT_FORCE, 0)
        player.add_external_force(force)

    def _move_down(self, player: Player) -> None:
        force = Force(0, -Physics.INPUT_FORCE)
        player.add_external_force(force)

    def _move_left(self, player: Player) -> None:
        force = Force(-Physics.INPUT_FORCE, 0)
        player.add_external_force(force)