import random
import os
import pygame
from pygame import mouse



#################### Jocul 1 ##################


"""pygame.init()
WIDTH, HEIGHT = 1000, 800
WIN =pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (233,233,233)
GREEN = (8,76,65)
BLACK = (0,0,0)
FONT_TITLE = pygame.font.SysFont('Bradley Hand ITC', 50, bold = pygame.font.Font.bold)
FONT_ANSWER = pygame.font.SysFont('Bradley Hand ITC', 35, bold = pygame.font.Font.bold)
FPS = 60

pygame.display.set_caption("Mystic Ball")
PATH = 'D:\Lucrari de laborator\Semestrul 3\PI\Assets'
BALL = pygame.image.load(os.path.join(PATH, 'ball.png'))
BALL = pygame.transform.scale(BALL, (800,700))
text = FONT_TITLE.render("Pune o intrebare si apasa pe bila",True , WHITE)

def getText():
    myDict = {
        1: "Probabil da",
        2: "Probabil nu",
        3: "Cu siguranta nu",
        4: "Nu sunt sigur",
        5: "Cu siguranta da",
        6: "Mai bine nu spun",
        7: "Intrebarea nu este clara!",
        8: "Stele spun ca da",
        9: "DA!",
        10: "Puteti fi sigur de asta",
        11: "Nu cred ca vreti sa stiti",
        12: "Iti spun mai tarziu",
        13: "Perspectivele sunt bune"
    }
    return random.choice(list(myDict.values()))

def draw_window(text2):
    WIN.fill(GREEN)
    WIN.blit(BALL, (100,100))
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    WIN.blit(text2, (350,360))

    pygame.display.update()

def main():
    text2 = FONT_ANSWER.render("",True , BLACK)
    clock = pygame.time.Clock()
    run =True
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        mousePress = pygame.mouse.get_pressed()
        if mousePress[0]:
            for i in range(9999):
                text2 = FONT_ANSWER.render(getText(),True, BLACK)
        draw_window(text2)
    
    pygame.quit()



if __name__ == "__main__":
    main()
"""

#################### Jocul 2 #####################
"""pygame.init()
WIDTH, HEIGHT = 1000, 800
WIN =pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (233,233,233)
GREEN = (8,76,65)
BLACK = (0,0,0)
FONT_TITLE = pygame.font.SysFont('Bradley Hand ITC', 42, bold = pygame.font.Font.bold)
FONT_ANSWER = pygame.font.SysFont('Bradley Hand ITC', 55, bold = pygame.font.Font.bold)
FPS = 60

pygame.display.set_caption("Ghiceste numarul!")
text = FONT_TITLE.render("Ghiceste numarul din intervalul 0- 50",True , WHITE)


def draw_window(numar, raspuns):
    WIN.fill(GREEN)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    numar = FONT_ANSWER.render(numar, True, WHITE)
    WIN.blit(numar, (WIDTH/2 - numar.get_width()/2,HEIGHT/2-numar.get_height()/2))

    raspuns = FONT_ANSWER.render(raspuns, True, WHITE)
    WIN.blit(raspuns, (WIDTH/2 - raspuns.get_width()/2, 480))

    pygame.display.update()



def check(numarRandom,numarAles):
    if int(numarAles) == int(numarRandom):
        return "Bravo! Ai ghicit!",True
    elif (int(numarAles) >= int(numarRandom+10) or int(numarAles) <= int(numarRandom-10) ):
        return "Rece",False
    elif (int(numarAles) >= int(numarRandom+5) and int(numarAles) < int(numarRandom+10) or int(numarAles) <= int(numarRandom-5) and int(numarAles) > int(numarRandom-10) ):
        return "Caldut!",False
    elif (int(numarAles) < int(numarRandom+5) or int(numarAles) > (numarRandom-5)):
        return "Fierbinte!", False
    


def main():
    numarRandom = random.randint(0, 50)
    number = ''
    response =''
    clock = pygame.time.Clock()
    run =True
    won = False
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    number = number[:-1]
                if event.key == pygame.K_RETURN: #enter
                    response,won = check(numarRandom,number)
                    number = ''
                if event.key == pygame.K_KP0:
                    number+='0'
                if event.key == pygame.K_KP1:
                    number+='1'
                if event.key == pygame.K_KP2:
                    number+='2'
                if event.key == pygame.K_KP3:
                    number+='3'
                if event.key == pygame.K_KP4:
                    number+='4'
                if event.key == pygame.K_KP5:
                    number+='5'
                if event.key == pygame.K_KP6:
                    number+='6'
                if event.key == pygame.K_KP7:
                    number+='7'
                if event.key == pygame.K_KP8:
                    number+='8'
                if event.key == pygame.K_KP9:
                    number+='9'
        draw_window(number,response)
        #In caz de castig
        if won:
            pygame.time.delay(3000)
            return True

    pygame.quit()



if __name__ == "__main__":
    main()
"""

