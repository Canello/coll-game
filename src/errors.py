class EventNotFoundError(Exception):
    def __init__(self, event_type: str):
        self.message = "There are no listeners for the event type: " + event_type
        super().__init__(self.message)