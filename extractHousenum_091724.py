from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def extractHouseNum(streetname, feature, parent):
    if streetname is None:
        return None

    splitadd = streetname.split(maxsplit=1)

    if splitadd[0].endswith(('ST', 'ND', 'RD', 'TH')):
        return None
    
    if len(splitadd) == 1:
        return None
    
    numList = []
    for value in splitadd[0]:
        if not value.isdigit():
            break
        numList.append(value)

    addnum = ''.join(numList)

    if addnum == '':
        return None
    else:
        return addnum.strip()[:10]
