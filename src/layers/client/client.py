from typing import Any, Callable
import tkinter as tk

class Client:
    def __init__(self) -> None:
        self._observers = []

    def add_event_listener(self, notify: Callable[[str], Any]) -> None:
        self._observers.append(notify)

    def notify(self, event: tk.Event) -> Any:
        try:
            self._send_to_all(event.char)
        except:
            pass # invalid event

    def _send_to_all(self, char: str) -> None:
        for notify in self._observers:
            notify(char)
