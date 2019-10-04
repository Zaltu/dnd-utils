"""
Various utilities (dice rolls, spell descriptions, character sheets, etc...) useful for playing D&D.
"""
import random

from character import Character

def xdy(sides, amount=1):
    """
    Simply return a list of X dice results of a Y-sided die.

    :param int sides: the number of sides on the die
    :param int amount: number of dice to throw, defaults to 1

    :returns: the results of the throws
    :rtype: list
    """
    return [random.randint(1, sides) for i in range(1, amount+1)]


def spelldesc(spellname, spellist=None):
    """
    Fetch and return a spell's description.

    :param str spellname: the name of the spell to describe
    :param str spellist: option spellist the spell can be found it for efficiency

    :returns: the spell's description
    :rtype: str
    """
    return (spellname, spellist)  # NYI


def get_character_stats(character, stat):
    if not isinstance(character, Character):
        character = Character(character)
    return getattr(char, stat)


def get_character_ability_mod(character, stat):
    if not isinstance(character, Character):
        character = Character(character)
    return getattr(char, stat+"_mod")


if __name__ == "__main__":
    char = Character(sheetlink="DriveTest", loadfull=True)
    print(char.NAME)
    print(char.STR_mod)
