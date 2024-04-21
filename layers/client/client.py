from typing import Any, Callable

class Client:
    def __init__(
        self,
        keyboard_listener: KeyboardListener,
        input_handler: InputHandler
    ) -> None:
        self.keyboard_listener = keyboard_listener
        self.input_handler = input_handler
        self.keyboard_listener.add_event_listener("keydown", input_handler.notify)

    def add_event_listener(self, event_type: str, notify: Callable[[InputEvent], Any]):
        self.input_handler.add_event_listener(event_type, notify)