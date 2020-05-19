import pygame
import random
pygame.init()

win = pygame.display.set_mode((800,600))
win.fill((255,255,255))
hanging_stick = pygame.image.load('hanging_stick.gif')
head = pygame.image.load('head.png')
neck = pygame.image.load('neck.png')
arm1 = pygame.image.load('arm1.png')
arm2 = pygame.image.load('arm2.png')
leg1 = pygame.image.load('leg1.png')
leg2 = pygame.image.load('leg2.png')

## Variables
word_list = ('life', 'love', 'ring', 'wolf', 'fish', 'king', 'tree', 'star', 'city', 'duck', 'rain', 'safe', 'pain')
chosen_word = random.choice(word_list)
print(chosen_word)
U1 = False
U2 = False
U3 = False
U4 = False
game_over = 0
A_Button_pressed =  False
B_Button_pressed =  False
C_Button_pressed =  False
D_Button_pressed =  False
E_Button_pressed =  False
F_Button_pressed =  False
G_Button_pressed =  False
H_Button_pressed =  False
I_Button_pressed =  False
J_Button_pressed =  False
K_Button_pressed =  False
L_Button_pressed =  False
M_Button_pressed =  False
N_Button_pressed =  False
O_Button_pressed =  False
P_Button_pressed =  False
Q_Button_pressed =  False
R_Button_pressed =  False
S_Button_pressed =  False
T_Button_pressed =  False
U_Button_pressed =  False
V_Button_pressed =  False
W_Button_pressed =  False
X_Button_pressed =  False
Y_Button_pressed =  False
Z_Button_pressed =  False

