class Dialogue(object):
    def __init__(self, text, sprite):
        self.text = text
        self.sprite = sprite
    
    def show(self):
        global fenetre, window_dimensions
        margin = 10
        scaleFactor = 4
        font = pygame.font.Font("./res/fonts/verdana.ttf", 30)
        text_height = blit_text(fenetre, self.text, (2*margin, 0), window_dimensions[0] - 2*margin, font, False)
        yTop = window_dimensions[1] - margin - text_height
        pygame.draw.rect(fenetre, (100,0,100) , (margin, yTop, window_dimensions[0] - 2*margin, window_dimensions[1] - yTop - margin)) # on met le background du dialogue
        
        fenetre.blit(pygame.transform.scale(self.sprite, (scaleFactor*40,scaleFactor*40)), (margin, yTop - scaleFactor * 40))# on met l'image du perso qui parle
        # fenetre.blit(self.sprite, (margin, yTop -))# on met l'image du perso qui parle
        blit_text(fenetre, self.text, (2*margin, yTop), window_dimensions[0] - 2*margin, font, True, pygame.Color("white"))
        pygame.display.flip()