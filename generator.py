import random

from Projects.randommissilegenerator.missile_types.facet_bomb import FacetBomb
from Projects.randommissilegenerator.missile_types.thermo_nuclear import ThermoNuclear
from Projects.randommissilegenerator.missile_types.tnt_bomb import TNTBomb


def generate_random_missile():
    serial_number = random.randint(10000, 100000)
    missile_type = random.choice(["Thermonuclear", "FacetBomb", "TNTBomb"])
    if missile_type == "Thermonuclear":
        return ThermoNuclear(serial_number)
    elif missile_type == "FacetBomb":
        return FacetBomb(serial_number)
    else:
        return TNTBomb(serial_number)