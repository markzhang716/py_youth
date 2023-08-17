class Map:
    name = 'Map'
    def __init__(self):
        self.weight = 10
    def getCenter(self=None):
        return(0,0)

class ChinaMap(Map):
    def getCenter(self):
        return(32.1234,112.6789)
cm = ChinaMap()
print(cm.name,cm.weight,cm.getCenter(),Map.getCenter())
