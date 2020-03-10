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
        choix = menu.show()
        if choix == 0:
            Dialogue("Bien vu poto, j'ai de la bonne",self.tile).show()
        if choix == 1:
            Dialogue("Va voir Davidovici",self.tile).show()
        if choix == 2:
            Dialogue("Lol c'est parti pour faire du théâtre",self.tile).show()