##################### Jocul 3 ########################

"""pygame.init()
WIDTH, HEIGHT = 1000, 800
WIN =pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (233,233,233)
GREEN = (8,76,65)
BLACK = (0,0,0)
PATH = 'D:\Lucrari de laborator\Semestrul 3\PI\Assets'

FOARFECE  = pygame.image.load(os.path.join(PATH, 'foarfece.png'))
FOARFECE = pygame.transform.scale(FOARFECE, (200,160))

PIATRA = pygame.image.load(os.path.join(PATH, 'piatra.png'))
PIATRA = pygame.transform.scale(PIATRA, (200,160))

HARTIE  = pygame.image.load(os.path.join(PATH, 'hartie.png'))
HARTIE = pygame.transform.scale(HARTIE, (200,160))

INTREBARE  = pygame.image.load(os.path.join(PATH, 'intreb.png'))
INTREBARE = pygame.transform.scale(INTREBARE, (100,200))

FONT_TITLE = pygame.font.SysFont('Bradley Hand ITC', 60, bold = pygame.font.Font.bold)
FONT_ANSWER = pygame.font.SysFont('Bradley Hand ITC', 55, bold = pygame.font.Font.bold)
FPS = 60
pygame.display.set_caption("Piatra, foarfece, hartie")
text = FONT_TITLE.render("Fati alegerea!",True , WHITE)
myDict2 ={
    0: INTREBARE,
    1: PIATRA,
    2: FOARFECE,
    3: HARTIE
}

def draw_window(numar,numarRandom, raspuns):
    WIN.fill(GREEN)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    WIN.blit(PIATRA, (5,100))
    WIN.blit(FOARFECE, (5, 360))
    WIN.blit(HARTIE, (5,620))
    tu = FONT_ANSWER.render("Eu", True, WHITE)
    WIN.blit(tu, (360, 220))
    calculator = FONT_ANSWER.render("Calculator", True, WHITE)
    WIN.blit(calculator, (620, 220))
    
    WIN.blit(myDict2[numar], (300,300))
    WIN.blit(myDict2[numarRandom], (600,300))

    raspuns = FONT_ANSWER.render(raspuns, True, WHITE)
    WIN.blit(raspuns, ((WIDTH/2 - raspuns.get_width()/2)+50, 480))

    pygame.display.update()



def check(numarAles):
    numarRandom = random.randint(1, 3)
    myDict = {
        1: [2],
        2: [3],
        3: [1]
    }
    if int(numarAles) == int(numarRandom):
        return "Egalitate!", numarRandom
    elif (numarRandom in myDict[numarAles]):
        return "Ati castigat!",numarRandom
    else:
        return "Ati pierdut!", numarRandom
    
    


def main():
    numarRandom = 0
    number = 0
    response =''
    clock = pygame.time.Clock()
    run =True
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[0]<200 and pygame.mouse.get_pos()[1]>=100 and pygame.mouse.get_pos()[1]<260:
                    number = 1
                    response,numarRandom = check( number)
                    #piatra
                if pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[0]<200 and pygame.mouse.get_pos()[1]>=360 and pygame.mouse.get_pos()[1]<520:
                    number = 2
                    response,numarRandom = check( number)
                    #foarfece
                if pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[0]<200 and pygame.mouse.get_pos()[1]>=620 and pygame.mouse.get_pos()[1]<780:
                    number = 3
                    response,numarRandom = check( number)
                    #hartie
                

        draw_window(number,numarRandom, response)
        

    pygame.quit()



if __name__ == "__main__":
    main()"""


