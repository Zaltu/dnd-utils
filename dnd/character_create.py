"""
Tool for generating a new character based on some kind of simplified user input.
"""
import os
# dungeonsheets.character.Character
from dungeonsheets import Character
from dungeonsheets.exceptions import LatexError

FILE_EXTENTION_PDF = ".pdf"
FILE_EXTENTION_FDF = ".fdf"
PARAMS = {
    "name",
    "player_name",
    "alignment",
    "class",
    "subclass",
    "level",
    "race",
    "background",
    "hp_max",
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
    "inspiration",
    "skill_proficiencies",
    "skill_expertise",
    "languages",
    "attacks_and_spellcasting"
    "personality_traits",
    "ideals",
    "bonds",
    "flaws",
    "features_and_traits",
    "cp",
    "sp",
    "ep",
    "gp",
    "pp",
    "equipment",
    "weapons",
    "magic_items",
    "armor",
    "shield",
    "spells_prepared",
    "__spells_unprepared",
    "wild_shapes"
}
REQUIRED_PARAMS = {
    "name",
    "player_name",
    "alignment",
    "race",
    "class",
    "level",
    "hp_max",
    "strength",
    "dexterity",
    "intelligence",
    "constitution",
    "wisdom",
    "charisma"
}

def create_character_sheet(path, logger, **kwargs):
    """
    From various inputs, generate a D&D character sheet that could be used elswhere.

    :param str path: path to the dir to generate the character sheets in
    :param logging.logger logger: logger
    :param kwargs: args to generate the character. See file docstring for more details.

    :raises FileNotFoundError: if the given path is invalid
    :raises AttributeError: if there are invalid or missing arguments
    :raises RuntimeError: if pdflatex is having issues
    :returns: list of paths to the files generated, [0]=pdf, [1]=fdf
    :rtype: list
    """
    # Ensure given path is valid
    if not os.path.exists(path) and os.path.isdir(path):
        raise FileNotFoundError(f"Invalid path {path}")
    # Ensure there are no invalid args
    for key, _ in kwargs.items():
        if key not in PARAMS:
            raise AttributeError(f"{key} is not a valid character attribute.\n{PARAMS}")
    # Ensure requires args are present
    for key in REQUIRED_PARAMS:
        if key not in kwargs:
            raise AttributeError(f"{key} was not provided and is required for creation.")

    # Handle spell curfudlery if necessary
    kwargs["spells"] = kwargs.get("spells_prepared", []) + kwargs.get("__spells_unprepared", [])

    # Generate character sheet
    char = Character(**kwargs)
    path = os.path.join(path, char.name)
    logger.info(f"Generating sheet for {kwargs['race']} {kwargs['class']} {kwargs['name']}")
    try:
        char.to_pdf(path, **{"flatten": False})
    except LatexError:
        raise RuntimeError("Unable to process LaTeX properly. Check system requirements.")
    # Return file paths, kind of ugly-ly
    return [path+FILE_EXTENTION_PDF, path+FILE_EXTENTION_FDF]
