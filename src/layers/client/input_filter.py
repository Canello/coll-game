from .keyboard_event import KeyboardEvent
from .input_event import InputEvent

class InputFilter:
    def __init__(self) -> None:
        pass

    def filter(event: KeyboardEvent) -> InputEvent:
        pass