import turtle

cur = turtle.Turtle()
cur.speed(0)
cur.pencolor("green")


win = turtle.Screen()
win.bgcolor("black")
win.title("Virus by Aman Programmer")
frwrd = 0
rght = 0
cur.up()
cur.goto(0, 200)
cur.down()
while (True):
    cur.forward(frwrd)
    cur.right(rght)
    frwrd+=3
    rght+=1
    if rght == 200:
        break


turtle.exitonclick()
