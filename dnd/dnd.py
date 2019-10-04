"""
Various utilities (dice rolls, spell descriptions, character sheets, etc...) useful for playing D&D.
"""
import os
import glob
import random

from character import Character

_CHARACTER_FOLDER = "chars/*"  # TODO


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


def get_character_data(charname, stat):
    """
    Get one of the character's stats.
    (in this context, "stat" can also refer to equipment, gold, spells, etc...)

    :param str charname: name of the character
    :param str stat: the stat to fetch

    :returns: the stat
    :rtype: basetype
    """
    charpath = os.path.join(_CHARACTER_FOLDER, charname)
    if charpath in glob.glob(_CHARACTER_FOLDER):
        char = Character(lfile=charpath)
    else:
        char = Character(sheetlink=charname)
        char.savelocal(charpath)
    return getattr(char, stat)


if __name__ == "__main__":
    CHARA = Character(sheetlink="DriveTest", loadfull=True)
    print(CHARA.NAME)
    print(CHARA.STR_mod)
