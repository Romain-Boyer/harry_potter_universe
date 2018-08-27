from dataclasses import dataclass

from ghost import Ghost
from professor import Professor


@dataclass
class House:
    name: str
    traits: list
    head: Professor
    ghost: Ghost
    founded_in: int = 991

    def current_age(self):
        return NOW - self.founded_in + 1
