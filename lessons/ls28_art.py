from turtle import Turtle, done


TRUNK = 100.0
UP = 90.0

t: Turtle = Turtle()


def tree(x: float, y: float) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    branch(TRUNK, UP)


def branch(length: float, angle: float) -> None:
    t.setheading(angle)
    t.forward(length)
    if length < 3:
        ... # Do nothing
    else:
        branch(length * 0.6, angle + 25)
        branch(length * 0.65, angle - 20)
    t.setheading(angle + 180)


if __name__ == "__main__":
    t.speed(5)
    t.getscreen().tracer(0, 0)
    t.getscreen().setup(width = 0.5, height = 0.5, startx = 1180, starty = 140)
    tree(0, 0)
    done()