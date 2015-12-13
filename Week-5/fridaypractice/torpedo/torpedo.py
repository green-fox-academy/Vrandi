from torpedofield import *
from ships import *

ocean = [
    [1,1,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,1]
]

def grouping_fields(ocean):
    empty_fields = []
    shipfields = []
    for i, row in enumerate(ocean):
        for index, field in enumerate(row):
            if field == 1:
                s = Shipfield((index, i))
                shipfields.append(s)
            else:
                f = Field((index, i))
                empty_fields.append(f)
    print([x.index for x in empty_fields])
    print([x.index for x in shipfields])


grouping_fields(ocean)
