import colorgram as cg


def main():
    # colors = cg.extract(
    #     r'D:\TrinhHan\HocTap\Projects\100daysPython\HirstPainting\picture.jpg', 22)
    # print(list(map(lambda x: (x.rgb.r, x.rgb.g, x.rgb.b), colors)))
    my_color = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233),
                (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23)]
    from turtle import Turtle, Screen
    tim = Turtle()

    screen = Screen()
    screen.screensize(1000, 1000)
    screen.colormode(255)
    tim.penup()
    tim.speed("fastest")
    tim.hideturtle()

    hirst_painting(20, 20, 25, 10, my_color, tim)

    screen.exitonclick()


def hirst_painting(rows, cols, distance, dotsize, lst_color, turtle):
    import random
    (x, y) = (-cols*distance/2, -rows*distance/2)
    for i in range(rows):
        turtle.setposition(x, y + i*distance)
        for j in range(cols):
            turtle.dot(dotsize, random.choice(lst_color))
            turtle.forward(distance)


if __name__ == '__main__':
    main()
