def blit_text(screen, text, pos, max_width, font, affichage = True, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    x, y = pos
    text_width = 0
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            if affichage : screen.blit(word_surface, (x, y))
            x += word_width + space
        if x - pos[0] > text_width :
            text_width = x - pos[0]
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
        
    text_height = y - pos[1]
    return text_width, text_height

def visual_refresh():
    global map, perso, window_dimensions
    map.refresh(perso.getPosition(), window_dimensions)
    perso.afficher(window_dimensions)
    pygame.display.flip()