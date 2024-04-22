from typing import Any, Callable

from keyboard_event import KeyboardEvent

class KeyboardListener:
    def __init__(self) -> None:
        pass

    def add_event_listener(event_type: str, notify: Callable[[KeyboardEvent], Any]):
        pass