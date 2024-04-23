from layers.client.client_factory import ClientFactory
from layers.game.game_factory import GameFactory

class App:
    @staticmethod
    def main() -> None:
        client = ClientFactory.make_client()
        game = GameFactory.make_game()
        client.add_event_listener("input", game.notify)
        game.start()

if __name__ == "__main__":
    App.main()