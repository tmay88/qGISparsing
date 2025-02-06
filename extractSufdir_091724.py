from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def extractSufdir(address, feature, parent):
    directionals = {
        ' S': 'S',
        ' N': 'N',
        ' E': 'E',
        ' W': 'W',
        ' SW': 'SW',
        ' NW': 'NW',
        ' SE': 'SE',
        ' NE': 'NE',
        ' S W': 'SW',
        ' S. W.': 'SW',
        ' N W': 'NW',
        ' N. W.': 'NW',
        ' S E': 'SE',
        ' S. E.': 'SE',
        ' N E': 'NE',
        ' N. E.': 'NE',
        ' SOUTH': 'S',
        ' NORTH': 'N',
        ' EAST': 'E',
        ' WEST': 'W'
    }
    for key, value in directionals.items():
        if address.endswith(key):
            return value
    return None