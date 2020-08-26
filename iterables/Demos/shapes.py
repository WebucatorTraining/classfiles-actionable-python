import turtle

def main():
    line = ((-40, 10), (-80, 170))
    triangle = ((140, 200), (180, 270), (335, 180))
    rectangle = ((40, 100), (80, 170), (235, 80), (195, 10))
    
    t = turtle.Turtle()

    t.up()
    t.setpos(line[0])
    t.down()

    t.goto(line[1])

    t.up()
    t.setpos(triangle[0])
    t.down()

    t.goto(triangle[1])
    t.goto(triangle[2])
    t.goto(triangle[0])

    t.up()
    t.setpos(rectangle[0])
    t.down()

    t.goto(rectangle[1])
    t.goto(rectangle[2])
    t.goto(rectangle[3])
    t.goto(rectangle[0])

    turtle.done()

main()