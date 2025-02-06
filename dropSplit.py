from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def dropSplit(entry, feature, parent):
    splitEntry = entry.split()
    concat = ' '.join(splitEntry[:-1])
    return concat.strip()
