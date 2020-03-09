class DoorConnector(Event):
    def __init__(self, mapToGo, posInNewMap):
        self.mapToGo = mapToGo
        self.posInNewMap = posInNewMap
    
    def act(self):
        map.initFromFile("./res/maps/map_"+self.mapToGo)
        perso.position = [self.posInNewMap[0], self.posInNewMap[1]]
