class Game:
    def __init__(
        self,
        world_builder: WorldBuilder,
        scoreboard: Scoreboard
    ) -> None:
        self.world = world_builder.build()
        self.scoreboard = scoreboard

    def start() -> None:
        pass

    def notify(event: InputEvent) -> None:
        pass



