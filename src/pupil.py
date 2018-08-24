from settings import NOW

from hogwarts_member import HogwartsMember


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
