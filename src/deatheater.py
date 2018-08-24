from typing import NamedTuple


class DeathEater(NamedTuple):
    """
    Creates a Deatheater
    """
    name: str
    birthyear: int

    @property
    def leader(self):
        return DeathEater('Voldemort', 1926)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, birthyear: {self.birthyear})"
