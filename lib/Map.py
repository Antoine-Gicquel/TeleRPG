class Map(object):
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.tilesDict = {"H" : pygame.image.load("./res/tiles/herbe.jpg").convert(), "B" : pygame.image.load("./res/tiles/beton.jpg").convert(), "E" : pygame.image.load("./res/tiles/escalier.jpg").convert(), " " : None}
        self.tilesDict[" "] = self.tilesDict["B"]
        self.tiles = []
    
    def initFromFile(self, filename):
        f = open(filename, "r")
        self.tiles = [] # tiles[y][x]
        lines = f.readlines()
        for l in lines:
            if len(l)>2:
                self.tiles.append([])
                for c in l:
                    if c != '\n':
                        self.tiles[-1].append(c)
    
    def refresh(self, posPerso):
        nbTilesX = math.floor(self.fenetre.get_width()/40)+2
        nbTilesY = math.floor(self.fenetre.get_height()/40)+2
        
        xDebut = posPerso[0] - nbTilesX // 2 + 1
        xFin = xDebut + nbTilesX
        yDebut = posPerso[1] - nbTilesY // 2 + 1
        yFin = yDebut + nbTilesY
        
        for j in range(xDebut, xFin):
            for i in range(yDebut, yFin):
                if (i>=0 and j>=0 and i<len(self.tiles) and j<len(self.tiles[0])):
                    fenetre.blit(self.tilesDict[self.tiles[i][j]], ((j-xDebut)*40, (i-yDebut)*40))
                else:
                    fenetre.blit(self.tilesDict["B"], ((j-xDebut)*40, (i-yDebut)*40))
    
    def canWalk(self, x, y):
        if (x < 0 or y < 0 or x>= len(self.tiles[0]) or y >= len(self.tiles)):
            return False
        if self.tiles[y][x] != "B":
            return True
        return False