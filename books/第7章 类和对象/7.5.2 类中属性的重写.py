class Map:
    name = 'Map2'
    def __init__(self):
        self.weight = 20

class ChinaMap(Map):
    name = 'China Map'

cm = ChinaMap()
print(cm.name,cm.weight)
