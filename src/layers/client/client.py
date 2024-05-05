from typing import Any, Callable
import tkinter as tk

from .input_event import InputEvent
from .input_handler import InputHandler

class Client:
    def __init__(
        self,
        input_handler: InputHandler
    ) -> None:
        self._input_handler = input_handler

    def add_event_listener(self, notify: Callable[[InputEvent], Any]):
        self._input_handler.add_event_listener(notify)

    def notify(self, event: tk.Event) -> None:
        self._input_handler.notify(event)
