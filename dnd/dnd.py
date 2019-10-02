"""
Various utilities (dice rolls, spell descriptions, character sheets, etc...) useful for playing D&D.
"""
from pprint import pprint as pp
import json
import random

import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

#CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)



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
    pass


#gc = gspread.authorize(CREDENTIALS)

#wrksht = gc.open("DriveTest").sheet1

#lis = wrksht.col_values(1)

#pp(lis)
