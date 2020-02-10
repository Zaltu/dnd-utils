"""
D&D constants. SLightly adjusted to our game though.
"""
from dnd.utils import get_spell_desc, get_character_data
#pylint: disable=line-too-long
__all__ = ["CLASSES", "SUBCLASSES", "RACES", "SKILLS", "ALIGNMENTS", "BACKGROUNDS", "IDEALS", "BONDS", "FLAWS", "LANGUAGES", "WEAPONS", "EQUIPEMENT", "ARMOR", "SHIELD",
           "get_spell_desc", "get_character_data"]
CLASSES = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorceror",
    "Warlock",
    "Wizard"
]
SUBCLASSES = {
    "Barbarian": ["BerzerkerPath", "TotemWarriorPath", "AncestralGuardianPath", "StormHeraldPath", "ZealotPath"],
    "Bard": ["CollegeOfLore", "CollegeOfValor", "CollegeOfGlamour", "CollegeOfSwords", "CollegeOfWhispers"],
    "Cleric": ["KnowledgeDomain", "LifeDomain", "LightDomain", "NatureDomain", "TempestDomain", "TrickeryDomain", "WarDomain", "ForgeDomain", "GraveDomain"],
    "Druid": ["LandCircle", "MoonCircle", "DreamsCircle", "ShepardCircle"],
    "Fighter": ["Champion", "BattleMaster", "EldritchKnight", "ArcaneArcher", "Cavalier", "Samurai"],
    "Monk": ["OpenHandWay", "ShadowWay", "FourElementsWay", "DrunkenMasterWay", "KenseiWay"],
    "Paladin": ["OathOfDevotion", "OathOfAncients", "OathOfVengance", "OathOfCrown", "OathOfConquest", "OathOfRedemption"],
    "Ranger": ["Hunter", "BeastMaster", "Gloomstalker", "HorizonWalker", "MonsterSlayer"],
    "Rogue": ["Thief", "Assassin", "ArcaneTrickster", "Inquisitive", "Mastermind", "Scout", "Swashbuckler"],
    "Sorceror": ["DraconicBloodline", "WildMagic", "DivineSoul", "ShadowMagic", "StormSorcery"],
    "Warlock": ["Archfey", "Fiend", "GreatOldOne", "Celestial", "Hexblade"],
    "Wizard": ["Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion", "Necromancy", "Transmutation", "WarMagic"]
}
RACES = [
    "HillDwarf",
    "MountainDwarf",
    "HighElf",
    "WoodElf",
    "DarkElf",
    "LightfootHalfling",
    "StoutHalfling",
    "Human",
    "Dragonborn",
    "ForestGnome",
    "RockGnome",
    "DeepGnome",
    "HalfElf",
    "HalfOrc",
    "Tiefling",
]
SKILLS = [
    "Acrobatics",
    "Animal_Handling",
    "Arcana",
    "Athletics",
    "Deception",
    "History",
    "Insight",
    "Intimidation",
    "Investigation",
    "Medicine",
    "Nature",
    "Perception",
    "Performance",
    "Persuasion",
    "Religion",
    "Sleight_Of_Hand",
    "Stealth",
    "Survival"
]
ALIGNMENTS = [
    "Lawful Good",
    "Lawful Neutral",
    "Lawful Evil",
    "Neutral Good",
    "True Neutral",
    "Neutral Evil",
    "Chaotic Good",
    "Chaotic Neutral",
    "Chaotic Evil"
]
BACKGROUNDS = [
    "Acolyte",
    "Charlatan",
    "Criminal",
    "Spy",
    "Entertainer",
    "Gladiator",
    "FolkHero",
    "GuildArtisan",
    "GuildMerchant",
    "Hermit",
    "Noble",
    "Knight",
    "Outlander",
    "Sage",
    "Sailor",
    "Pirate",
    "Soldier",
    "Urchin"
    "CityWatch",
    "ClanCrafter",
    "CloisteredScholar",
    "Courtier",
    "FactionAgent",
    "FarTraveler",
    "Inheritor",
    "KnightOfTheOrder",
    "MercenaryVeteran",
    "UrbanBountyHunter"
]
# TODO
IDEALS = [

]
# TODO
BONDS = [

]
# TODO
FLAWS = [

]
LANGUAGES = [
    "Common",
    "Undercommon",
    "Dwarvish",
    "Elvish",
    "Orcish",
    "Gnomish",
    "Giant",
    "Draconian",
    "Infernal",
    "Salassani"
]
WEAPONS = [
    "Club",
    "Dagger",
    "GreatClub",
    "Handaxe",
    "Javelin",
    "LightHammer",
    "Mace",
    "Quarterstaff",
    "Sickle",
    "Spear",
    "LightCrossbow",
    "Dart",
    "Shortbow",
    "Sling",
    "Battleaxe",
    "Flail",
    "Glaive",
    "Greataxe",
    "Greatsword",
    "Halberd",
    "Lance",
    "Longsword",
    "Mail",
    "Morningstar",
    "Pike",
    "Rapier",
    "Scimitar",
    "Shortsword",
    "ThrowingHamer",
    "Trident",
    "Warpick",
    "Warhammer",
    "Whip",
    "Blowgun",
    "HandCrossbow",
    "HeavyCrossbow",
    "Longbow",
    "Net"
]
EQUIPEMENT = [

]
ARMOR = [
    "PaddedArmor",
    "LeatherArmor",
    "StuddedLeatherArmor",
    "HideArmor",
    "ChainShirt",
    "ScaleMail",
    "Breastplate",
    "HalfPlate",
    "RingMail",
    "ChainMail",
    "SplintArmor",
    "PlateMail"
]
SHIELD = [
    "WoodenShild",
    "NoShield"
]
