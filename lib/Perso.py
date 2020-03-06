class Perso(object):
    def __init__(self, fenetre):
        self.fenetre = fenetre
        surf = pygame.display.get_surface()
        self.creditsFH = 0
        self.position = [0, 0] # en tiles
        self.tile = pygame.image.load('./res/skin/perso.png').convert_alpha()
        xPerso = math.floor((surf.get_width()/2 - self.tile.get_rect()[0]/2)/40)*40
        yPerso = math.floor((surf.get_height()/2 - self.tile.get_rect()[1]/2)/40)*40
        self.hitbox = pygame.Rect((xPerso + 1, yPerso + 1), (38, 38))
                
    def afficher(self, windowDim):
        xPerso = math.floor((windowDim[0]/2 - self.tile.get_rect()[0]/2)/40)*40
        yPerso = math.floor((windowDim[1]/2 - self.tile.get_rect()[1]/2)/40)*40
        self.hitbox = pygame.Rect((xPerso + 1, yPerso + 1), (38, 38))
        self.fenetre.blit(self.tile, (xPerso, yPerso))
    
    def move(self, dx, dy):
        self.position[0] += dx
        self.position[1] += dy
    
    def getPosition(self):
        return self.position