def word_display():
    win.blit(hanging_stick,(75,75))
    ### Displays the underline 
    displayed_word = list(chosen_word)
    displayed_word[0] = '_'
    displayed_word[1] = '_'
    displayed_word[2] = '_'
    displayed_word[3] = '_'
    font = pygame.font.SysFont('comicsans', 60)
    text = font.render(displayed_word[0], 1, (0,0,0))
    text2 = font.render(displayed_word[1], 1, (0,0,0))
    text3 = font.render(displayed_word[2], 1, (0,0,0))
    text4 = font.render(displayed_word[3], 1, (0,0,0))
    win.blit(text, (500,200))
    win.blit(text2, (550,200))
    win.blit(text3, (600,200))
    win.blit(text4, (650,200))


    if game_over == 1:
        win.blit(head, (190,115))
    if game_over == 2:
        win.blit(head, (190,115))
        win.blit(neck, (225,179))
    if game_over == 3:
        win.blit(head, (190,115))
        win.blit(neck, (225,179))
        win.blit(arm1, (178,180))
    if game_over == 4:
        win.blit(head, (190,115))
        win.blit(neck, (225,179))
        win.blit(arm1, (178,180))
        win.blit(arm2, (233,178))
    if game_over == 5:
        win.blit(head, (190,115))
        win.blit(neck, (225,179))
        win.blit(arm1, (178,180))
        win.blit(arm2, (233,178))
        win.blit(leg1, (189,235))
    if game_over >= 6:
        win.blit(head, (190,115))
        win.blit(neck, (225,179))
        win.blit(arm1, (178,180))
        win.blit(arm2, (233,178))
        win.blit(leg1, (189,235))
        win.blit(leg2, (232,235))
        
        gameover_font = pygame.font.SysFont('comicsans', 100)
        gameover_text = gameover_font.render('Game Over', 1, (0,0,0))
        win.blit(gameover_text, (400,0))

    


        

    if U1 == True:
        if chosen_word[0] == 'a':
            displayed_word[0] = guess
        if chosen_word[0] == 'b':
            displayed_word[0] = guess2
        if chosen_word[0] == 'c':
            displayed_word[0] = guess3
        if chosen_word[0] == 'd':
            displayed_word[0] = guess4
        if chosen_word[0] == 'e':
            displayed_word[0] = guess5
        if chosen_word[0] == 'f':
            displayed_word[0] = guess6
        if chosen_word[0] == 'g':
            displayed_word[0] = guess7
        if chosen_word[0] == 'h':
            displayed_word[0] = guess8
        if chosen_word[0] == 'i':
            displayed_word[0] = guess9
        if chosen_word[0] == 'j':
            displayed_word[0] = guess10
        if chosen_word[0] == 'k':
            displayed_word[0] = guess11
        if chosen_word[0] == 'l':
            displayed_word[0] = guess12
        if chosen_word[0] == 'm':
            displayed_word[0] = guess13
        if chosen_word[0] == 'n':
            displayed_word[0] = guess14
        if chosen_word[0] == 'o':
            displayed_word[0] = guess15
        if chosen_word[0] == 'p':
            displayed_word[0] = guess16
        if chosen_word[0] == 'q':
            displayed_word[0] = guess17
        if chosen_word[0] == 'r':
            displayed_word[0] = guess18
        if chosen_word[0] == 's':
            displayed_word[0] = guess19
        if chosen_word[0] == 't':
            displayed_word[0] = guess20
        if chosen_word[0] == 'u':
            displayed_word[0] = guess21
        if chosen_word[0] == 'v':
            displayed_word[0] = guess22
        if chosen_word[0] == 'w':
            displayed_word[0] = guess23
        if chosen_word[0] == 'x':
            displayed_word[0] = guess24
        if chosen_word[0] == 'y':
            displayed_word[0] = guess25
        if chosen_word[0] == 'z':
            displayed_word[0] = guess26
        text = font.render(displayed_word[0], 1, (0,0,0))
        win.blit(text, (500,200))
    if U2 == True:
        if chosen_word[1] == 'a':
            displayed_word[1] = guess
        if chosen_word[1] == 'b':
            displayed_word[1] = guess2
        if chosen_word[1] == 'c':
            displayed_word[1] = guess3
        if chosen_word[1] == 'd':
            displayed_word[1] = guess4
        if chosen_word[1] == 'e':
            displayed_word[1] = guess5
        if chosen_word[1] == 'f':
            displayed_word[1] = guess6
        if chosen_word[1] == 'g':
            displayed_word[1] = guess7
        if chosen_word[1] == 'h':
            displayed_word[1] = guess8
        if chosen_word[1] == 'i':
            displayed_word[1] = guess9
        if chosen_word[1] == 'j':
            displayed_word[1] = guess10
        if chosen_word[1] == 'k':
            displayed_word[1] = guess11
        if chosen_word[1] == 'l':
            displayed_word[1] = guess12
        if chosen_word[1] == 'm':
            displayed_word[1] = guess13
        if chosen_word[1] == 'n':
            displayed_word[1] = guess14
        if chosen_word[1] == 'o':
            displayed_word[1] = guess15
        if chosen_word[1] == 'p':
            displayed_word[1] = guess16
        if chosen_word[1] == 'q':
            displayed_word[1] = guess17
        if chosen_word[1] == 'r':
            displayed_word[1] = guess18
        if chosen_word[1] == 's':
            displayed_word[1] = guess19
        if chosen_word[1] == 't':
            displayed_word[1] = guess20
        if chosen_word[1] == 'u':
            displayed_word[1] = guess21
        if chosen_word[1] == 'v':
            displayed_word[1] = guess22
        if chosen_word[1] == 'w':
            displayed_word[1] = guess23
        if chosen_word[1] == 'x':
            displayed_word[1] = guess24
        if chosen_word[1] == 'y':
            displayed_word[1] = guess25
        if chosen_word[1] == 'z':
            displayed_word[1] = guess26
        text2 = font.render(displayed_word[1], 1, (0,0,0))
        win.blit(text2, (550,200))
    if U3 == True:
        if chosen_word[2] == 'a':
            displayed_word[2] = guess
        if chosen_word[2] == 'b':
            displayed_word[2] = guess2
        if chosen_word[2] == 'c':
            displayed_word[2] = guess3
        if chosen_word[2] == 'd':
            displayed_word[2] = guess4
        if chosen_word[2] == 'e':
            displayed_word[2] = guess5
        if chosen_word[2] == 'f':
            displayed_word[2] = guess6
        if chosen_word[2] == 'g':
            displayed_word[2] = guess7
        if chosen_word[2] == 'h':
            displayed_word[2] = guess8
        if chosen_word[2] == 'i':
            displayed_word[2] = guess9
        if chosen_word[2] == 'j':
            displayed_word[2] = guess10
        if chosen_word[2] == 'k':
            displayed_word[2] = guess11
        if chosen_word[2] == 'l':
            displayed_word[2] = guess12
        if chosen_word[2] == 'm':
            displayed_word[2] = guess13
        if chosen_word[2] == 'n':
            displayed_word[2] = guess14
        if chosen_word[2] == 'o':
            displayed_word[2] = guess15
        if chosen_word[2] == 'p':
            displayed_word[2] = guess16
        if chosen_word[2] == 'q':
            displayed_word[2] = guess17
        if chosen_word[2] == 'r':
            displayed_word[2] = guess18
        if chosen_word[2] == 's':
            displayed_word[2] = guess19
        if chosen_word[2] == 't':
            displayed_word[2] = guess20
        if chosen_word[2] == 'u':
            displayed_word[2] = guess21
        if chosen_word[2] == 'v':
            displayed_word[2] = guess22
        if chosen_word[2] == 'w':
            displayed_word[2] = guess23
        if chosen_word[2] == 'x':
            displayed_word[2] = guess24
        if chosen_word[2] == 'y':
            displayed_word[2] = guess25
        if chosen_word[2] == 'z':
            displayed_word[2] = guess26
        text3 = font.render(displayed_word[2], 1, (0,0,0))
        win.blit(text3, (600,200))
    if U4 == True:
        if chosen_word[3] == 'a':
            displayed_word[3] = guess
        if chosen_word[3] == 'b':
            displayed_word[3] = guess2
        if chosen_word[3] == 'c':
            displayed_word[3] = guess3
        if chosen_word[3] == 'd':
            displayed_word[3] = guess4
        if chosen_word[3] == 'e':
            displayed_word[3] = guess5
        if chosen_word[3] == 'f':
            displayed_word[3] = guess6
        if chosen_word[3] == 'g':
            displayed_word[3] = guess7
        if chosen_word[3] == 'h':
            displayed_word[3] = guess8
        if chosen_word[3] == 'i':
            displayed_word[3] = guess9
        if chosen_word[3] == 'j':
            displayed_word[3] = guess10
        if chosen_word[3] == 'k':
            displayed_word[3] = guess11
        if chosen_word[3] == 'l':
            displayed_word[3] = guess12
        if chosen_word[3] == 'm':
            displayed_word[3] = guess13
        if chosen_word[3] == 'n':
            displayed_word[3] = guess14
        if chosen_word[3] == 'o':
            displayed_word[3] = guess15
        if chosen_word[3] == 'p':
            displayed_word[3] = guess16
        if chosen_word[3] == 'q':
            displayed_word[3] = guess17
        if chosen_word[3] == 'r':
            displayed_word[3] = guess18
        if chosen_word[3] == 's':
            displayed_word[3] = guess19
        if chosen_word[3] == 't':
            displayed_word[3] = guess20
        if chosen_word[3] == 'u':
            displayed_word[3] = guess21
        if chosen_word[3] == 'v':
            displayed_word[3] = guess22
        if chosen_word[3] == 'w':
            displayed_word[3] = guess23
        if chosen_word[3] == 'x':
            displayed_word[3] = guess24
        if chosen_word[3] == 'y':
            displayed_word[3] = guess25
        if chosen_word[3] == 'z':
            displayed_word[3] = guess26
        text4 = font.render(displayed_word[3], 1, (0,0,0))
        win.blit(text4, (650,200))

    if displayed_word[0] != '_' and displayed_word[1] != '_' and displayed_word[2] != '_' and displayed_word[3] != '_':
        gamewon_font = pygame.font.SysFont('comicsans', 100)
        gamewon_text = gamewon_font.render('You Won!', 1, (0,0,0))
        win.blit(gamewon_text, (400,0))
        



    

