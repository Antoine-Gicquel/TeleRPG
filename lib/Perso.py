class Perso(object):
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.creditsFH = 0
        self.position = [0, 0, 0] # en tiles
        self.tile = pygame.image.load('./res/skin/perso.png').convert_alpha()
        xPerso = math.floor((fenetre.get_width()/2 - self.tile.get_rect()[0]/2)/40)*40
        yPerso = math.floor((fenetre.get_height()/2 - self.tile.get_rect()[1]/2)/40)*40
        self.hitbox = pygame.Rect((xPerso + 1, yPerso + 1), (38, 38))
                
    def afficher(self):
        xPerso = math.floor((fenetre.get_width()/2 - self.tile.get_rect()[0]/2)/40)*40
        yPerso = math.floor((fenetre.get_height()/2 - self.tile.get_rect()[1]/2)/40)*40
        self.hitbox = pygame.Rect((xPerso + 1, yPerso + 1), (38, 38))
        fenetre.blit(self.tile, (xPerso, yPerso))
    
    def move(self, dx, dy, dz = 0):
        self.position[0] += dx
        self.position[1] += dy
        self.position[2] += dz
    
    def getPosition(self):
        return self.position