class Menu(object):
    def __init__(self, text, choices):
        self.choices = choices[:]
        for i in range(len(self.choices)):
            self.choices[i] = "    "+self.choices[i] # on ajoute une tabulation a chaque choix
        self.text = text
    
    def show(self):
        """ Retourne l'indice du choix """
        global fenetre, window_dimensions
        margin = 10
        font = pygame.font.Font("./res/fonts/verdana.ttf", 30)
        menu_height = 0
        menu_width = 0
        
        # taille du titre du menu
        titre_width, titre_height = blit_text(fenetre, self.text, (0, 0), window_dimensions[0] - 2*margin, font, False)
        menu_height += int(titre_height*1.2)
        menu_width = titre_width
        
        listChoicesHeight = []
        font.set_bold(True)
        for l in self.choices:
            listChoicesHeight.append(menu_height)
            choice_width, choice_height = blit_text(fenetre, l, (menu_height, 0), window_dimensions[0] - 2*margin, font, False)
            menu_height += choice_height
            menu_width = max(menu_width, choice_width)
        font.set_bold(False)
        yBottom = menu_height + 2*margin
    
        finalChoice = None
        currentChoice = 0
        
        while finalChoice == None:
            pygame.draw.rect(fenetre, (100,0,100) , (margin, margin, 2*margin + menu_width, 2*margin + menu_height)) # on met le background du menu
            # on met le titre du menu
            blit_text(fenetre, self.text, (2*margin, 2*margin), window_dimensions[0] - 2*margin, font, True, pygame.Color("white"))
            for i in range(len(self.choices)):
                if currentChoice == i:
                    font.set_bold(True)
                blit_text(fenetre, self.choices[i], (2*margin, listChoicesHeight[i] + 2*margin), window_dimensions[0] - 2*margin, font, True, pygame.Color("white"))
                if currentChoice == i:
                    font.set_bold(False)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                    finalChoice = -1
                    needRefresh = True
                    break
                if event.type == VIDEORESIZE:
                    window_dimensions = [event.w, event.h]
                    fenetre = pygame.display.set_mode((event.w, event.h),
                                                    pygame.RESIZABLE)
                    needRefresh = True
                    
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        currentChoice = max(currentChoice - 1, 0)
                    if event.key == K_DOWN:
                        currentChoice = min(currentChoice + 1, len(self.choices) - 1)
                    if event.key == K_RETURN:
                        finalChoice = currentChoice
                    if event.key == K_ESCAPE:
                        finalChoice = -1
        
        visual_refresh()
        return finalChoice