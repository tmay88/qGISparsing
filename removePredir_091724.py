from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def removePredir(streetname, predir, feature, parent):
    if predir is None:
        return streetname
    
    splitStreetname = streetname.split(maxsplit=1)
    if len(splitStreetname) == 1:
        return streetname
    
    return splitStreetname[1]