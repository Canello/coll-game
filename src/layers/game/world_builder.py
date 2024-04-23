from .world import World
from .game_factory import GameFactory
from .objects.player import Player

class WorldBuilder:
    def __init__(self) -> None:
        pass

    def build(self) -> World:
        # create objects and set their positions
        player = Player()
        objects = []

        # instantiate world
        world = GameFactory.make_world(player)

        # add objects to the world
        for object in objects:
            world.add_object(object)
        
        return world