 
def draw_spiral(turtle, sides, dir_of_rot, degree_of_rot, rgb_start, rgb_end):


    ### Turtle Window Configuration
    turtle.colormode(255)
    turtle.bgcolor("black")
    ### Turtle Pen Setup
    t = turtle.Pen()
    t.speed(0)
    t.hideturtle()


    ### Spiral Creation ------------------

    x = [0,0,0]  # Intialize the rgb vector

    r, g, b = x[0], x[1], x[2] = rgb_start
    end_r, end_g, end_b = rgb_end

    numloops = 360

    # Use (numloops - 1) so the rgb end is arrived at
    # in the penultimate loop since the
    # last loop rgb values are not used
    Rinterval = (end_r - r)/(numloops - 1)
    Ginterval = (end_g - g)/(numloops - 1)
    Binterval = (end_b - b)/(numloops - 1)
    

    # Drawing loop
    for i in range(1, numloops+1):
        t.pencolor(r, g, b)
        t.forward(i * 3/sides + i)
        # degrees for a corner turn + 1 to make it spiral
        if dir_of_rot == 'right':
            t.right(360/sides + degree_of_rot)
        else:
            t.left(360/sides + degree_of_rot)
        t.width(i*sides/200)
        x[0] += Rinterval
        x[1] += Ginterval
        x[2] += Binterval

        r, g, b = int(x[0]), int(x[1]), int(x[2])

        # Note: the last rgb tuple is not used in the drawing
        print(r, g, b)       # For color performance analysis

    # Draw half a leg to finish inside the spiral
    # to hide ending
    t.forward( ( (numloops+1) * 3/sides + (numloops+1) )/2 )


    turtle.done()
