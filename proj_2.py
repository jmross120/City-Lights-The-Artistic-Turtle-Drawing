import turtle
import math
import random

t = turtle.Turtle()
win = turtle.Screen()
turtle.colormode()

def window_sys(win):
    win.bgcolor(0, 0, 0.495)
    win.title("City Lights")
    win.setup(1000,750)

def background_gradient(t, win):
    
    from turtle import Screen, Turtle

    TARGET = (255/255, 204/255, 229/255)
    COLOR = (0.0, 0.0, 102/255)

    
    win.tracer(False)

    WIDTH, HEIGHT = win.window_width(), win.window_height()

    deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]

    t.color(COLOR)

    t.penup()
    t.goto(-WIDTH/2, HEIGHT/2)
    t.pendown()

    direction = 1

    for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):
        t.forward(WIDTH * direction)
        t.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
        t.sety(y)
        direction *= -1

    win.tracer(True)

    ''' 

    I initially made a background gradient using my own code which is written below. 
    It works, but it took a long time to be drawn out. 
    I found the code above online.
    It does the same thing, it just draws the gradient faster than the one i wrote which 
    i thought would be better for you.
    
    
    t.penup()
    height = -375
    t.goto(-500, height)
    t.pendown()
    r = 1.0
    g = 0.8
    b = 0.89
    while [r, g, b] > [0, 0, 0.495]:
        t.pencolor((r, g, b))
        t.forward(1000)
        t.penup()
        t.right(270)
        t.forward(1)
        t.left(90)
        t.pendown()
        r = r - 0.0013
        g = g - 0.0010
        b = b - 0.00066
        height = height + 1
        t.goto(-500, height)

'''

    
        
def tower(t, color, height, length, xpos, ypos):
    t.penup()
    t.goto(xpos, ypos)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.left(90)
    t.begin_fill()
    t.forward(height)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(length)
    t.end_fill()

def lights(t, xpos, ypos, height, length, color, gap, win_height, win_width):
    t.penup()
    t.goto(xpos, ypos)
    t.pencolor(color)
    t.pendown()
    for i in range(length):
        for _ in range (height):
            t.fillcolor(color)
            t.begin_fill()
            t.right(90)
            t.forward(win_height)
            t.right(90)
            t.forward(win_width)
            t.right(90)
            t.forward(win_height)
            t.right(90)
            t.forward(win_width)
            t.right(90)
            t.end_fill()
            t.penup()
            t.forward(gap + 10)
            t.left(90)
            t.pendown()
        t.penup()
        t.goto(xpos, ypos)
        t.left(180)
        t.forward(i * gap)
        t.left(180)
        t.pendown()
    t.left(180)

def moon(t, xpos, ypos):
    t.penup()
    t.goto(xpos, ypos)
    t.pendown()
    t.pencolor("beige")
    t.fillcolor("beige")
    t.begin_fill()
    for _ in range(70):
        t.forward(4)
        t.left(3)
    t.left(160)
    for _ in range(50):
        t.forward(4)
        t.right(3)
    t.end_fill()
    t.left(140)

# def ground():

def foregroud(t):
#bottom
    t.penup()
    t.goto(-500, -375)
    t.pendown()
    t.fillcolor((250/255, 255/255, 208/255))
    t.pencolor((250/255, 255/255, 208/255))
    t.begin_fill()
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(875)
    t.right(35)
    t.forward(150)
    t.right(55)
    t.forward(200)
    t.right(90)
    t.forward(900)
    t.right(180)
    t.end_fill()
#second layer
    t.penup()
    t.goto(-500, -375)
    t.pendown()
    t.pencolor((94/255, 116/255, 162/255))
    t.fillcolor((94/255, 116/255, 162/255))
    t.begin_fill()
    t.left(90)
    t.forward(190)
    t.right(90)
    t.forward(850)
    t.right(35)
    t.forward(200)
    t.right(55)
    t.forward(200)
    t.right(90)
    t.forward(900)
    t.right(180)
    t.end_fill()
#ground
    t.penup()
    t.goto(-500, -375)
    t.pendown()
    t.pencolor((247/255, 172/255, 106/255))
    t.fillcolor((247/255, 172/255, 106/255))
    t.begin_fill()
    t.left(90)
    t.forward(140)
    t.right(90)
    t.forward(850)
    t.right(35)
    t.forward(200)
    t.right(55)
    t.forward(200)
    t.right(90)
    t.forward(900)
    t.right(180)
    t.end_fill()
#pool
    t.penup()
    t.goto(-500, -375)
    t.pendown()
    t.pencolor((73/255, 91/255, 182/255))
    t.fillcolor((73/255, 91/255, 182/255))
    t.begin_fill()
    t.left(90)
    t.forward(120)
    t.right(90)
    t.forward(725)
    t.right(60)
    t.forward(200)
    t.right(120)
    t.forward(800)
    t.left(180)
    t.end_fill()

