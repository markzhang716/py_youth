class Map:
    name = 'Map'
    def __init__(self):
        self.weight = 10

class ChinaMap(Map):
    def __init__(self):
        Map.__init__(self)
        self.weight += 2
cm = ChinaMap()
print(cm.name)
print(cm.weight)
