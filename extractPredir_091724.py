from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def extractPredir(address, feature, parent):
    directionals = {
        'S W ': 'SW',
        'S. W. ': 'SW',
        'N W ': 'NW',
        'N. W. ': 'NW',
        'S E ': 'SE',
        'S. E. ': 'SE',
        'N E ': 'NE',
        'N. E. ': 'NE',
        'NORTHWEST ': 'NW',
        'NORTHEAST ': 'NE',
        'SOUTHWEST ': 'SW',
        'SOUTHEAST ': 'SE',
        'NORTH WEST ': 'NW',
        'NORTH EAST ': 'NE',
        'SOUTH WEST ': 'SW',
        'SOUTH EAST ': 'SE',
        'S ': 'S',
        'S. ': 'S',
        'N ': 'N',
        'N. ': 'N',
        'E ': 'E',
        'E. ': 'E',
        'W ': 'W',
        'W. ': 'W',
        'SW ': 'SW',
        'NW ': 'NW',
        'SE ': 'SE',
        'NE ': 'NE',
        'SOUTH ': 'S',
        'NORTH ': 'N',
        'EAST ': 'E',
        'WEST ': 'W'
    }
    
    for key, value in directionals.items():
        if address.startswith(key):
            return value
    return None
