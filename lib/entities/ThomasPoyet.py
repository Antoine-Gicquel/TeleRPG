class ThomasPoyet(Entity):
    def __init__(self):
        self.prenom = "Yves"
        self.nom = "Poilane"
        self.tile = pygame.image.load("./res/entities/thomas_poyet.png").convert_alpha()
    
    def getImage(self):
        return self.tile
    
    def runScenario(self):
        Dialogue("Salut, je suis Thomas et je mange des chips",self.tile).show()
        