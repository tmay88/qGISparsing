from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def replace(entry, feature, parent):
    return entry.replace('12ND', '12TH')
