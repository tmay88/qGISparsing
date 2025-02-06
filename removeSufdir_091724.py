from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def removeSufdir(streetname, sufdir, feature, parent):
    if sufdir is None:
        return streetname
    
    address = " ".join(streetname.split()[:-1])
    return address
