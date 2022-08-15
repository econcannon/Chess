import pygame
pygame.init()


screen_height = 600
screen_width= 600
block_height = screen_height/8
block_width = screen_height/8

win = pygame.display.set_mode((screen_height,screen_width))
pygame.display.set_caption('Chess')


#load images
board_img = pygame.image.load('mvc\\Model\\Imgs\\chess_board_img.png').convert()
board_img = pygame.transform.scale(board_img,(screen_width, screen_height))

#black pieces
black_pawn_img = pygame.image.load('mvc\\Model\\Imgs\\black_pawn.png').convert()
black_rook_img = pygame.image.load('mvc\\Model\\Imgs\\black_rook.png').convert()
black_knight_img = pygame.image.load('mvc\\Model\\Imgs\\black_knight.png').convert()
black_bishop_img = pygame.image.load('mvc\\Model\\Imgs\\black_bishop.png').convert()
black_queen_img = pygame.image.load('mvc\\Model\\Imgs\\black_queen.png').convert()
black_king_img = pygame.image.load('mvc\\Model\\Imgs\\black_king.png').convert()

#white pieces
white_pawn_img = pygame.image.load('mvc\\Model\\Imgs\\white_pawn.png').convert()
white_rook_img = pygame.image.load('mvc\\Model\\Imgs\\white_rook.png').convert()
white_knight_img = pygame.image.load('mvc\\Model\\Imgs\\white_knight.png').convert()
white_bishop_img = pygame.image.load('mvc\\Model\\Imgs\\white_bishop.png').convert()
white_queen_img = pygame.image.load('mvc\\Model\\Imgs\\white_queen.png').convert()
white_king_img = pygame.image.load('mvc\\Model\\Imgs\\white_king.png').convert()

#white piece scale
white_pawn_img = pygame.transform.scale(white_pawn_img, (100, 100))
white_rook_img = pygame.transform.scale(white_rook_img, (100, 100))
white_knight_img = pygame.transform.scale(white_knight_img, (100, 100))
white_bishop_img = pygame.transform.scale(white_bishop_img, (100, 100))
white_queen_img = pygame.transform.scale(white_queen_img, (100, 100))
white_king_img = pygame.transform.scale(white_king_img, (100, 100))

#black piece scale
black_pawn_img = pygame.transform.scale(black_pawn_img, (100, 100))
black_rook_img = pygame.transform.scale(black_rook_img, (100, 100))
black_knight_img = pygame.transform.scale(black_knight_img, (100, 100))
black_bishop_img = pygame.transform.scale(black_bishop_img, (100, 100))
black_queen_img = pygame.transform.scale(black_queen_img, (100, 100))
black_king_img = pygame.transform.scale(black_king_img, (100, 100))


#blit images
win.blit(board_img, (0,0))
win.blit(white_pawn_img, (0,0))
win.blit(white_bishop_img, (100,100))


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass

    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


pygame.quit()