def foreground_shadows(t):
#shadow on second layer
    t.penup()
    t.goto(-500, -375)
    t.pencolor((27/255, 42/255, 122/255))
    t.fillcolor((27/255, 42/255, 122/255))
    t.left(90)
    t.forward(190)
    t.right(90)
    t.forward(850)
    t.pendown()
    t.begin_fill()
    t.right(135)
    t.forward(70)
    t.left(135)
    t.forward(49)
    t.left(90)
    t.forward(48)
    t.right(90)
    t.end_fill()
#right wall shadow
    t.penup()
    t.goto(-500, -375)
    t.pencolor((56/255, 71/255, 146/255))
    t.fillcolor((56/255, 71/255, 146/255))
    t.left(90)
    t.forward(190)
    t.right(90)
    t.forward(850)
    t.right(35)
    t.begin_fill()
    t.pendown()
    t.forward(200)
    t.right(55)
    t.forward(50)
    t.right(125)
    t.forward(200)
    t.right(55)
    t.forward(50)
    t.right(90)
    t.end_fill()
#ground shadow
    t.penup()
    t.goto(-500, -375)
    t.pencolor((168/255, 110/255, 60/255))
    t.fillcolor((168/255, 110/255, 60/255))
    t.left(90)
    t.forward(140)
    t.right(90)
    t.forward(850)
    t.begin_fill()
    t.pendown()
    t.right(35)
    t.forward(200)
    t.right(55)
    t.forward(70)
    t.right(131)
    t.forward(282)
    t.right(145)
    t.end_fill()

def skyline(t):
#first background layer
    t.penup()
    t.goto(-500, -375)
    t.pendown()
    t.pencolor((73/255, 91/255, 182/255))
    t.fillcolor((73/255, 91/255, 182/255))
    t.begin_fill()
    t.left(90)
    t.forward(375)
    t.right(90)
    t.forward(1000)
    t.right(90)
    t.forward(375)
    t.right(90)
    t.forward(1000)
    t.left(180)
    t.end_fill()
#second background layer
    t.penup()
    t.goto(-500, -375)
    t.pendown()
    t.pencolor((43/255, 48/255, 110/255))
    t.fillcolor((43/255, 48/255, 110/255))
    t.begin_fill()
    t.left(90)
    t.forward(290)
    t.right(90)
    t.forward(1000)
    t.right(90)
    t.forward(290)
    t.right(90)
    t.forward(1000)
    t.left(180)
    t.end_fill()

def city_skyline(t, num_towers):
    #background
    for _ in range(10):
        height = random.randint(180, 230)
        length = random.randint(30, 100)
        xpos = random.randint(-120, 120)
        ypos = -175
        color = ([43/255, 48/255, 110/255])
        tower(t, color, height, length, xpos, ypos)

        light_height = int(height / 13)
        light_length = 1
        light_color = (random.uniform(0.7, 1), random.uniform(0.7, 1), 0)
        gap = 3
        win_height = random.randint(2, 5)
        win_width = length - 10
        lights(t, xpos + 5, ypos, light_height, light_length, light_color, gap, win_height, win_width)
    #middle
    for _ in range(15):
        height = random.randint(120,170)
        length = random.randint(30, 100)
        xpos = random.randint(-225, 225)
        ypos = -175
        color = ([43/255, 48/255, 110/255])
        tower(t, color, height, length, xpos, ypos)

        light_height = int(height / 13)
        light_length = 1
        light_color = (random.uniform(0.7, 1), random.uniform(0.7, 1), 0)
        gap = 3
        win_height = random.randint(2, 5)
        win_width = length - 10
        lights(t, xpos + 5, ypos, light_height, light_length, light_color, gap, win_height, win_width)
    #foreground
    for _ in range(num_towers):
        height = random.randint(60, 110)
        length = random.randint(30, 100)
        xpos = random.randint(-375, 375)
        ypos = -175
        color = ([43/255, 48/255, 110/255])
        tower(t, color, height, length, xpos, ypos)

        light_height = int(height / 13)
        light_length = 1
        light_color = (random.uniform(0.7, 1), random.uniform(0.7, 1), 0)
        gap = 3
        win_height = random.randint(2, 5)
        win_width = length - 10
        lights(t, xpos + 5, ypos, light_height, light_length, light_color, gap, win_height, win_width)




'''

System Process

'''

t.hideturtle()
t.speed(0)
window_sys(win)

'''

Background

'''

background_gradient(t, win)

moon(t, 0, 200)

skyline(t)

'''

background towers

'''


city_skyline(t, 30)


'''

Foreground

'''

foregroud(t)
foreground_shadows(t)

win.mainloop()