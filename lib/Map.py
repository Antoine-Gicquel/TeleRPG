def gotoMap(connector):
    map.initFromFile("./res/maps/map_"+connector.mapToGo)
    perso.position = [connector.posInNewMap[0], connector.posInNewMap[1]]


class Map(object):
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.tilesDict = dict()
        tilesNames = ["herbe", "beton", "eau", "escalier", "orange", "porte", "telesol", "void"]
        for tileName in tilesNames:
            self.addTile(tileName)

        self.tiles = []
        self.tilesdata = []

    def addTile(self, tileName):
        self.tilesDict[tileName] = pygame.image.load("./res/tiles/"+tileName+".jpg").convert()

    def initFromFile(self, filename):
        f = open(filename, "r")
        self.tiles = [] # tiles[y][x]
        self.tilesdata = []
        lines = f.readlines()
        for l in lines:
            if len(l)>2:
                self.tiles.append([])
                self.tilesdata.append([])
                l = l.split(" ")
                for c in l:
                    if '\n' in c:
                        c = c.split('\n')[0]
                    c = c.split(",")
                    self.tiles[-1].append(c[0])
                    if len(c) == 1:
                        self.tilesdata[-1].append(None)
                    elif len(c) > 1:
                        self.tilesdata[-1].append(DoorConnector(c[1], (int(c[2]), int(c[3]))))

    def refresh(self, posPerso, windowDim):
        surf = pygame.display.get_surface()
        nbTilesX = math.floor(windowDim[0]/40)+2
        nbTilesY = math.floor(windowDim[1]/40)+2

        xDebut = posPerso[0] - nbTilesX // 2 + 1
        xFin = xDebut + nbTilesX
        yDebut = posPerso[1] - nbTilesY // 2 + 1
        yFin = yDebut + nbTilesY

        for j in range(xDebut, xFin):
            for i in range(yDebut, yFin):
                if (i>=0 and j>=0 and i<len(self.tiles) and j<len(self.tiles[0])):
                    self.fenetre.blit(self.tilesDict[self.tiles[i][j]], ((j-xDebut)*40, (i-yDebut)*40))
                else:
                    self.fenetre.blit(self.tilesDict["void"], ((j-xDebut)*40, (i-yDebut)*40))

    def canWalk(self, x, y):
        if (x < 0 or y < 0 or x>= len(self.tiles[0]) or y >= len(self.tiles)):
            return False
        if self.tiles[y][x] not in ["beton", "orange"]:
            return True
        return False

    def checkAction(self, playerPos):
        if self.tilesdata[playerPos[1]][playerPos[0]] != None:
            return True

    def getAction(self, playerPos):
        c = self.tilesdata[playerPos[1]][playerPos[0]]
        return gotoMap, c
