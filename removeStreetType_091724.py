from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def removeStreetType(address, streetType, feature, parent):
    if streetType is None:
        return address
    else:
        splitAddress = address.rsplit(' ', 1)
        return splitAddress[0]