### Class used for all the buttons in the program
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False



def redrawWindow():
    win.fill((255,255,255))
    ## Allows the buttons to dissapear when clicked on
    if A_Button_pressed == False:
        A_Button.draw(win, (0,0,0))
    if B_Button_pressed == False:
        B_Button.draw(win, (0,0,0))
    if C_Button_pressed == False:
        C_Button.draw(win, (0,0,0))
    if D_Button_pressed == False:
        D_Button.draw(win, (0,0,0))
    if E_Button_pressed == False:
        E_Button.draw(win, (0,0,0))
    if F_Button_pressed == False:
        F_Button.draw(win, (0,0,0))
    if G_Button_pressed == False:
        G_Button.draw(win, (0,0,0))
    if H_Button_pressed == False:
        H_Button.draw(win, (0,0,0))
    if I_Button_pressed == False:
        I_Button.draw(win, (0,0,0))
    if J_Button_pressed == False:
        J_Button.draw(win, (0,0,0))
    if K_Button_pressed == False:
        K_Button.draw(win, (0,0,0))
    if L_Button_pressed == False:
        L_Button.draw(win, (0,0,0))
    if M_Button_pressed == False:
        M_Button.draw(win, (0,0,0))
    if N_Button_pressed == False:
        N_Button.draw(win, (0,0,0))
    if O_Button_pressed == False:
        O_Button.draw(win, (0,0,0))
    if P_Button_pressed == False:
        P_Button.draw(win, (0,0,0))
    if Q_Button_pressed == False:
        Q_Button.draw(win, (0,0,0))
    if R_Button_pressed == False:
        R_Button.draw(win, (0,0,0))
    if S_Button_pressed == False:
        S_Button.draw(win, (0,0,0))
    if T_Button_pressed == False:
        T_Button.draw(win, (0,0,0))
    if U_Button_pressed == False:
        U_Button.draw(win, (0,0,0))
    if V_Button_pressed == False:
        V_Button.draw(win, (0,0,0))
    if W_Button_pressed == False:
        W_Button.draw(win, (0,0,0))
    if X_Button_pressed == False:
        X_Button.draw(win, (0,0,0))
    if Y_Button_pressed == False:
        Y_Button.draw(win, (0,0,0))
    if Z_Button_pressed == False:
        Z_Button.draw(win, (0,0,0))

