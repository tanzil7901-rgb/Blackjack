import pygame, random

pygame.init()
window_width = 1000
window_height = 800
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Blackjack')

game_running = False
game_win = None
game_start_screen = True
fps = pygame.time.Clock()
card_width = 23 * 6.5
card_height = 34 * 6.5
font = pygame.font.Font(None,36)
big_font = pygame.font.Font(None, 72)

class Deck:
    def __init__(self):
        self.card_ranks = [11,2,3,4,5,6,7,8,9,10,10,10,10,
                           11,2,3,4,5,6,7,8,9,10,10,10,10,
                           11,2,3,4,5,6,7,8,9,10,10,10,10,
                           11,2,3,4,5,6,7,8,9,10,10,10,10]
        
        self.card_sprites = [pygame.image.load('Pixel art/Deck of Cards/H-A.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-2.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-3.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-4.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-5.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-6.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-7.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-8.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-9.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-10.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-J.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-Q.png'),
                             pygame.image.load('Pixel art/Deck of Cards/H-K.png'),

                             pygame.image.load('Pixel art/Deck of Cards/S-A.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-2.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-3.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-4.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-5.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-6.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-7.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-8.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-9.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-10.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-J.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-Q.png'),
                             pygame.image.load('Pixel art/Deck of Cards/S-K.png'),

                             pygame.image.load('Pixel art/Deck of Cards/D-A.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-2.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-3.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-4.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-5.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-6.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-7.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-8.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-9.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-10.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-J.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-Q.png'),
                             pygame.image.load('Pixel art/Deck of Cards/D-K.png'),

                             pygame.image.load('Pixel art/Deck of Cards/C-A.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-2.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-3.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-4.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-5.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-6.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-7.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-8.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-9.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-10.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-J.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-Q.png'),
                             pygame.image.load('Pixel art/Deck of Cards/C-K.png')]

    def draw_card(self):
        self.index = random.randint(0,len(self.card_ranks) - 1)
        self.card_rank = self.card_ranks.pop(self.index)
        self.card_png = self.card_sprites.pop(self.index)
        self.card_sprite = pygame.transform.scale(self.card_png,(card_width,card_height))
        return self.card_rank, self.card_sprite
    
class Opponent:
    def __init__(self):
        self.card, self.card_sprite = deck.draw_card()
        self.facedown_card = '?'
        face_card_png = pygame.image.load('Pixel art/Deck of Cards/Facedown and Deck.png')
        self.facedown_card_sprite = pygame.transform.scale(face_card_png,(card_width,card_height))
        self.hand_total = self.card
        self.new_card_sprites = []

class Player:
    def __init__(self):
        self.card_1, self.card_1_sprite = deck.draw_card()
        self.card_2, self.card_2_sprite = deck.draw_card()
        self.hand_total = self.card_1 + self.card_2
        if self.card_1 == 11 and self.hand_total > 21:
            self.card_1 = 1
            self.hand_total = self.card_1 + self.card_2
        elif self.card_2 == 11 and self.hand_total > 21:
            self.card_2 = 1
            self.hand_total = self.card_1 + self.card_2
        self.new_card_sprites = []

    def hit(self):
        global game_win
        self.new_card, self.new_card_sprite = deck.draw_card()
        if self.new_card == 11 and self.hand_total > 10:
            self.new_card = 1
        self.hand_total += self.new_card
        if self.hand_total > 21:
            game_win = False
        self.new_card_sprites.append(self.new_card_sprite)

    def stand(self):
        global game_win
        if player.hand_total > 21:
            return 
        opponent.facedown_card, opponent.facedown_card_sprite = deck.draw_card()
        opponent.hand_total += opponent.facedown_card
        while opponent.hand_total < 17:
            new_card, new_card_sprite = deck.draw_card()
            opponent.hand_total += new_card
            opponent.new_card_sprites.append(new_card_sprite)
        if self.hand_total > opponent.hand_total and not self.hand_total > 21:
            game_win = True
        elif self.hand_total < opponent.hand_total and not opponent.hand_total > 21:
            game_win = False
        elif opponent.hand_total > 21 and not self.hand_total > 21:
            game_win = True
        elif self.hand_total == opponent.hand_total:
            game_win = False
        elif opponent.hand_total and self.hand_total == 21:
            game_win = False

deck_png = pygame.image.load('Pixel art/Deck of Cards/Facedown and Deck.png')
deck_sprite = pygame.transform.scale(deck_png,(card_width,card_height))

deck = Deck()
player = Player()
opponent = Opponent()

while game_start_screen:
    window.fill((78,106,84))
    fps.tick(60)

    guide = font.render('Welcome to Blackjack!\nTo learn this game, check out:\nhttps://bicyclecards.com/how-to-play/blackjack', True, (255,255,255))
    window.blit(guide,(200,250))
    controls = font.render('Press "H" to hit or "S" to stand\nOnce ready, press "Enter" to start game', True, (255, 255, 255))
    window.blit(controls,(200,400))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            game_start_screen = False
            game_running = True
            break

    pygame.display.flip()

while game_running:
    game_start_screen = False
    window.fill((78,106,84))
    fps.tick(60)

    window.blit(deck_sprite,(800,270))
    player_total = font.render(f"Your hand total: {player.hand_total}", True, (255, 255, 255))
    window.blit(player_total, (30, 440))
    opponent_total = font.render(f"Opponent hand total: {opponent.hand_total}", True, (255, 255, 255))
    if game_win is None:
        opponent_total = font.render(f"Opponent hand total: ?", True, (255, 255, 255))
    else:
        opponent_total = font.render(f"Opponent hand total: {opponent.hand_total}", True, (255, 255, 255))
    window.blit(opponent_total,(30,280))
    window.blit(player.card_1_sprite,(30,500))
    window.blit(player.card_2_sprite,(185,500))
    window.blit(opponent.card_sprite,(30,30))
    window.blit(opponent.facedown_card_sprite,(185,30))
    for i, player_card_sprite in enumerate(player.new_card_sprites): 
        window.blit(player_card_sprite, (340 + i * 155, 500))
    for n, opponent_card_sprite in enumerate(opponent.new_card_sprites):
        window.blit(opponent_card_sprite,(340 + n * 155,30))
    
    text = font.render('To restart, press "Enter"', True, (255,255,255))
    if game_win == True:
        win_text = big_font.render("YOU WIN!", True, (0, 255, 0))
        window.blit(win_text, (340,340))
        window.blit(text,(340,390))
    elif game_win == False:
        lose_text = big_font.render("YOU LOSE!", True, (255, 0, 0))
        window.blit(lose_text,(340,340))
        window.blit(text,(340,390))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_h and game_win is None:
            player.hit()   
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and game_win is None:
            player.stand()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and game_win is not None:
            deck = Deck()
            player = Player()
            opponent = Opponent()
            game_win = None
        
    pygame.display.flip()   
pygame.quit()