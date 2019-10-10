"""
Various utilities (dice rolls, spell descriptions, character sheets, etc...) useful for playing D&D.
"""
import os
import glob
import json
import random

from dnd.character import Character  #pylint: disable=no-name-in-module

_CHARACTER_FOLDER = os.path.abspath(os.path.join(__file__, "../", "chars/*"))
_SPELL_FOLDER = os.path.abspath(os.path.join(__file__, "../", "jspells/"))


def xdy(sides, amount=1):
    """
    Simply return a list of X dice results of a Y-sided die.

    :param int sides: the number of sides on the die
    :param int amount: number of dice to throw, defaults to 1

    :returns: the results of the throws
    :rtype: list
    """
    return [random.randint(1, sides) for i in range(1, amount+1)]


def get_spell_desc(spellname):
    """
    Fetch and return a spell's description.

    :param str spellname: the name of the spell to describe

    :returns: the spell's description
    :rtype: str
    """
    fletter = spellname[0].lower()
    path = os.path.join(_SPELL_FOLDER, "spells_"+fletter+".json")
    spell = None
    with open(path, "r") as spellf:
        spell = json.load(spellf).get(spellname.lower())
    return spell["desc"]


def get_character_data(charname, stat):
    """
    Get one of the character's stats.
    (in this context, "stat" can also refer to equipment, gold, spells, etc...)

    :param str charname: name of the character
    :param str stat: the stat to fetch

    :returns: the stat
    :rtype: basetype
    """
    charpath = os.path.abspath(os.path.join(_CHARACTER_FOLDER[:-1], charname.lower()+".json"))
    if charpath in glob.glob(_CHARACTER_FOLDER):
        char = Character(lfile=charpath)
    else:
        char = Character(sheetlink=charname)
        char.savelocal(charpath)
    return getattr(char, stat)


if __name__ == "__main__":
    #from pprint import pprint as pp
    #CHARA = Character(sheetlink="DriveTest", loadfull=True)
    #CHARA.savelocal("Claude")
    #CHARA = Character(lfile="chars/Claude.json")
    #pp(CHARA.spells)
    #pp(CHARA.gold)
    #pp(CHARA.NAME)
    #pp(CHARA.STR_mod)
    #pp(get_spell_desc("fireball"))
    #pp(get_character_data("Claude", "gold"))
    pass
