import os
import turtle
from Turtle import racer

win_length = 500
win_height = 500
turtles = 8

turtle.screensize(win_length,win_height)

path = 'Turtle-Race\score\scores.txt'

def setupFile(name, colors):
    file = open(name, 'w')
    for color in colors:
        file.write(color + ' 0 \n')
    file.close()


def startGame(choose=None):
    tList = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ['red', 'green', 'blue', 'yellow', 'pink', 'orange', 'purple', 'black', 'grey']
    start = -(win_length/2) + 20
    for t in range(turtles):
        newPosX = start + t*(win_length)//turtles
        tList.append(racer(colors[t],(newPosX, -230)))
        tList[t].turt.showturtle()

    run = True
    while run:
        for t in tList:
            t.move()

        maxColor = []
        maxDis = 0
        for t in tList:
            if t.pos[1] > 230 and t.pos[1] > maxDis:
                maxDis = t.pos[1]
                maxColor = []
                maxColor.append(t.color)
            elif t.pos[1] > 230 and t.pos[1] == maxDis:
                maxDis = t.pos[1]
                maxColor.append(t.color)

        if len(maxColor) > 0:
            run = False
            print('The winner is: ')
            for win in maxColor:
                print(win)

    if win == choose.lower():
        print('You got it!')
    else:
        print('Try again!')
    
    if os.path.isfile(path) != True:
        setupFile(path,colors)
    oldScore = []
    file = open(path, 'r')
    for line in file:
        l = line.split()
        color = l[0]
        score = l[1]
        oldScore.append([color, score])

    file.close()
    file = open(path, 'w')

    for entry in oldScore:
        for winner in maxColor:
            if entry[0] == winner:
                entry[1] = int(entry[1]) + 1

        file.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')

    file.close()

def Title():
    print("Turtle color : red, green, blue, yellow, pink, orange, purple, black, grey")
    print("Which color of turtle would you like to play ?")

if __name__ == "__main__":
    print("Welcome to Turtle Racing!!!")
    Title()
    choose = input('>>>')
    startGame(choose)
    while True:
        print("-----------------------------------")
        print("Would you like to play again ?")
        start = input('>>>')
        if start.lower() not in {'y','Y','yes','Yes'}: 
            break
        select = input('Would you want to change your turtle? ')
        if select.lower() in {'y','Y','yes','Yes'}:
            Title()
            choose = input('>>>')
        startGame(choose)
    
    print('Thanks to play!')
