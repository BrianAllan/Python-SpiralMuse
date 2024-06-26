
import Config

def draw_spiral(turtle, sides, dir_of_rot, degree_of_rot, numloops, rgb_list, scale):

    t = Config.turtle_config(turtle)

    
    # Drawing loop
    for i in range(0, numloops):
        t.pencolor(rgb_list[i])
        side_length = (6 * i/sides + 90/sides**2) * scale
        t.forward(side_length)

        if dir_of_rot == 'right':
            # degrees for a corner turn + degree_of_rot to make it spiral
            t.right(360/sides + degree_of_rot)
        else:
            t.left(360/sides + degree_of_rot)
        # For 360 loops, width ranges from...
        #side_width = (i + 90)/90       # 0 to 5
        #side_width = (i + 180)/180      # 0 to 3
        side_width = (i + 360)/360     # 0 to 2
        t.width(side_width)

    # Draw half a leg to finish inside the spiral
    # to hide ending
    t.forward( side_length/2 )


    turtle.done()

########################################################
#### For Testing
    
##import turtle
##import Colorpaths
##
##counter = 0
##
### Engage turtle drawing program
##if counter == 0:
##    ### Turtle Window Setup
##    turtle.setup(width=1280, height=960)
##else:                             # Skips clear on 1st iteration
##    turtle.Screen().clear()       # Deletes all drawings and turtles
##counter += 1
##
##
##numloops = 360
##sides = 3
##dir_of_rot = 'left'
##degree_of_rot = 1
##rgb_start = (255, 255, 255)
##rgb_end = (0, 0, 255)
##rgb_order = 'rgb'
##
##scale = 1
##
##path = 'manhattan'
##
##if path == 'straightline':
##    rgb_list = Colorpaths.straightline(numloops, rgb_start, rgb_end)
##elif path == 'manhattan':
##    rgb_list = Colorpaths.Manhattan(numloops, rgb_start, rgb_end, rgb_order)
##else:
##    pass
##
##draw_spiral(turtle, sides, dir_of_rot, degree_of_rot, numloops, rgb_list, scale)
##
