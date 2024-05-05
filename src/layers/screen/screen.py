import tkinter as tk
import threading
from typing import Any, Callable

class Screen:
    _instance = None
    _has_been_instantiated = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not Screen._has_been_instantiated:
            gui_setup_event = threading.Event()
            gui_thread = threading.Thread(target=self._run_gui, args=(gui_setup_event,))
            gui_thread.start()
            gui_setup_event.wait() # ensure that gui is setted up, to prevent adding event listener to inexistent window
            Screen._has_been_instantiated = True

    def draw_rect(self, x: float, y: float, width: float, heigth: float, fill: str="blue") -> None:
        self._canvas.create_rectangle(x, y, x + width, y + heigth, fill=fill)

    def draw_img(self, filename: str, width: float, height: float) -> None:
        # picks the img with filename in images folder
        # then paints it
        pass

    def clear(self) -> None:
        self._canvas.delete("all")

    def listen_to_keypress(self, on_key_press: Callable[[tk.Event], Any]):
        self._window.bind("<Key>", on_key_press)

    def _run_gui(self, gui_setup_event: threading.Event) -> None:
        self._window = tk.Tk()
        self._window.title = "World"
        self._canvas = tk.Canvas(self._window, width=600, height=600)
        self._canvas.pack()
        gui_setup_event.set()
        self._window.mainloop()