import pygame as pg
import random
import os

white = (255, 255, 255)
randomcolor = (240, 130, 233)

pg.init()

screen_width = 1200
screen_heigth = 600

gameWindow = pg.display.set_mode((screen_width, screen_heigth))
pg.display.set_caption("Rock Paper Scissors")

clock = pg.time.Clock()
font = pg.font.SysFont(None, 55)
User_Input = "P"
FPS = 60

image1 = pg.image.load("Rock Paper Scissors/assets/R.png")
image1 = pg.transform.scale(image1, (230, 230)).convert_alpha()

image2 = pg.image.load("Rock Paper Scissors/assets/P.png")
image2 = pg.transform.scale(image2, (230, 230)).convert_alpha()

image3 = pg.image.load("Rock Paper Scissors/assets/S.png")
image3 = pg.transform.scale(image3, (230, 230)).convert_alpha()

def text_screen(title, color, x, y):
    text = font.render(title, True, color)
    gameWindow.blit(text, [x, y])

Score = 0
enemyScore = 0
def result_time():
    gameWindow.fill(white)
    global Score
    global enemyScore
    rand = random.choice("RPSRPSRPSRPSRPSRPSRPSRPSRPS") 
    
    if not os.path.exists("Rock Paper Scissors/assets/userdatabase.txt"):
        with open('Rock Paper Scissors/assets/userdatabase.txt', 'w') as f:
            f.write("0")

    if not os.path.exists("Rock Paper Scissors/assets/AIdatabase.txt"):
        with open('Rock Paper Scissors/assets/AIdatabase.txt', 'w') as j:
            j.write("0")

    with open('Rock Paper Scissors/assets/userdatabase.txt', 'r') as i:
        highscore = i.read()

    with open('Rock Paper Scissors/assets/AIdatabase.txt', 'r') as x:
        AIhighscore = x.read()

    
    if (User_Input == 'R' and rand == 'S'):
        text_screen("You wins.", randomcolor, 500, 270)
        Score += 10

    elif (User_Input == 'R' and rand == 'R'):
        text_screen("Tie", randomcolor, 550, 270)

    elif (User_Input == 'S' and rand == 'P'):
        text_screen("You wins.", randomcolor, 500, 270)
        Score += 10

    elif (User_Input == 'S' and rand == 'S'):
        text_screen("Tie", randomcolor, 550, 270)

    elif (User_Input == 'P' and rand == 'P'):
        text_screen("Tie", randomcolor, 550, 270)

    elif (User_Input == 'P' and rand == 'S'):
        text_screen("A.I wins.", randomcolor, 500, 270)
        enemyScore += 10

    elif (User_Input == 'R'and rand == 'P'):
        text_screen("A.I wins.", randomcolor, 500, 270)
        enemyScore += 10

    elif (User_Input == 'P' and rand == 'R'):
        text_screen("You wins.", randomcolor, 500, 270)
        Score += 10

    elif (User_Input == 'S' and rand == 'R'):
        text_screen("A.I wins.", randomcolor, 500, 270)
        enemyScore += 10
    
    if Score > int(highscore):
        highscore = Score
    
    if enemyScore > int(AIhighscore):
        AIhighscore = enemyScore

    with open('Rock Paper Scissors/assets/userdatabase.txt', 'w') as f:
        f.write(f"{highscore}")
    
    with open('Rock Paper Scissors/assets/AIdatabase.txt', 'w') as j:
        j.write(f"{AIhighscore}")
    
    exit_game = False
    while not exit_game:
        image1 = pg.image.load(f"Rock Paper Scissors/assets/{User_Input}.png")
        image1 = pg.transform.scale(image1, (230, 230)).convert_alpha()

        image2 = pg.image.load(f"Rock Paper Scissors/assets/{rand}.png")
        image2 = pg.transform.scale(image2, (230, 230)).convert_alpha()

        text_screen("Press Enter To Restart", randomcolor, 390, 50)
        text_screen(f"Score: {Score}     A.I Score: {enemyScore}", randomcolor, 0, 0)
        text_screen(f"Your High Score: {highscore}     A.I High Score: {AIhighscore}", randomcolor, 0, 550)
        gameWindow.blit(image1, (70, 200))
        gameWindow.blit(image2, (900, 200))
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    game_loop()
                    exit_game = True

def game_loop():
    exit_game = False
    global User_Input
    
    while not exit_game:

        if not os.path.exists("Rock Paper Scissors/assets/userdatabase.txt"):
            with open('Rock Paper Scissors/assets/userdatabase.txt', 'w') as f:
                f.write("0")

        if not os.path.exists("Rock Paper Scissors/assets/AIdatabase.txt"):
            with open('Rock Paper Scissors/assets/AIdatabase.txt', 'w') as j:
                j.write("0")
                
        with open('Rock Paper Scissors/assets/userdatabase.txt', 'r') as i:
            highscore = i.read()

        with open('Rock Paper Scissors/assets/AIdatabase.txt', 'r') as i:
            AIhighscore = i.read()

        gameWindow.fill(white)
        gameWindow.blit(image1, (70, 200))
        gameWindow.blit(image2, (500, 200))
        gameWindow.blit(image3, (900, 200))
        text_screen("R", randomcolor, 170, 170)
        text_screen("P", randomcolor, 610, 170)
        text_screen("S", randomcolor, 1005, 170)
        text_screen("Press Key To Select Choice", randomcolor, 340, 50)
        text_screen(f"Score: {Score}     A.I Score: {enemyScore}", randomcolor, 0, 0)
        text_screen(f"Your High Score: {highscore}     A.I High Score: {AIhighscore}", randomcolor, 0, 550)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    User_Input = "R"
                    result_time()   
                    exit_game = True 
                
                if event.key == pg.K_p:
                    User_Input = "P"
                    result_time()    
                    exit_game = True 

                if event.key == pg.K_s:
                    User_Input = "S"
                    result_time()    
                    exit_game = True

        pg.display.update()

clock.tick(FPS)

game_loop()

pg.quit()
quit()