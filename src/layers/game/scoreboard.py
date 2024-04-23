from .world_event import WorldEvent

class Scoreboard:
    def __init__(self) -> None:
        self.score1 = 0
        self.score2 = 0

    def notify(self, event: WorldEvent) -> None:
        pass

    def increase_score1() -> None:
        pass

    def increase_score2() -> None:
        pass

    def decrease_score1() -> None:
        pass

    def decrease_score2() -> None:
        pass

    def reset() -> None:
        pass