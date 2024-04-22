from typing import Any, Callable

from .input_event import InputEvent
from .keyboard_listener import KeyboardListener
from .input_handler import InputHandler

class Client:
    def __init__(
        self,
        keyboard_listener: KeyboardListener,
        input_handler: InputHandler
    ) -> None:
        self._keyboard_listener = keyboard_listener
        self._input_handler = input_handler
        self._keyboard_listener.add_event_listener("keydown", input_handler.notify)

    def add_event_listener(self, notify: Callable[[InputEvent], Any]):
        self._input_handler.add_event_listener(notify)