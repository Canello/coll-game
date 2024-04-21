from .game import Game

class GameFactory:
    """
    Responsible for dependency injection on objects from the game layer.
    """

    @staticmethod
    def make_game() -> Game:
        world_builder = GameFactory.make_world_builder()
        scoreboard = GameFactory.make_scoreboard()
        return Game(world_builder, scoreboard)
    
    @staticmethod
    def make_world_builder() -> WorldBuilder:
        return WorldBuilder()
    
    @staticmethod
    def make_scoreboard() -> Scoreboard:
        return Scoreboard()