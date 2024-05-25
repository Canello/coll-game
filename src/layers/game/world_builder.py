from .world import World
from .objects.player import Player
from .objects.ball import Ball
from .objects.wall import Wall
from .objects.goal import Goal

class WorldBuilder:
    def __init__(self) -> None:
        pass

    def build(self) -> World:
        from .game_factory import GameFactory # importing here to avoid circular import between GameFactory and WorldBuilder

        # create objects and set their positions
        player = Player(x=10, y=10)
        objects = [
            Wall(x=40, y=160, width=80, height=80),
        ]

        # instantiate world
        world = GameFactory.make_world(player)

        # add objects to the world
        for object in objects:
            world.add_object(object)
        
        return world