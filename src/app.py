from layers.client.client_factory import ClientFactory
from layers.game.game_factory import GameFactory
from layers.screen.screen import Screen

class App:
    @staticmethod
    def main() -> None:
        client = ClientFactory.make_client()
        game = GameFactory.make_game()
        screen = Screen()
        screen.listen_to_keypress(client.notify)
        client.add_event_listener("input", game.notify)
        game.start()

if __name__ == "__main__":
    App.main()