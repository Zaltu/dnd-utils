from pprint import pprint as pp
import json

structures = {}
currentStruct = ""

#base = ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__',
#        '__file__', '__cached__', "spells", "Spell", "create_spell", "base", "structures", "currentStruct"]
base = list(globals().keys())
base.extend(["spells", "Spell", "create_spell", "base"])

from spells import *
for key in globals().copy():
    if key in base:
        continue

    if key.startswith("spells_"):
        structures[key] = {}
        currentStruct = key
        continue

    descl = globals()[key].__doc__.replace("    ", "").split(".\n")
    ndescl = []
    for line in descl:
        if line.startswith("\n"):
            ndescl.append("\n"+line.replace("\n", ""))
        else:
            ndescl.append(line.replace("\n", ""))

    desc = ". \n".join(ndescl)
    structures[currentStruct][globals()[key].name.lower()] = {
        "name": globals()[key].name,
        "desc": desc,
        "level": globals()[key].level,
        "casting_time": globals()[key].casting_time,
        "casting_range": globals()[key].casting_range,
        "components": globals()[key].components,
        "materials": globals()[key].materials,
        "duration": globals()[key].duration,
        "ritual": globals()[key].ritual,
        "magic_school": globals()[key].magic_school,
        "classes": globals()[key].classes
    }

for letter in structures:
    with open("jspells/"+letter+".json", "w+") as wfile:
        wfile.write(json.dumps(structures[letter], indent=4, sort_keys=True))
