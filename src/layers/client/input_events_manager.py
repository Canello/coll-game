from typing import Any, Callable

class InputEventsManager:
    def __init__(self) -> None:
        pass

    def add_event_listener(self, notify: Callable[[InputEvent], Any]) -> None:
        pass

    def send_to_all(self, event: InputEvent) -> None:
        pass