from .world import World
from .game_factory import GameFactory
from .objects.player import Player
from .objects.ball import Ball
from .objects.wall import Wall
from .objects.goal import Goal

class WorldBuilder:
    def __init__(self) -> None:
        pass

    def build(self) -> World:
        # create objects and set their positions
        player = Player()
        objects = [
            Wall(x=40, y=160),
        ]

        # instantiate world
        world = GameFactory.make_world(player)

        # add objects to the world
        for object in objects:
            world.add_object(object)
        
        return world