run = True  
## Creates all the buttons used for the program
A_Button = button((192,192,192),  50-30, 400, 75, 50, 'A')
B_Button = button((192,192,192),  135-30, 400, 75, 50, 'B')
C_Button = button((192,192,192),  220-30, 400, 75, 50, 'C')
D_Button = button((192,192,192),  305-30, 400, 75, 50, 'D')
E_Button = button((192,192,192),  390-30, 400, 75, 50, 'E')
F_Button = button((192,192,192),  475-30, 400, 75, 50, 'F')
G_Button = button((192,192,192),  560-30, 400, 75, 50, 'G')
H_Button = button((192,192,192),  645-30, 400, 75, 50, 'H')
I_Button = button((192,192,192),  730-30, 400, 75, 50, 'I')
J_Button = button((192,192,192),  50-30, 465, 75, 50, 'J')
K_Button = button((192,192,192),  135-30, 465, 75, 50, 'K')
L_Button = button((192,192,192),  220-30, 465, 75, 50, 'L')
M_Button = button((192,192,192),  305-30, 465, 75, 50, 'M')
N_Button = button((192,192,192),  390-30, 465, 75, 50, 'N')
O_Button = button((192,192,192),  475-30, 465, 75, 50, 'O')
P_Button = button((192,192,192),  560-30, 465, 75, 50, 'P')
Q_Button = button((192,192,192),  645-30, 465, 75, 50, 'Q')
R_Button = button((192,192,192),  730-30, 465, 75, 50, 'R')
S_Button = button((192,192,192),  50, 530, 75, 50, 'S')
T_Button = button((192,192,192),  135, 530, 75, 50, 'T')
U_Button = button((192,192,192),  220, 530, 75, 50, 'U')
V_Button = button((192,192,192),  305, 530, 75, 50, 'V')
W_Button = button((192,192,192),  390, 530, 75, 50, 'W')
X_Button = button((192,192,192),  475, 530, 75, 50, 'X')
Y_Button = button((192,192,192),  560, 530, 75, 50, 'Y')
Z_Button = button((192,192,192),  645, 530, 75, 50, 'Z')