################### Jocul 4 ##################
"""pygame.init()
WIDTH, HEIGHT = 1000, 800
WIN =pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (233,233,233)
GREEN = (8,76,65)
BLACK = (0,0,0)
PATH = 'D:\Lucrari de laborator\Semestrul 3\PI\Assets'

FOARFECE = pygame.image.load(os.path.join(PATH, 'foarfece.png'))
FOARFECE = pygame.transform.scale(FOARFECE, (200,160))

PIATRA = pygame.image.load(os.path.join(PATH, 'piatra.png'))
PIATRA = pygame.transform.scale(PIATRA, (200,160))

HARTIE = pygame.image.load(os.path.join(PATH, 'hartie.png'))
HARTIE = pygame.transform.scale(HARTIE, (200,160))

LIZARD = pygame.image.load(os.path.join(PATH, 'lizard.png'))
LIZARD = pygame.transform.scale(LIZARD, (200,160))

SPOCK = pygame.image.load(os.path.join(PATH, 'spock.png'))
SPOCK = pygame.transform.scale(SPOCK, (200,160))

INTREBARE  = pygame.image.load(os.path.join(PATH, 'intreb.png'))
INTREBARE = pygame.transform.scale(INTREBARE, (100,200))

FONT_TITLE = pygame.font.SysFont('Bradley Hand ITC', 60, bold = pygame.font.Font.bold)
FONT_ANSWER = pygame.font.SysFont('Bradley Hand ITC', 55, bold = pygame.font.Font.bold)
FPS = 60
pygame.display.set_caption("Piatra, foarfece, hartie")
text = FONT_TITLE.render("Fati alegerea!",True , WHITE)
myDict2 ={
    0: INTREBARE,
    1: PIATRA,
    2: FOARFECE,
    3: HARTIE,
    4: LIZARD,
    5: SPOCK
}

def draw_window(numar,numarRandom, raspuns):
    WIN.fill(GREEN)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    WIN.blit(PIATRA, (5,100))
    WIN.blit(FOARFECE, (5, 360))
    WIN.blit(HARTIE, (5,620))
    WIN.blit(LIZARD, (305,620))
    WIN.blit(SPOCK, (605,620))
    tu = FONT_ANSWER.render("Eu", True, WHITE)
    WIN.blit(tu, (360, 220))
    calculator = FONT_ANSWER.render("Calculator", True, WHITE)
    WIN.blit(calculator, (620, 220))
    
    WIN.blit(myDict2[numar], (300,300))
    WIN.blit(myDict2[numarRandom], (600,300))

    raspuns = FONT_ANSWER.render(raspuns, True, WHITE)
    WIN.blit(raspuns, ((WIDTH/2 - raspuns.get_width()/2)+50, 480))

    pygame.display.update()



def check(numarAles):
    numarRandom = random.randint(1, 5)
    myDict = {
        1: [2,4],
        2: [3,4],
        3: [1,5],
        4: [3,5],
        5: [1,2]
    }
    if int(numarAles) == int(numarRandom):
        return "Egalitate!", numarRandom
    elif (numarRandom in myDict[numarAles]):
        return "Ati castigat!",numarRandom
    else:
        return "Ati pierdut!", numarRandom
    
    
def main():
    numarRandom = 0
    number = 0
    response =''
    clock = pygame.time.Clock()
    run =True
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[0]<200 and pygame.mouse.get_pos()[1]>=100 and pygame.mouse.get_pos()[1]<260:
                    number = 1
                    response,numarRandom = check( number)
                    #piatra
                if pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[0]<200 and pygame.mouse.get_pos()[1]>=360 and pygame.mouse.get_pos()[1]<520:
                    number = 2
                    response,numarRandom = check( number)
                    #foarfece
                if pygame.mouse.get_pos()[0]>=0 and pygame.mouse.get_pos()[0]<200 and pygame.mouse.get_pos()[1]>=620 and pygame.mouse.get_pos()[1]<780:
                    number = 3
                    response,numarRandom = check( number)
                    #hartie
                if pygame.mouse.get_pos()[0]>=300 and pygame.mouse.get_pos()[0]<500 and pygame.mouse.get_pos()[1]>=620 and pygame.mouse.get_pos()[1]<780:
                    number = 4
                    response,numarRandom = check( number)
                    #Lizard
                if pygame.mouse.get_pos()[0]>=600 and pygame.mouse.get_pos()[0]<800 and pygame.mouse.get_pos()[1]>=620 and pygame.mouse.get_pos()[1]<780:
                    number = 5
                    response,numarRandom = check( number)
                    #Spock

        draw_window(number,numarRandom, response)
        

    pygame.quit()



if __name__ == "__main__":
    main()"""


