from typing import Any, Callable
import tkinter as tk

from .input_filter import InputFilter
from .input_events_manager import InputEventsManager
from .input_event import InputEvent

class InputHandler:
    def __init__(
        self,
        input_filter: InputFilter,
        input_events_manager: InputEventsManager
    ) -> None:
        self._input_filter = input_filter
        self._input_events_manager = input_events_manager

    def notify(self, event: tk.Event) -> Any:
        input_event = self._input_filter.filter(event.char)
        if (input_event != None):
            self._input_events_manager.send_to_all(input_event)

    def add_event_listener(self, notify: Callable[[InputEvent], Any]) -> None:
        self._input_events_manager.add_event_listener(notify)