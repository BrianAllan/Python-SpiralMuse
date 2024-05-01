 
def draw_spiral(turtle, sides, dir_of_rot, degree_of_rot, rgb_start, rgb_end, rgb_order):

    ### Turtle Window Configuration
    turtle.colormode(255)
    turtle.bgcolor("black")
    ### Turtle Pen Setup
    t = turtle.Pen()
    t.speed(0)
    t.hideturtle()

    ### Color Evolution Initialization -----------------

    mapping = {'rgb': '012',
               'rbg': '021',
               'grb': '102',
               'gbr': '120',
               'brg': '201',
               'bgr': '210'}

    # Create indices for ijk space corresponding to rgb space
    i = int(mapping[rgb_order][0])
    j = int(mapping[rgb_order][1])
    k = int(mapping[rgb_order][2])

    x = [0,0,0]  # Initialize the rgb vector
    r, g, b = x[0], x[1], x[2] = rgb_start
    # Create corresponding ijk vectors
    # for i, j, k ordered path through rgb space
    z = [x[i], x[j], x[k]]     
    ijk_end = [rgb_end[i], rgb_end[j], rgb_end[k]]
     

    numloops = 360
    
    # Calculate Manhattan distance (Mdist) through RGB color space
    # and step size for each iteration (Minterval)
    Mdist = (
            abs(rgb_end[0] - r) +
            abs(rgb_end[1] - g) + 
            abs(rgb_end[2] - b)
            )
    print(f'Mdist is: {Mdist}')
    Minterval = Mdist/numloops
    print(f'Minterval is: {Minterval}')

    ### Spiral Creation ------------------

    # Drawing loop
    for m in range(1, numloops+1):
        t.pencolor(r, g, b)
        t.forward(m * 3/sides + m)
        # degrees for a corner turn + 1 to make it spiral
        if dir_of_rot == 'right':
            t.right(360/sides + degree_of_rot)
        else:
            t.left(360/sides + degree_of_rot)
        t.width(m*sides/200)

        # Evolve the ijk vector --> z
        if z[0] - ijk_end[0] > Minterval/2:
            z[0] -= Minterval
        elif ijk_end[0] - z[0] > Minterval/2:
            z[0] += Minterval
        elif z[1] - ijk_end[1] > Minterval/2:
            z[1] -= Minterval
        elif ijk_end[1] - z[1] > Minterval/2:
            z[1] += Minterval
        elif z[2] - ijk_end[2] > Minterval/2:
            z[2] -= Minterval
        elif ijk_end[2] - z[2] > Minterval/2:
            z[2] += Minterval
        else:
            pass

        # Update the rgb vector --> x
        x[i], x[j], x[k] = z[0], z[1], z[2]

        # Obtain integer values from the rgb vector
        r, g, b = int(x[0]), int(x[1]), int(x[2])  

        print(r, g, b)       # For color performance analysis

    # Draw half a leg to finish inside the spiral
    # to hide ending
    t.forward( ( (numloops+1) * 3/sides + (numloops+1) )/2 )


    turtle.done()