##################### Jocul 5 #################

"""pygame.init()
WIDTH, HEIGHT = 1000, 1000
WIN =pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (233,233,233)
GREEN = (8,76,65)
BLACK = (0,0,0)
FONT_TITLE = pygame.font.SysFont('Bradley Hand ITC', 50, bold = pygame.font.Font.bold)
FONT_ANSWER = pygame.font.SysFont('Bradley Hand ITC', 35, bold = pygame.font.Font.bold)
FPS = 60

pygame.display.set_caption("Arunca moneda")
PATH = 'D:\Lucrari de laborator\Semestrul 3\PI\Assets'

CAP = pygame.image.load(os.path.join(PATH, 'cap.png'))
CAP = pygame.transform.scale(CAP, (700,700))

PAJURA = pygame.image.load(os.path.join(PATH, 'pajura.png'))
PAJURA = pygame.transform.scale(PAJURA, (700,700))

MONEDA = pygame.image.load(os.path.join(PATH, 'coin.jpg'))
MONEDA = pygame.transform.scale(MONEDA, (700,700))

START = pygame.image.load(os.path.join(PATH, 'start.png'))
START = pygame.transform.scale(START, (350,150))

myDict = {
    0: MONEDA,
    1: CAP,
    2: PAJURA
}


text = FONT_TITLE.render("Apasa start pentru a arunca moneda",True , WHITE)
def getNumber():
    return random.randint(1, 2)

def draw_window(nr):
    WIN.fill(GREEN)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    WIN.blit(myDict[nr], (150,100))
    WIN.blit(START, (325,800))
    pygame.display.update()

def main():
    alegere = 0
    clock = pygame.time.Clock()
    run =True
    draw_window(alegere)
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]>=350 and pygame.mouse.get_pos()[0]<=650 and pygame.mouse.get_pos()[1]>=800 and pygame.mouse.get_pos()[1]<950:
                    for i in range(20):
                        alegere =getNumber()          
                        draw_window(alegere)
    
    pygame.quit()


if __name__ == "__main__":
    main()
"""

########### Jocul 6 ##################

pygame.init()
WIDTH, HEIGHT = 1000, 1000
WIN =pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (233,233,233)
GREEN = (8,76,65)
BLACK = (0,0,0)
FONT_TITLE = pygame.font.SysFont('Bradley Hand ITC', 50, bold = pygame.font.Font.bold)
FONT_ANSWER = pygame.font.SysFont('Bradley Hand ITC', 35, bold = pygame.font.Font.bold)
FPS = 60

pygame.display.set_caption("Trage paiul cel lung")
PATH = 'D:\Lucrari de laborator\Semestrul 3\PI\Assets'

CAP = pygame.image.load(os.path.join(PATH, 'win.jpg'))
CAP = pygame.transform.scale(CAP, (700,700))

PAJURA = pygame.image.load(os.path.join(PATH, 'lose.jpg'))
PAJURA = pygame.transform.scale(PAJURA, (700,700))

MONEDA = pygame.image.load(os.path.join(PATH, 'pai.jpg'))
MONEDA = pygame.transform.scale(MONEDA, (700,700))

START = pygame.image.load(os.path.join(PATH, 'start.png'))
START = pygame.transform.scale(START, (350,150))

myDict = {
    0: MONEDA,
    1: CAP,
    2: PAJURA
}


text = FONT_TITLE.render("Apasa start pentru a trage paiul",True , WHITE)
def getNumber():
    return random.randint(1, 2)

def draw_window(nr):
    WIN.fill(GREEN)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    WIN.blit(myDict[nr], (150,100))
    WIN.blit(START, (325,800))
    pygame.display.update()

def main():
    alegere = 0
    clock = pygame.time.Clock()
    run =True
    draw_window(alegere)
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]>=350 and pygame.mouse.get_pos()[0]<=650 and pygame.mouse.get_pos()[1]>=800 and pygame.mouse.get_pos()[1]<950:
                    for i in range(20):
                        alegere =getNumber()          
                        draw_window(alegere)
    
    pygame.quit()

if __name__ == "__main__":
    main()