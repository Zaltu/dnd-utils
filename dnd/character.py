"""
Holding module for all the constants required to access a specific character's data.
"""
#pylint: disable=multiple-statements,invalid-name
import os
import math
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
CREDFILE = os.path.abspath(os.path.join(__file__, "../", "auth", "credentials.json"))
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(CREDFILE, SCOPE)

_EQUIPMENT_INDEX = 36

class Character:
    """
    Represents a character sheet. Can be given either a file path ora URL to a google drive character sheet.

    :param str lfile: path to file that contains the character data
    :param str sheetlink: Technically the name of the sheet in gdrive, generally the character's name
    :param bool loadfull: whether the full character sheet should be loaded on object creation
    """
    basesheet = None
    spellsheet = None
    featsheet = None
    def __init__(self, lfile=None, sheetlink=None, loadfull=False):
        if sheetlink is not None:
            GC = gspread.authorize(CREDENTIALS)
            self.gc = GC.open(sheetlink)
            self.loadfull = loadfull
            if loadfull:
                self.sheets = {
                    "base": self.gc.sheet1.get_all_values(),
                    "magic": self.gc.get_worksheet(1).get_all_values(),
                    #"feats": self.gc.get_worksheet(2).get_all_values()
                }
        elif lfile is not None:
            try:
                with open(lfile, "r") as charfile:
                    self.sheets = json.load(charfile)
            except IOError:
                raise BadCharacterException("Cannot find file %s" % lfile)
            self.loadfull = True
        else:
            raise BadCharacterException(
                "Character location not provided.\nYou must provide a local file path or a google drive URL."
            )

    #pylint: disable=missing-docstring,missing-return-doc,missing-return-type-doc
    @property
    def NAME(self): return self._data_at(0, 0)
    @property
    def PLAYER(self): return self._data_at(0, 4)

    @property
    def RACE(self): return self._data_at(2, 4)
    @property
    def CLASS(self): return self._data_at(2, 0)
    @property
    def ALIGNMENT(self): return self._data_at(2, 5)
    @property
    def DEITY(self): return self._data_at(2, 6)

    @property
    def LEVEL(self): return self._data_at(2, 0)
    @property
    def HP(self): return self._data_at(7, 8)
    @property
    def AC(self): return self._data_at(11, 8)

    @property
    def STR(self): return self._data_at(9, 1)
    @property
    def STR_mod(self): return _get_ability_modifier(self.STR)
    @property
    def DEX(self): return self._data_at(10, 1)
    @property
    def DEX_mod(self): return _get_ability_modifier(self.DEX)
    @property
    def INT(self): return self._data_at(12, 1)
    @property
    def INT_mod(self): return _get_ability_modifier(self.INT)
    @property
    def CON(self): return self._data_at(11, 1)
    @property
    def CON_mod(self): return _get_ability_modifier(self.CON)
    @property
    def WIS(self): return self._data_at(13, 1)
    @property
    def WIS_mod(self): return _get_ability_modifier(self.WIS)
    @property
    def CHA(self): return self._data_at(14, 1)
    @property
    def CHA_mod(self): return _get_ability_modifier(self.CHA)
    #pylint: enable=missing-docstring,missing-return-doc,missing-return-type-doc

    @property
    def equipment(self):
        """
        All the equipment this character has.

        :returns: all equipment names
        :rtype: list
        """
        if not self.loadfull:
            self.sheets = {"base": self.gc.sheet1.get_all_values()}
        enames = []
        for eqrow in self.sheets["base"][_EQUIPMENT_INDEX:]:
            if eqrow[0] == "MONEY":
                break
            if eqrow[0]:
                enames.append(eqrow[0])
        return enames

    @property
    def weapons(self):
        pass

    @property
    def armor(self):
        pass

    @property
    def spells(self, level=None):
        """
        Fetch a formatted list of spells marked as known on the character sheet.

        :param int level: optionally return only the spells of a certain level

        :returns: spell breakdown
        :rtype: dict|list
        """
        breakdown = {}
        for block in self.sheets["magic"][2]:
            if block:
                breakdown[self.sheets["magic"][2].index(block)] = block.split("\n")
        for block in self.sheets["magic"][4]:
            if block:
                breakdown[self.sheets["magic"][4].index(block)+5] = block.split("\n")
        return breakdown.get(level) if level else breakdown

    @property
    def gold(self):
        """
        The character's gold, mapped by currency breakdown

        :returns: character's gold
        :rtype: dict
        """
        return {
            "PP": self.sheets["base"][64][1],
            "GP": self.sheets["base"][64][2],
            "SP": self.sheets["base"][64][3],
            "CP": self.sheets["base"][64][4]
        }

    def _data_at(self, row, column, sheet=0):
        """
        Get a singular point of data from the character source.

        :param int row: Sheet row
        :param int column: Sheet column
        :param int sheet: the index of the sheet the requested data is on

        :returns: value in sheet at row/col
        :rtype: str|int|float
        """
        if self.loadfull:
            return self.sheets[sheet][row][column]
        return self.gc.get_worksheet(sheet).cell(row, column).value

    def savelocal(self, path):
        """
        Write this character's information sheets to a local file.
        This will overwrite any existing file with the same name.
        This file can be used to recreate a character instance at another point.

        :param str path: path to write

        :raises BadCharacterException: if there is a problem writing the data to file
        """
        if not self.loadfull:
            raise BadCharacterException("Cannot save character unless fully loaded.")
        try:
            with open(path, "w+") as outfile:
                outfile.write(json.dumps(self.sheets, indent=4, sort_keys=True))
        except IOError:
            raise BadCharacterException("Could not create or overwrite file at %s" % path)


def _get_ability_modifier(ability):
    """
    Return the ability modifier for a given ability score.
    Ability modifiers are -5 at 0, and increment by 1 every 2 ability points.

    :param int ability: the full ability score

    :returns: ability modifier
    :rtype: int
    """
    return math.floor(int(ability)/2 - 5)


class BadCharacterException(Exception):
    """
    Character exception class
    """
