class YvesPoilane(Entity):
    def __init__(self):
        self.prenom = "Yves"
        self.nom = "Poilane"
        self.tile = pygame.image.load("./res/entities/yves_poilane.png").convert_alpha()
    
    def getImage(self):
        return self.tile
    
    def runScenario(self):
        # dia = Dialogue("Coucou je suis Yves Poilane et je mange des frites avec de la pizza, et le coronavirus", self.tile)
        # dia.show()
        menu = Menu("Tu veux quoi ?", ["D'la weed", "Des credits stage", "Des credits FH"])
        menu.show()