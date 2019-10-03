"""
Holding module for all the constants required to access a specific character's data.
"""
#pylint: disable=multiple-statements,invalid-name
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
GC = gspread.authorize(CREDENTIALS)

_EQUIPMENT_INDEX = 36

class Character:
    """
    Represents a character sheet

    :param str sheetlink: Technically the name of the sheet in gdrive, generally the character's name
    :param bool loadfull: whether the full character sheet should be loaded on object creation
    """
    basesheet = None
    spellsheet = None
    featsheet = None
    def __init__(self, sheetlink, loadfull=False):
        self.gc = GC.open(sheetlink)
        self.loadfull = loadfull
        if loadfull:
            self.sheets = [
                self.gc.sheet1.get_all_values(),
                #self.gc.get_worksheet(1).get_all_values(),
                #self.gc.get_worksheet(2).get_all_values()
            ]

    #pylint: disable=missing-docstring,missing-return-doc,missing-return-type-doc
    @property
    def NAME(self): return self._data_at(1, 1)
    @property
    def PLAYER(self): return self._data_at(1, 5)

    @property
    def RACE(self): return self._data_at(3, 5)
    @property
    def CLASS(self): return self._data_at(3, 1)
    @property
    def ALIGNMENT(self): return self._data_at(3, 6)
    @property
    def DEITY(self): return self._data_at(3, 7)

    @property
    def LEVEL(self): return self._data_at(3, 1)
    @property
    def HP(self): return self._data_at(8, 9)
    @property
    def AC(self): return self._data_at(12, 9)

    @property
    def STR(self): return self._data_at(10, 2)
    @property
    def DEX(self): return self._data_at(11, 2)
    @property
    def INT(self): return self._data_at(13, 2)
    @property
    def CON(self): return self._data_at(12, 2)
    @property
    def WIS(self): return self._data_at(14, 2)
    @property
    def CHA(self): return self._data_at(15, 2)
    #pylint: enable=missing-docstring,missing-return-doc,missing-return-type-doc

    @property
    def equipment(self):
        """
        All the equipment this character has.

        :returns: all equipment names
        :rtype: list
        """
        if not self.loadfull:
            self.sheets = [self.gc.sheet1.get_all_values()]
        enames = []
        for eqrow in self.sheets[0][_EQUIPMENT_INDEX:]:
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
    def spells(self):
        pass

    @property
    def gold(self):
        """
        The character's gold, mapped by currency breakdown

        :returns: character's gold
        :rtype: dict
        """
        ps = self.data.sheet1.range("B65:E65")
        return {
            "PP": ps[0].value,
            "GP": ps[1].value,
            "SP": ps[2].value,
            "CP": ps[3].value,
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
