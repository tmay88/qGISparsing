from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def drop(entry, feature, parent):
    return entry[:-2]
