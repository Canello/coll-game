from .game import Game
from .world_builder import WorldBuilder
from .world import World
from .world_events_manager import WorldEventsManager
from .collision_handler import CollisionHandler
from .scoreboard import Scoreboard
from .objects.player import Player

class GameFactory:
    """
    Responsible for dependency injection on objects from the game layer.
    """

    @staticmethod
    def make_game(player: Player) -> Game:
        world_builder = WorldBuilder()
        scoreboard = Scoreboard()
        return Game(world_builder, scoreboard)
    
    @staticmethod
    def make_world() -> World:
        world_events_manager = WorldEventsManager()
        collision_handler = CollisionHandler()
        return World(world_events_manager, collision_handler)