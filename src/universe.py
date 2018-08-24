import datetime
from abc import ABCMeta, abstractmethod
from typing import NamedTuple

NOW = 1994


class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
    """

    location = 'England'

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"

    def says(self, words):
        return f'{self._name} says "{words}"'

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]

        print(f"{self._name} is {', '.join(true_traits)} "
              f"but not {', '.join(false_traits)}")

    def exhibits_trait(self, trait):
        try:
            value = self._traits[trait]
        except KeyError:
            print(f"{self._name} does not have a character trait with the name '{trait}'")
            return

        if value:
            print(f"Yes, {self._name} is {trait}!")
        else:
            print(f"No, {self._name} is not {trait}!")

        return value

    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1

    @classmethod
    def dumbledore(cls):
        return cls('Albus Percival Wulfric Brian Dumbledore', 1881, 'male')

    @property
    def age(self):
        # now = datetime.datetime.now().year
        now = NOW
        return now - self.birthyear


class Pupil(HogwartsMember):
    """
    Creates a Hogwarts pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year
        self.known_spells = set()

        if pet is not None:
            self.pet_name, self_pet_type = pet

        self._owls = {
            'Study of Ancient Runes': False,
            'Arithmancy': False,
            'Astronomy': False,
            'Care of Magical Creatures': False,
            'Charms': False,
            'Defence Against the Dark Arts': False,
            'Divination': False,
            'Herbology': False,
            'History of Magic': False,
            'Muggle Studies': False,
            'Potions': False,
            'Transfiguration': False
        }

        self._friends = set()

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear}, house: {self.house})")

    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed.
        """
        grades = {
            'O': True,
            'Ordinary': True,
            'P': True,
            'Passed': True,
            'A': True,
            'Acceptable': True,
            'Poor': False,
            'H': False,
            'Horrible': False,
        }

        return grades.get(grade, False)

    @classmethod
    def harry(cls):
        return cls('Harry James Potter', 1980, 'male', 'Griffindor', start_year=1991, pet=('Hedwig', 'owl'))

    @classmethod
    def ron(cls):
        return cls('Ronald Bilius Weasley', 1980, 'male', 'Griffindor', 1991, pet=('Pigwidgeon', 'owl'))

    @classmethod
    def hermione(cls):
        hermione_ = cls('Hermione Granger', 1979, 'female', 'Griffindor', 1991, pet=('Crookshanks', 'cat'))
        hermione_.add_trait('highly intelligent')
        return hermione_

    @classmethod
    def malfoy(cls):
        return cls('Draco Lucius Malfoy', 1980, 'male', 'Slytherin', 1991, pet=('Unnamed', 'owl'))

    @property
    def owls(self):
        return self._owls

    @property
    def current_year(self):
        # now = datetime.datetime.now().year
        now = NOW
        return now - self.start_year + 1

    @property
    def friends(self):
        if not self._friends:
            return f"{self._name} has no friend"
        return f"{self._name}'s current friends are {[person._name for person in self._friends]}"

    @owls.setter
    def owls(self, subject_and_grade):
        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError('Pass an interable with two items: subject and grade!')

        passed = self.passed(grade)

        if passed:
            self._owls[subject] = True
        else:
            print('The exam was not passed, so no Owl was awarded!')

    @owls.deleter
    def owls(self):
        print("Caution, you are deleting this students' ELM's! "
              "You should only do that if she/he dropped out of school without passing any exam!")
        del self._owls

    def be_friend(self, person):
        """Adds another person to your list of friends"""
        if (person.__class__.__name__ != 'HogwartsMember'
                and self.house != 'Slytherin'
                and person.house == 'Slytherin'):
            print('Are you sure you want to be friends with someone from Slytherin ?')

        self._friends.add(person)
        print(f'{person._name} is now your friend !')

    def learn_spell(self, spell):
        """
        Allows a pupil to learn a spell, given that he/she is old enough
        """
        if spell.min_year is not None:
            if self.current_year >= spell.min_year:
                print(f"{self._name} now knows spell {spell.name}")
                self.known_spells.add(spell)

            elif self.exhibits_trait('highly intelligent'):
                print(f"{self._name} now knows spell {spell.name}")
                self.known_spells.add(spell)

            elif self.current_year < spell.min_year:
                print(f"{self._name} is too young to study this spell!")

        elif spell.__class__.__name__ in ['Hex', 'Curse']:
            # Only Slytherin's would study hexes and curses
            if self.house == 'Slytherin':
                print(f"{self._name} now knows spell {spell.name}")
                self.known_spells.add(spell)

            else:
                print(f"How dare you study a hex or curse?!")

        else:
            print(f"{self._name} now knows spell {spell.name}")
            self.known_spells.add(spell)

    def cast_spell(self, spell):
        """
        Allows a pupil to cast a spell
        """
        if spell.__class__.__name__ == 'Curse':
            print("This is dark magic - stay away from performing curses!")

        elif spell.__class__.__name__ == 'Hex':
            if self.house == 'Slytherin':
                print(f"{self._name}: {spell.incantation}!")
            else:
                print(f"You shouldn't cast a hex, that's mean!")

        elif spell in self.known_spells:
            print(f"{self._name}: {spell.incantation}!")

        elif spell.name not in self.known_spells:
            print(f"You can't cast the {spell.name} spell correctly "
                  f" - you have to study it first! ")


class Professor(HogwartsMember):
    """
    Creates a Hogwarts professor
    """

    def __init__(self, name: str, birthyear: int, sex: str, subject: str, house: str = None):
        super().__init__(name, birthyear, sex)
        self.subject = subject

        if house is not None:
            self.house = house

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")

    @staticmethod
    def saluate_pupil():
        return "Hello student !"

    @classmethod
    def mcgonagall(cls):
        return cls('Minerva McGonagall', 1935, 'female', 'Transfiguration', house='Griffindor')

    @classmethod
    def snape(cls):
        return cls('Severus Snape', 1960, 'male', 'Potions', house='Slytherin')


class Ghost(HogwartsMember):
    """
    Creates a Hogwarts ghost
    """

    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int, house: str = None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, year of death: {self.year_of_death})")

    @staticmethod
    def saluate_pupil():
        return "BoooOOOooooh ! I'am a ghoooost"

    @classmethod
    def nearly_headless_nick(cls):
        return cls('Sir Nicholas de Mimsy-Porpington', 1401, 'male', '1492', 'Gryffindor')


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


class Spell(metaclass=ABCMeta):
    """Creates a spell"""
    def __init__(self, name:str, incantation:str, effect:str, min_year: int = None):
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
    def __init__(self, name:str, incantation:str, effect:str, difficulty: str = None, min_year: int = None):
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
    def __init__(self, name: str, incantation:str, effect:str):
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
    def __init__(self, name: str, incantation:str, effect:str):
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
    def __init__(self, name: str, incantation:str, effect:str, min_year: int = None):
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
    def __init__(self, name: str, incantation:str, effect:str, difficulty: str = None):
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
    def __init__(self, name: str, incantation:str, effect:str):
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
    def __init__(self, name: str, incantation:str, effect:str):
        super().__init__(name, incantation, effect)

    @property
    def defining_feature(self):
        return "Improves the condition of a living object"

    def cast(self):
        pass


if __name__ == '__main__':
    hagrid = HogwartsMember('Hagrid', 1952, 'male')
    dumby = HogwartsMember.dumbledore()

    harry = Pupil.harry()
    ron = Pupil.ron()
    hermione = Pupil.hermione()
    malfoy = Pupil.malfoy()

    snape = Professor.snape()
    mcgonagall = Professor.mcgonagall()

    nick = Ghost.nearly_headless_nick()

    lumos = Charm.lumos()
    wingardium_leviosa = Charm.wingardium_leviosa()

    ron.add_trait('kind')
    ron.add_trait('tidy-minded')
    ron.add_trait('impatient', value=False)

    bellatrix = DeathEater('Bellatrix Lestrange', 1951)

    wing_lev = Charm.wingardium_leviosa()
    rictum = Charm('tickling_charm', 'Rictumsempra', 'Causes victim to buckle with laughter', min_year=5)
    stickfast = Hex('stickfast_hex', 'Colloshoo', "Makes target's shoes stick to ground")
    crutio = Curse('Cruciatus Curse', 'Crucio', 'Causes intense, excruciating pain on the victim', 'difficult')

    print('Day 1\n')
    print(hagrid.says("Hello Harry !"))
    print(harry.says("Hello giant one !"))
    print('=' * 30)

    print('Day 2\n')
    print(snape.saluate_pupil())
    print(nick.saluate_pupil())
    print(f"Is Peter a full name : {Pupil.is_full_name('Peter')}")
    print('=' * 30)

    print('Day 4\n')
    print(harry)
    print('=' * 30)

    print('Day 6\n')
    print(f"Harry is {harry.age} years old")
    print("Today harry passed his potion exam !!")
    print(f'Before, Harry\'s grade : {harry.owls["Potions"]}')
    harry.owls = ('Potions', 'P')
    print(f'And now Harry\'s grade : {harry.owls["Potions"]}')
    print('=' * 30)

    print('Day 8\n')
    print(harry.friends)
    harry.be_friend(ron)
    harry.be_friend(hermione)
    print(harry.friends)
    lumos.cast()
    print('=' * 30)

    print('Day 9\n')
    ron.print_traits()
    ron.exhibits_trait('kind')
    ron.exhibits_trait('fat')
    print('=' * 30)

    print('Day 10-11\n')
    print(bellatrix)
    print(bellatrix.name)
    print(f'{bellatrix.leader.name} is Beatrix\' leader')
    print('=' * 30)

    print('Day 12-15\n')
    print("Harry knows the following spells: ", harry.known_spells or 'None')
    print("Harry is currently in year: ", harry.current_year)
    harry.learn_spell(wing_lev)

    # Test whether Harry can learn a spell he is too young for
    harry.learn_spell(rictum)
    # Can hermione study the spell?
    hermione.learn_spell(rictum)

    harry.cast_spell(wing_lev)