while run:
    redrawWindow()
    word_display()
    pygame.display.update()
    
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if A_Button.isOver(pos):
                guess = 'a'
                if guess == chosen_word[0]:
                    U1 = True
                if guess == chosen_word[1]:
                    U2 = True
                if guess == chosen_word[2]:
                    U3 = True
                if guess == chosen_word[3]:
                    U4 = True
                if guess != chosen_word[0] and guess != chosen_word[1] and guess != chosen_word[2] and guess != chosen_word[3]:
                    game_over += 1
                A_Button_pressed = True

            if B_Button.isOver(pos):
                guess2 = 'b'
                if guess2 == chosen_word[0]:
                    U1 = True
                if guess2 == chosen_word[1]:
                    U2 = True
                if guess2 == chosen_word[2]:
                    U3 = True
                if guess2 == chosen_word[3]:
                    U4 = True
                if guess2 != chosen_word[0] and guess2 != chosen_word[1] and guess2 != chosen_word[2] and guess2 != chosen_word[3]:
                    game_over += 1
                B_Button_pressed = True
            if C_Button.isOver(pos):
                guess3 = 'c'
                if guess3 == chosen_word[0]:
                    U1 = True
                if guess3 == chosen_word[1]:
                    U2 = True
                if guess3 == chosen_word[2]:
                    U3 = True
                if guess3 == chosen_word[3]:
                    U4 = True
                if guess3 != chosen_word[0] and guess3 != chosen_word[1] and guess3 != chosen_word[2] and guess3 != chosen_word[3]:
                    game_over += 1
                C_Button_pressed = True
            if D_Button.isOver(pos):
                guess4 = 'c'
                if guess4 == chosen_word[0]:
                    U1 = True
                if guess4 == chosen_word[1]:
                    U2 = True
                if guess4 == chosen_word[2]:
                    U3 = True
                if guess4 == chosen_word[3]:
                    U4 = True
                if guess4 != chosen_word[0] and guess4 != chosen_word[1] and guess4 != chosen_word[2] and guess4 != chosen_word[3]:
                    game_over += 1
                D_Button_pressed = True
            if E_Button.isOver(pos):
                guess5 = 'e'
                if guess5 == chosen_word[0]:
                    U1 = True
                if guess5 == chosen_word[1]:
                    U2 = True
                if guess5 == chosen_word[2]:
                    U3 = True
                if guess5 == chosen_word[3]:
                    U4 = True
                if guess5 != chosen_word[0] and guess5 != chosen_word[1] and guess5 != chosen_word[2] and guess5 != chosen_word[3]:
                    game_over += 1
                E_Button_pressed = True
            if F_Button.isOver(pos):
                guess6 = 'f'
                if guess6 == chosen_word[0]:
                    U1 = True
                if guess6 == chosen_word[1]:
                    U2 = True
                if guess6 == chosen_word[2]:
                    U3 = True
                if guess6 == chosen_word[3]:
                    U4 = True
                if guess6 != chosen_word[0] and guess6 != chosen_word[1] and guess6 != chosen_word[2] and guess6 != chosen_word[3]:
                    game_over += 1
                F_Button_pressed = True
            if G_Button.isOver(pos):
                guess7 = 'g'
                if guess7 == chosen_word[0]:
                    U1 = True
                if guess7 == chosen_word[1]:
                    U2 = True
                if guess7 == chosen_word[2]:
                    U3 = True
                if guess7 == chosen_word[3]:
                    U4 = True
                if guess7 != chosen_word[0] and guess7 != chosen_word[1] and guess7 != chosen_word[2] and guess7 != chosen_word[3]:
                    game_over += 1
                G_Button_pressed = True
            if H_Button.isOver(pos):
                guess8 = 'h'
                if guess8 == chosen_word[0]:
                    U1 = True
                if guess8 == chosen_word[1]:
                    U2 = True
                if guess8 == chosen_word[2]:
                    U3 = True
                if guess8 == chosen_word[3]:
                    U4 = True
                if guess8 != chosen_word[0] and guess8 != chosen_word[1] and guess8 != chosen_word[2] and guess8 != chosen_word[3]:
                    game_over += 1
                H_Button_pressed = True
            if I_Button.isOver(pos):
                guess9 = 'i'
                if guess9 == chosen_word[0]:
                    U1 = True
                if guess9 == chosen_word[1]:
                    U2 = True
                if guess9 == chosen_word[2]:
                    U3 = True
                if guess9 == chosen_word[3]:
                    U4 = True
                if guess9 != chosen_word[0] and guess9 != chosen_word[1] and guess9 != chosen_word[2] and guess9 != chosen_word[3]:
                    game_over += 1
                I_Button_pressed = True
            if J_Button.isOver(pos):
                guess10 = 'j'
                if guess10 == chosen_word[0]:
                    U1 = True
                if guess10 == chosen_word[1]:
                    U2 = True
                if guess10 == chosen_word[2]:
                    U3 = True
                if guess10 == chosen_word[3]:
                    U4 = True
                if guess10 != chosen_word[0] and guess10 != chosen_word[1] and guess10 != chosen_word[2] and guess10 != chosen_word[3]:
                    game_over += 1
                J_Button_pressed = True
            if K_Button.isOver(pos):
                guess11 = 'k'
                if guess11 == chosen_word[0]:
                    U1 = True
                if guess11 == chosen_word[1]:
                    U2 = True
                if guess11 == chosen_word[2]:
                    U3 = True
                if guess11 == chosen_word[3]:
                    U4 = True
                if guess11 != chosen_word[0] and guess11 != chosen_word[1] and guess11 != chosen_word[2] and guess11 != chosen_word[3]:
                    game_over += 1
                K_Button_pressed = True
            if L_Button.isOver(pos):
                guess12 = 'l'
                if guess12 == chosen_word[0]:
                    U1 = True
                if guess12 == chosen_word[1]:
                    U2 = True
                if guess12 == chosen_word[2]:
                    U3 = True
                if guess12 == chosen_word[3]:
                    U4 = True
                if guess12 != chosen_word[0] and guess12 != chosen_word[1] and guess12 != chosen_word[2] and guess12 != chosen_word[3]:
                    game_over += 1
                L_Button_pressed = True
            if M_Button.isOver(pos):
                guess13 = 'm'
                if guess13 == chosen_word[0]:
                    U1 = True
                if guess13 == chosen_word[1]:
                    U2 = True
                if guess13 == chosen_word[2]:
                    U3 = True
                if guess13 == chosen_word[3]:
                    U4 = True
                if guess13 != chosen_word[0] and guess13 != chosen_word[1] and guess13 != chosen_word[2] and guess13 != chosen_word[3]:
                    game_over += 1
                M_Button_pressed = True
            if N_Button.isOver(pos):
                guess14 = 'n'
                if guess14 == chosen_word[0]:
                    U1 = True
                if guess14 == chosen_word[1]:
                    U2 = True
                if guess14 == chosen_word[2]:
                    U3 = True
                if guess14 == chosen_word[3]:
                    U4 = True
                if guess14 != chosen_word[0] and guess14 != chosen_word[1] and guess14 != chosen_word[2] and guess14 != chosen_word[3]:
                    game_over += 1
                N_Button_pressed = True
            if O_Button.isOver(pos):
                guess15 = 'o'
                if guess15 == chosen_word[0]:
                    U1 = True
                if guess15 == chosen_word[1]:
                    U2 = True
                if guess15 == chosen_word[2]:
                    U3 = True
                if guess15 == chosen_word[3]:
                    U4 = True
                if guess15 != chosen_word[0] and guess15 != chosen_word[1] and guess15 != chosen_word[2] and guess15 != chosen_word[3]:
                    game_over += 1
                O_Button_pressed = True
            if P_Button.isOver(pos):
                guess16 = 'p'
                if guess16 == chosen_word[0]:
                    U1 = True
                if guess16 == chosen_word[1]:
                    U2 = True
                if guess16 == chosen_word[2]:
                    U3 = True
                if guess16 == chosen_word[3]:
                    U4 = True
                if guess16 != chosen_word[0] and guess16 != chosen_word[1] and guess16 != chosen_word[2] and guess16 != chosen_word[3]:
                    game_over += 1
                P_Button_pressed = True
            if Q_Button.isOver(pos):
                guess17 = 'q'
                if guess17 == chosen_word[0]:
                    U1 = True
                if guess17 == chosen_word[1]:
                    U2 = True
                if guess17 == chosen_word[2]:
                    U3 = True
                if guess17 == chosen_word[3]:
                    U4 = True
                if guess17 != chosen_word[0] and guess17 != chosen_word[1] and guess17 != chosen_word[2] and guess17 != chosen_word[3]:
                    game_over += 1
                Q_Button_pressed = True
            if R_Button.isOver(pos):
                guess18 = 'r'
                if guess18 == chosen_word[0]:
                    U1 = True
                if guess18 == chosen_word[1]:
                    U2 = True
                if guess18 == chosen_word[2]:
                    U3 = True
                if guess18 == chosen_word[3]:
                    U4 = True
                if guess18 != chosen_word[0] and guess18 != chosen_word[1] and guess18 != chosen_word[2] and guess18 != chosen_word[3]:
                    game_over += 1
                R_Button_pressed = True
            if S_Button.isOver(pos):
                guess19 = 's'
                if guess19 == chosen_word[0]:
                    U1 = True
                if guess19 == chosen_word[1]:
                    U2 = True
                if guess19 == chosen_word[2]:
                    U3 = True
                if guess19 == chosen_word[3]:
                    U4 = True
                if guess19 != chosen_word[0] and guess19 != chosen_word[1] and guess19 != chosen_word[2] and guess19 != chosen_word[3]:
                    game_over += 1
                S_Button_pressed = True
            if T_Button.isOver(pos):
                guess20 = 't'
                if guess20 == chosen_word[0]:
                    U1 = True
                if guess20 == chosen_word[1]:
                    U2 = True
                if guess20 == chosen_word[2]:
                    U3 = True
                if guess20 == chosen_word[3]:
                    U4 = True
                if guess20 != chosen_word[0] and guess20 != chosen_word[1] and guess20 != chosen_word[2] and guess20 != chosen_word[3]:
                    game_over += 1
                T_Button_pressed = True
            if U_Button.isOver(pos):
                guess21 = 'u'
                if guess21 == chosen_word[0]:
                    U1 = True
                if guess21 == chosen_word[1]:
                    U2 = True
                if guess21 == chosen_word[2]:
                    U3 = True
                if guess21 == chosen_word[3]:
                    U4 = True
                if guess21 != chosen_word[0] and guess21 != chosen_word[1] and guess21 != chosen_word[2] and guess21 != chosen_word[3]:
                    game_over += 1
                U_Button_pressed = True
            if V_Button.isOver(pos):
                guess22 = 'v'
                if guess22 == chosen_word[0]:
                    U1 = True
                if guess22 == chosen_word[1]:
                    U2 = True
                if guess22 == chosen_word[2]:
                    U3 = True
                if guess22 == chosen_word[3]:
                    U4 = True
                if guess22 != chosen_word[0] and guess22 != chosen_word[1] and guess22 != chosen_word[2] and guess22 != chosen_word[3]:
                    game_over += 1
                V_Button_pressed = True
            if W_Button.isOver(pos):
                guess23 = 'w'
                if guess23 == chosen_word[0]:
                    U1 = True
                if guess23 == chosen_word[1]:
                    U2 = True
                if guess23 == chosen_word[2]:
                    U3 = True
                if guess23 == chosen_word[3]:
                    U4 = True
                if guess23 != chosen_word[0] and guess23 != chosen_word[1] and guess23 != chosen_word[2] and guess23 != chosen_word[3]:
                    game_over += 1
                W_Button_pressed = True
            if X_Button.isOver(pos):
                guess24 = 'x'
                if guess24 == chosen_word[0]:
                    U1 = True
                if guess24 == chosen_word[1]:
                    U2 = True
                if guess24 == chosen_word[2]:
                    U3 = True
                if guess24 == chosen_word[3]:
                    U4 = True
                if guess24 != chosen_word[0] and guess24 != chosen_word[1] and guess24 != chosen_word[2] and guess24 != chosen_word[3]:
                    game_over += 1
                X_Button_pressed = True
            if Y_Button.isOver(pos):
                guess25 = 'y'
                if guess25 == chosen_word[0]:
                    U1 = True
                if guess25 == chosen_word[1]:
                    U2 = True
                if guess25 == chosen_word[2]:
                    U3 = True
                if guess25 == chosen_word[3]:
                    U4 = True
                if guess25 != chosen_word[0] and guess25 != chosen_word[1] and guess25 != chosen_word[2] and guess25 != chosen_word[3]:
                    game_over += 1
                Y_Button_pressed = True
            if Z_Button.isOver(pos):
                guess26 = 'z'
                if guess26 == chosen_word[0]:
                    U1 = True
                if guess26 == chosen_word[1]:
                    U2 = True
                if guess26 == chosen_word[2]:
                    U3 = True
                if guess26 == chosen_word[3]:
                    U4 = True
                if guess26 != chosen_word[0] and guess26 != chosen_word[1] and guess26 != chosen_word[2] and guess26 != chosen_word[3]:
                    game_over += 1
                Z_Button_pressed = True




        ### Helps change the shading of the buttons when the mouse is over them
        if event.type == pygame.MOUSEMOTION:
            if A_Button.isOver(pos):
                A_Button.color = (169,169,169)
            else: 
                A_Button.color = (192,192,192)

            if B_Button.isOver(pos):
                B_Button.color = (169,169,169)
            else: 
                B_Button.color = (192,192,192)
            
            if C_Button.isOver(pos):
                C_Button.color = (169,169,169)
            else: 
                C_Button.color = (192,192,192)
            
            if D_Button.isOver(pos):
                D_Button.color = (169,169,169)
            else: 
                D_Button.color = (192,192,192)
            
            if E_Button.isOver(pos):
                E_Button.color = (169,169,169)
            else: 
                E_Button.color = (192,192,192)
            
            if F_Button.isOver(pos):
                F_Button.color = (169,169,169)
            else: 
                F_Button.color = (192,192,192)
            
            if G_Button.isOver(pos):
                G_Button.color = (169,169,169)
            else: 
                G_Button.color = (192,192,192)
            
            if H_Button.isOver(pos):
                H_Button.color = (169,169,169)
            else: 
                H_Button.color = (192,192,192)
            
            if I_Button.isOver(pos):
                I_Button.color = (169,169,169)
            else: 
                I_Button.color = (192,192,192)
            
            if J_Button.isOver(pos):
                J_Button.color = (169,169,169)
            else: 
                J_Button.color = (192,192,192)
            
            if K_Button.isOver(pos):
                K_Button.color = (169,169,169)
            else: 
                K_Button.color = (192,192,192)
            
            if L_Button.isOver(pos):
                L_Button.color = (169,169,169)
            else: 
                L_Button.color = (192,192,192)
            
            if M_Button.isOver(pos):
                M_Button.color = (169,169,169)
            else: 
                M_Button.color = (192,192,192)
            
            if N_Button.isOver(pos):
                N_Button.color = (169,169,169)
            else: 
                N_Button.color = (192,192,192)
            
            if O_Button.isOver(pos):
                O_Button.color = (169,169,169)
            else: 
                O_Button.color = (192,192,192)
            
            if P_Button.isOver(pos):
                P_Button.color = (169,169,169)
            else: 
                P_Button.color = (192,192,192)
            
            if Q_Button.isOver(pos):
                Q_Button.color = (169,169,169)
            else: 
                Q_Button.color = (192,192,192)
            
            if R_Button.isOver(pos):
                R_Button.color = (169,169,169)
            else: 
                R_Button.color = (192,192,192)
            
            if S_Button.isOver(pos):
                S_Button.color = (169,169,169)
            else: 
                S_Button.color = (192,192,192)
            
            if T_Button.isOver(pos):
                T_Button.color = (169,169,169)
            else: 
                T_Button.color = (192,192,192)
            
            if U_Button.isOver(pos):
                U_Button.color = (169,169,169)
            else: 
                U_Button.color = (192,192,192)

            if V_Button.isOver(pos):
                V_Button.color = (169,169,169)
            else: 
                V_Button.color = (192,192,192)
            
            if W_Button.isOver(pos):
                W_Button.color = (169,169,169)
            else: 
                W_Button.color = (192,192,192)
            
            if X_Button.isOver(pos):
                X_Button.color = (169,169,169)
            else: 
                X_Button.color = (192,192,192)
            
            if Y_Button.isOver(pos):
                Y_Button.color = (169,169,169)
            else: 
                Y_Button.color = (192,192,192)
            
            if Z_Button.isOver(pos):
                Z_Button.color = (169,169,169)
            else: 
                Z_Button.color = (192,192,192)
            
        