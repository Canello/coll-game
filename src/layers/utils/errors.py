class EventNotFoundError(Exception):
    def __init__(self, event_type: str) -> None:
        self.message = "There are no listeners for event type: " + event_type
        super().__init__(self.message)