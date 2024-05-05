from .client import Client

class ClientFactory:
    """
    Responsible for dependency injection on objects from the client layer.
    """

    @staticmethod
    def make_client() -> Client:
        return Client()