import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.level = 0

    def update(self):
        self.goto(-290, 275)
        self.clear()
        self.write("Level " + str(self.level), font=FONT)

    def stop(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
        turtle.done()
