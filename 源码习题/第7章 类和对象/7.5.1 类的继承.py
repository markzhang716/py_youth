class Map:
    name = '地图'
    def __init__(self):
        self.weight = 20

class ChinaMap(Map):
    pass
cm = ChinaMap()
print(cm.name,cm.weight)
