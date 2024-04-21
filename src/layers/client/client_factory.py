from .client import Client

class ClientFactory:
    """
    Responsible for dependency injection on objects from the client layer.
    """

    @staticmethod
    def make_client() -> Client:
        keyboard_listener = ClientFactory.make_keyboard_listener()
        input_handler = ClientFactory.make_input_handler()
        return Client(keyboard_listener, input_handler)
    
    @staticmethod
    def make_keyboard_listener() -> KeyboardListener:
        return KeyboardListener()

    @staticmethod
    def make_input_handler() -> InputHandler:
        input_filter = ClientFactory.make_input_filter()
        input_events_manager = ClientFactory.make_input_events_manager()
        return InputHandler(input_filter, input_events_manager)
    
    @staticmethod
    def make_input_filter() -> InputFilter:
        return InputFilter()
    
    @staticmethod
    def make_input_events_manager() -> InputEventsManager:
        return InputEventsManager()