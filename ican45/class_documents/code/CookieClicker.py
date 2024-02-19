import turtle
import time
import threading
import warnings 

warnings.filterwarnings('ignore') 

def clicked(x, y):
    global clicks, clicksPerClick, cookiePen
    clicks += clicksPerClick
    cookiePen.clear()
    cookiePen.write(f"Clicks: {clicks}", align="center", font=("Courier", 32, "normal"))

def gClicked(x, y):
    global clicks, clicksPerSecond, cookiePen, cpsPen
    if clicks >= 10:
        clicks -= 10
        clicksPerSecond += 1
        cookiePen.clear()
        cookiePen.write(f"Clicks: {clicks}", align="center", font=("Courier", 32, "normal"))
        cpsPen.clear()
        cpsPen.write(f"CPS: {clicksPerSecond}", align="center", font=("Courier", 32, "normal"))

def cursorClicked(x, y):
    global clicksPerClick, cpcPen, cookiePen, clicks
    if clicks >= 100:
        clicks -= 100
        clicksPerClick += 1
        cookiePen.clear()
        cookiePen.write(f"Clicks: {clicks}", align="center", font=("Courier", 32, "normal"))
        cpcPen.clear()
        cpcPen.write(f"Clicks Per Click: {clicksPerClick}", align="center", font=("Courier", 32, "normal"))

def createPen(colour):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color(colour)
    pen.penup()
    return pen

def runAutoClick():
    global clicks, cookiePen, wn
    while True:
        clicks += clicksPerSecond
        cookiePen.clear()
        cookiePen.write(f"Clicks: {clicks}", align="center", font=("Courier", 32, "normal"))
        wn.update()
        time.sleep(1)

wn = turtle.Screen()
wn.screensize(800, 800)
wn.title("Cookie Clicker")
wn.bgcolor("black")

wn.register_shape("C:\\Users\\there\\Downloads\\cookie.gif")
wn.register_shape("C:\\Users\\there\\Downloads\\grandma.gif")
wn.register_shape("C:\\Users\\there\\Downloads\\cursor.gif")

cookie = turtle.Turtle()
cookie.goto(0, 0)
cookie.shape("C:\\Users\\there\\Downloads\\cookie.gif")
cookie.speed(0)

clicks = 0
clicksPerSecond = 0
clicksPerClick = 1

cookiePen = createPen("white")
cookiePen.goto(0, 300)
cookiePen.write(f"Clicks: {clicks}", align="center", font=("Courier", 32, "normal"))

cpsPen = createPen("white")
cpsPen.goto(400, 300)
cpsPen.write(f"CPS: {clicksPerSecond}", align="center", font=("Courier", 32, "normal"))

cpcPen = createPen("white")
cpcPen.goto(-400, 300)
cpcPen.write(f"Clicks Per Click: {clicksPerClick}", align="center", font=("Courier", 32, "normal"))

grandma = turtle.Turtle()
grandma.goto(400, 0)
grandma.shape("C:\\Users\\there\\Downloads\\grandma.gif")
grandma.speed(0)

cursor = turtle.Turtle()
cursor.goto(-400, 0)
cursor.shape("C:\\Users\\there\\Downloads\\cursor.gif")
cursor.speed(0)

cookie.onclick(clicked)
grandma.onclick(gClicked)
cursor.onclick(cursorClicked)

t1 = threading.Thread(target=runAutoClick, name='t1')
t1.start()

wn.mainloop()
    