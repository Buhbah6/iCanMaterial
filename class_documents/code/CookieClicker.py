import turtle
import time

def clicked(x, y):
    global clicks, cookiePen
    clicks += 1
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

def createPen(colour):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color(colour)
    pen.penup()
    return pen

def main():
    wn = turtle.Screen()
    wn.title("Cookie Clicker")
    wn.bgcolor("black")

    wn.register_shape("[Enter Your Cookie Image Path Here]")
    wn.register_shape("[Enter Your Grandma Image Path Here]")

    cookie = turtle.Turtle()
    cookie.goto(-200, 0)
    cookie.shape("[Enter Your Cookie Image Path Here]")
    cookie.speed(0)

    clicks = 0
    clicksPerSecond = 0

    cookiePen = createPen("white")
    cookiePen.goto(-200, 300)
    cookiePen.write(f"Clicks: {clicks}", align="center", font=("Courier", 32, "normal"))

    cpsPen = createPen("white")
    cpsPen.goto(200, 300)
    cpsPen.write(f"CPS: {clicksPerSecond}", align="center", font=("Courier", 32, "normal"))

    grandma = turtle.Turtle()
    grandma.goto(200, 0)
    grandma.shape("[Enter Your Grandma Image Path Here]")
    grandma.speed(0)

    cookie.onclick(clicked)
    grandma.onclick(gClicked)

    while True:
        cookie.onclick(clicked)
        grandma.onclick(gClicked)
        clicks += clicksPerSecond
        cookiePen.clear()
        cookiePen.write(f"Clicks: {clicks}", align="center", font=("Courier", 32, "normal"))
        wn.update()
        time.sleep(1)

    wn.mainloop()
    
main()