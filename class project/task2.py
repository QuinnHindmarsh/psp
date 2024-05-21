import turtle


def drawStar(size=100):
    for num in range(5):
        turtle.forward(size)
        turtle.left(216)

drawStar()
drawStar(100)
drawStar(250)