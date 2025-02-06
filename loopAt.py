from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def loopat(entry, feature, parent):
    newEntry = []
    for x in entry:
        if x != '&':
            newEntry.append(x)
        else:
            break            
    return ''.join(newEntry).strip()
