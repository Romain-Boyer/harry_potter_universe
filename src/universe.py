from deatheater import DeathEater
from ghost import Ghost
from hogwarts_member import HogwartsMember
from house import House
from professor import Professor
from pupil import Pupil
from spell import (Spell, Charm, Transfiguration, Jinx, Hex, Curse, CounterSpell, HealingSpell)

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
    bloody_baron = Ghost("Bloody Baron's", 1409, 'male', 1468, 'Slytherin')

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

    gryffindor = House('Griffyndor', ['bravery', 'nerve', 'courage'], mcgonagall, nick)
    slytherin = House('Slytherin', ['cunning', 'ambition', 'determination'], snape, bloody_baron)

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
    print('=' * 30)

    print('Days 16 - 18\n')
    print(f'New house : {gryffindor.name}')
