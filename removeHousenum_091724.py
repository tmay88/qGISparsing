from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def removeHouseNumber(streetname, housenum, feature, parent):
    if housenum is None:
        return streetname
    
    splitadd = streetname.split(maxsplit=1)
    if len(splitadd) == 1:
        return streetname
    
    return splitadd[1]
