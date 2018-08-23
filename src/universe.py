class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardry
    """

    location = 'England'

    def __init__(self, name, birthyear, sex):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words):
        return f'{self._name} says "{words}"'


class Pupil(HogwartsMember):
    """
    Creates a Hogwarts pupil
    """

    def __init__(self, name, birthyear, sex, house, start_year, pet=None):
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


class Professor(HogwartsMember):
    """
    Creates a Hogwarts professor
    """

    def __init__(self, name, birthyear, sex, subject, house=None):
        super().__init__(name, birthyear, sex)
        self.subject = subject

        if house is not None:
            self.house = house


class Ghost(HogwartsMember):
    """
    Creates a Hogwarts ghost
    """

    def __init__(self, name, birthyear, sex, year_of_death, house=None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house


if __name__ == '__main__':
    hagrid = HogwartsMember('Hagrid', '1952', 'male')

    harry = Pupil(
        name='Harry',
        birthyear='1980',
        sex='male',
        house='Griffindor',
        start_year='1991',
        pet=('Hedwig', 'owl')
    )

    print(hagrid.says("Hello Harry !"))
    print(harry.says("Hello giant one !"))
    print('='*30)
