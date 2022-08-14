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

white = []
black = []

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


white = [white_pawn_img, white_rook_img, white_knight_img, white_bishop_img, white_queen_img, white_king_img]
black = [black_pawn_img, black_rook_img, black_knight_img, black_bishop_img, black_queen_img, black_king_img]

for img in white:
    pygame.transform.scale(img, (block_width*1/2, block_height*3/4))
for img in black:
    pygame.transform.scale(img, (block_width*1/2, block_height*3/4))


#blit images
win.blit(board_img, (0,0))
win.blit(white_pawn_img, (150,150))



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