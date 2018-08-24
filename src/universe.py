class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
    """

    location = 'England'

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"

    def says(self, words):
        return f'{self._name} says "{words}"'

    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1

    @classmethod
    def dumbledore(cls):
        return cls('Albus Percival Wulfric Brian Dumbledore', 1881, 'male')


class Pupil(HogwartsMember):
    """
    Creates a Hogwarts pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

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
        return cls('Hermione', 1979, 'female', 'Griffindor', 1991, pet=('Crookshanks', 'cat'))


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


if __name__ == '__main__':
    hagrid = HogwartsMember('Hagrid', 1952, 'male')
    dumby = HogwartsMember.dumbledore()

    harry = Pupil.harry()
    ron = Pupil.ron()
    hermione = Pupil.hermione()

    snape = Professor.snape()
    mcgonagall = Professor.mcgonagall()

    nick = Ghost('Nick quasi sans tête', 541, 'male', 589)

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
