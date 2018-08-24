from abc import ABCMeta, abstractmethod


class Spell(metaclass=ABCMeta):
    """Creates a spell"""

    def __init__(self, name: str, incantation: str, effect: str, min_year: int = None):
        self.name = name
        self.incantation = incantation
        self.effect = effect
        self.min_year = min_year

    @abstractmethod
    def cast(self):
        pass

    @property
    @abstractmethod
    def defining_feature(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, incantation: '{self.incantation}', effect: {self.effect})"


class Charm(Spell):
    """
    Creates a charm  -
    a spell that alters the inherent qualities of an object
    """

    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super().__init__(name, incantation, effect, min_year)
        self.difficulty = difficulty

    @property
    def defining_feature(self):
        return ("Alteration of the object's inherent qualities, "
                "that is, its behaviour and capabilities")

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def lumos(cls):
        return cls('Lumos', 'Lumos', 'Illuminates the wand tip', 'simple', min_year=5)

    @classmethod
    def wingardium_leviosa(cls):
        return cls('Wingardium Leviosa', 'Wingardium Leviosa', 'Makes objects fly', 'simple', min_year=1)


class Transfiguration(Spell):
    """
    Creates a transfiguration -
    a spell that alters the form or appearance of an object
    """

    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return "Alteration of the object's form or appearance"

    def cast(self):
        pass


class Jinx(Spell):
    """
    Creates a jinx -
    a spell whose effects are irritating but amusing
    """

    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return ("Minor darf magic - "
                "a spell whose effects are irritating but amusing, "
                "almost playful and of minor inconvenience to the target")

    def cast(self):
        pass


class Hex(Spell):
    """
    Creates a hex -
    a spell that affects an object in a negative manner
    """

    def __init__(self, name: str, incantation: str, effect: str, min_year: int = None):
        super().__init__(name, incantation, effect, min_year)

    @property
    def defining_feature(self):
        return ("Medium dark magic - "
                "Affects an object in a negative manner. "
                "Major inconvenience to the target.")

    def cast(self):
        pass


class Curse(Spell):
    """
    Creates a curse -
    a spell that affects an object in a strongly negative manner
    """

    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return ("Worst kind of dark magic - "
                "Intended to affect an object in a strongly negative manner.")

    def cast(self):
        pass


class CounterSpell(Spell):
    """
    Creates a counter-spell -
    a spell that inhibits the effect of another spell
    """

    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return ("Inhibites the effects of another spell")

    def cast(self):
        pass


class HealingSpell(Spell):
    """
    Creates a healing-spell -
    a spell that improves the condition of a living object
    """

    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return "Improves the condition of a living object"

    def cast(self):
        pass
