
import turtle
import tkinter as tk
import tkinter.messagebox as box
from tkinter.font import Font
from tkinter import ttk
import random



### Base Color Choices
colors = {
    'light gray': (211, 211, 211),
    'light steel blue': (176, 196, 222),
    'medium blue': (0, 0, 205),
    'royal blue': (65, 105, 225),
    'deep sky blue': (0, 191, 255),
    'cyan': (0, 255, 255),
    'turquoise': (64, 224, 208),
    'teal': (0, 128, 128),
    'aquamarine': (127, 255, 212),
    'sea green': (46, 139, 87),
    'spring green': (0, 255, 127),
    'forest green': (34, 139, 34),
    'lime': (0, 255, 0),
    'olive drab': (107, 142, 35),
    'dark khaki': (189, 183, 107),
    'khaki': (240, 230, 140),
    'yellow': (255, 255, 0),
    'gold': (255, 215, 0),
    'tan': (210, 180, 140),
    'saddle brown': (139, 69, 19),
    'orange': (255, 165, 0),
    'firebrick': (178, 34, 34),
    'maroon': (128, 0, 0),
    'light salmon': (255, 160, 122),
    'tomato': (255, 99, 71),
    'crimson': (220, 20, 60),
    'light coral': (240, 128, 128),
    'pink': (255, 192, 203),
    'hot pink': (255, 105, 180),
    'medium violet red': (199, 21, 133),
    'violet': (238, 130, 238),
    'magenta': (255, 0, 255),
    'orchid': (218, 112, 214),
    'dark violet': (138, 0, 211),
    'medium purple': (147, 112, 219)
    }


bgcolor1 = 'gray85'
bgcolor2 = 'powder blue'
wincolor = 'azure2'



##### Turtle Window ##########################

def draw_spiral(sides, dir_of_rot, degree_of_rot, color_start, color_end):

    ### Turtle Configuration -------------
    turtle.colormode(255)
    turtle.setup(width=1280, height=960)
    t = turtle.Pen()
    t.speed(0)
    turtle.bgcolor("black")
    t.hideturtle()



    ### Spiral Creation ------------------

    x = [0,0,0]  # Intialize the rgb vector

    r, g, b = x[0], x[1], x[2] = colors[color_start]
    end_r, end_g, end_b = colors[color_end]

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




####### tkinter window #####################


## tkinter Spiral Control window configuration

window = tk.Tk()
window.title('Spiral Muse - Spiral Control')
window.geometry('1050x800')
window.configure(bg=wincolor)

# tkinter font configuration
Arial10 = Font(family="Arial", size=10, weight="normal")
Arial11 = Font(family="Arial", size=11, weight="normal")
Arial12 = Font(family="Arial", size=12, weight="normal")
Arial20 = Font(family="Arial", size=20, weight="bold")
Verd10 = Font(family="Verdana", size=10, weight="normal")
Verd12 = Font(family="Verdana", size=12, weight="normal")
Verd14 = Font(family="Verdana", size=14, weight="bold")
Verd20 = Font(family="Verdana", size=20, weight="bold")

# Change message box font to Verdana
window.option_add('*Dialog.msg.font', 'Verdana 12')  


##### Description Frame -----------------------

frame_descript = tk.Frame(window,
                          bg=bgcolor2,
                          padx=10,
                          pady=5,
                          relief=tk.RIDGE,
                          borderwidth=5
                          )
frame_descript.grid(row=0,
                    column=0,
                    padx=10,
                    pady=0,
                    sticky=tk.N
                    )

# Create label as frame title
tk.Label(frame_descript,
         text='Spiral Muse',
         bg=bgcolor2,
         height=1,      # height in lines, not pixels
         pady=5,
         font=Verd20
         ).grid(row=0, columnspan=2)



# Create and place 1st part of description
description1 = (
    'Generate colored spiral designs (against a black background) '
    'starting with a base polygonal shape (triangle, square, '
    'pentagon, etc.) and a base color. The base polygonal shape '
    'is specified by the number of sides (3, 4, 5,...up to 10).'
)
mess_descript1 = tk.Message(master=frame_descript,
                            text=description1,
                            bg=bgcolor2,
                            width=580,
                            padx=5,
                            font=Verd10
                            )
mess_descript1.grid(row=1, columnspan=2)

# Create and place spiral image
img = tk.PhotoImage(file = 'Green_Color_Spiral.png')
small_img = tk.PhotoImage.subsample(img, x=5, y=5)
tk.Label(frame_descript,
         image=small_img,
         bg=bgcolor2
         ).grid(row=2, column=0)


# Create 2nd part of description
description2 = (
    'The color can be allowed to DRIFT away from the base '
    'color as the spiral twists and expands outward, '
    'creating an unfolding effect. '
    'This can be set using an integer number '
    'from 2 to 8, where 2 represents a lot of drift and 8 '
    'represents only a little. Think of this number as the degree '
    'of color STABILITY, the opposite of DRIFT. '
    'Regardless, a little amount of random variation is automatically '
    'added to the color, creating an organic look. '
)
mess_descript2 = tk.Message(master=frame_descript,
                            text=description2,
                            bg=bgcolor2,
                            width=350,
                            padx=5,
                            font=Verd10
                            )
mess_descript2.grid(row=2, column=1)



##### Parameter Selection Frame ----------------------

param_sel_textwidth = 560

# Create frame
frame_params = tk.Frame(window, 
                       bg=bgcolor2,
                       padx=10,
                       pady=5,
                       relief=tk.RIDGE,
                       borderwidth=5
                       )
frame_params.grid(row=1,
                 column=0,
                 padx=10,
                 pady=0,
                 sticky=tk.N
                 )

## Sides Section

sides = 3           # Default value

# Sides text message
sidestext = ('How many sides would you like for the base polygon? '
               'Select a number from 3 to 10.'
)
tk.Message(master=frame_params,
                   text=sidestext,
                   bg=bgcolor2,
                   width=param_sel_textwidth,
                   padx=5,
                   font=Verd10
                   ).grid(row=0, columnspan=2)

# Create Label
tk.Label(frame_params,
         text='Base Polygon Sides',
         bg=bgcolor2,
         height=1,      # height in lines, not pixels
         padx=10,
         pady=5,
         font=Verd14
         ).grid(row=1, column=0, sticky=tk.E)

# Create Sides Combobox
n = tk.StringVar()

sides_combo = ttk.Combobox(frame_params,
                           width=2,
                           textvariable=n,
                           values=[i for i in range(3, 11)],
                           font=Verd12
                           )
sides_combo.grid(row=1, column=1, sticky='W')

sides_combo.current(0)



## Rotation Section
direction = tk.StringVar()         # construct string var
dir_of_rot = 'left'         # default value
degree_of_rot = 1           # default value

# Rotation text message
rottext = (
    'Select the direction of rotation, '
    'either \'left\' or \'right\', and '
    'the degree of rotation, an integer '
    'number from 1 to 20.'
)
tk.Message(master=frame_params,
                      text=rottext,
                      bg=bgcolor2,
                      width=param_sel_textwidth,
                      padx=5,
                      font=Verd10
                      ).grid(row=4, columnspan=2)

# Create label as title
tk.Label(frame_params,
         text='Direction of Rotation',
         bg=bgcolor2,
         height=1,      # height in lines, not in pixels
         padx=10,
         pady=5,
         font=Verd14
         ).grid(row=5, column=0, sticky=tk.E)
tk.Label(frame_params,
         text='Degree of Rotation',
         bg=bgcolor2,
         height=1,      # height in lines, not in pixels
         padx=10,
         pady=5,
         font=Verd14
         ).grid(row=6, column=0, sticky=tk.E)


# Create Direction of Rotation Radio Buttons
frame_radio = tk.Frame(frame_params, 
                       bg=bgcolor2,
                       padx=10,
                       pady=0,
                       borderwidth=0
                       )
radio_1 = tk.Radiobutton(frame_radio,
                         text='Left',
                         font=Verd12,
                         variable = direction,
                         value='left',
                         bg=bgcolor2,
                         activebackground='cyan',
                         borderwidth=0
                         )
radio_2 = tk.Radiobutton(frame_radio,
                         text='Right',
                         font=Verd12,
                         variable = direction,
                         value='right',
                         bg=bgcolor2,
                         activebackground='cyan',
                         borderwidth=0
                         )
radio_1.select()
frame_radio.grid(row=5, column=1, sticky=tk.W)
radio_1.pack(side=tk.LEFT)
radio_2.pack(side=tk.RIGHT)


# Create Degree of Rotation Combobox

deg = tk.StringVar()

degree_combo = ttk.Combobox(frame_params,
                           width=2,
                           textvariable=deg,
                           values=[i for i in range(1, 21)],
                           font=Verd12
                           )
degree_combo.grid(row=6, column=1, sticky='W')

degree_combo.current(0)




##### Color Select Frame ------------------------------------

# Create frame
frame_colorselect = tk.Frame(window,
                            bg=bgcolor2,
                            padx=10,
                            pady=5,
                            relief=tk.RIDGE,
                            borderwidth=5
                            )
frame_colorselect.grid(row=0,
                       column=1,
                       pady=0
                       )

## Color Selection Section
color_start = 'cyan'
color_end = 'magenta'

coltext = (
'Select the inner start color and '
'the outer end color of the spiral.'
)
tk.Message(master=frame_colorselect,
           text=coltext,
           bg=bgcolor2,
           width=param_sel_textwidth,
           padx=5,
           font=Verd10
).grid(row=0, columnspan=2)

# Create label as title
tk.Label(frame_colorselect,
         text='Inner Start Color',
         bg=bgcolor2,
         height=1,
         padx=10,
         pady=5,
         font=Verd14
).grid(row=1, column=0, sticky=tk.E)
tk.Label(frame_colorselect,
         text='Outer End Color',
         bg=bgcolor2,
         height=1,
         padx=10,
         pady=5,
         font=Verd14
).grid(row=3, column=0, sticky=tk.E)

# Create Start Color Entry
start_entry = tk.Entry(frame_colorselect, width=17, font=Verd12)
start_entry.insert(0, str(color_start))
start_entry.grid(row=2, column=1, padx=(0,20), sticky=tk.W)

# Create function to get Start Color
# and print it in the entry box

def start_color_select():
    # Getting color
    color_start = colorstrip.get(colorstrip.curselection()).strip()
    # Printing in entry box
    start_entry.delete(0, tk.END)
    start_entry.insert(0, str(color_start))


# Create Start Color Button
tk.Button(frame_colorselect,
          text='Select',
          command=start_color_select,
          font=Verd12
          ).grid(row=2, column=0, padx=20)



# Create End Color Entry
end_entry = tk.Entry(frame_colorselect, width=17, font=Verd12)
end_entry.insert(0, str(color_end))
end_entry.grid(row=4, column=1, padx=(0,20), sticky=tk.W)

# Create function to get End Color
# and print it in the entry box

def end_color_select():
    # Getting color
    color_end = colorstrip.get(colorstrip.curselection()).strip()
    # Printing in entry box
    end_entry.delete(0, tk.END)
    end_entry.insert(0, str(color_end))


# Create End Color Button
tk.Button(frame_colorselect,
          text='Select',
          command=end_color_select,
          font=Verd12
          ).grid(row=4, column=0, padx=20)




##### Color Strip Frame ------------------------------------

frame_colorstrip = tk.Frame(window,
                            bg=bgcolor2,
                            padx=10,
                            pady=5,
                            relief=tk.RIDGE,
                            borderwidth=5
                            )
frame_colorstrip.grid(row=0,
                       column=2,
                       rowspan=3,
                       pady=0
                       )

# Create listbox
colorstrip = tk.Listbox(frame_colorstrip,
                     selectbackground='ghost white',
                     height=len(colors),
                     borderwidth=5,
                     font=Verd10,
                     # keep listbox selection from
                     # being deselected by other selections
                     exportselection=False    
                     )

# Add items to listbox
for i, key in enumerate(colors.keys()):
    colorstrip.insert(i, '  ' + key)
    colorstrip.itemconfig(i, bg=key)

# Select the last element as default
#colorstrip.select_set(len(colors) - 1)   
colorstrip.grid(row=0, column=0)



##### Proceed Frame -----------------------------------------

frame_proceed = tk.Frame(window,
                         bg=bgcolor2,
                         padx=10,
                         pady=5,
                         relief=tk.RIDGE,
                         borderwidth=5)
frame_proceed.grid(row=1,
                   column=1,
                   pady=0,
                   sticky=tk.N
                   )

tk.Label(frame_proceed,
         text='Proceed with Drawing?',
         bg=bgcolor2,
         height=1,     # height in lines, not pixels
         padx=0,
         pady=5,
         font=Verd14
         ).grid(row=0, column=0)



### Proceed Function
counter = 0

def proceed_submit():
    global sides
    global dir_of_rot
    global degree_of_rot
    global counter
    global color_start
    global color_end
    

    if counter > 0:                   # Skips clear on 1st iteration
        turtle.Screen().clear()       # Deletes all drawings and turtles
    counter += 1

    # Exception handling for sides
    sides = sides_combo.get()
    if not sides.isdigit():
        box.showwarning('', 'The sides entry must be an integer.  Select again.')
        return
    sides = int(sides)
    if sides < 3 or sides > 10:
        box.showwarning('', 'The selected number of sides is out of range.  Select again.')
        return


    # Exception handling for direction of rotation
    dir_of_rot = direction.get()
    if dir_of_rot == 'left':
        radio_1.select()
    elif dir_of_rot == 'right':
        radio_2.select()
    else:
        box.showwarning(title='Selections',
                        message=('The Direction of Rotation entry must be either '
                                '\'left\' or \'right\'.  Select again.')
                        )
        return

    # Exception handling for degree of rotation
    degree_of_rot = degree_combo.get()
    if not degree_of_rot.isdigit():
        box.showwarning(title='Selections',
                        message='The Degree of Rotation entry must be an integer.  Select again.')
        return
    degree_of_rot = int(degree_of_rot)
    if degree_of_rot < 1 or degree_of_rot > 20:
        box.showwarning(title='Selections',
                        message='The Degree of Rotation is out of range.  Select again.')
        return

    # Exception handing for start and end color choices
    color_start = start_entry.get()
    color_end = end_entry.get()

    mess_proceed = f'''Your Selection is...\t\t\t
Sides:\t\t{sides}
Direction of Rotation:\t{dir_of_rot}
Degree of Rotation:\t{degree_of_rot}
Start Color:\t{color_start}
End Color:\t{color_end}
'''
    
    box.showinfo('', mess_proceed)
    draw_spiral(sides, dir_of_rot, degree_of_rot, color_start, color_end)

### End Proceed Function

                         
tk.Button(frame_proceed,
          text='Proceed',
          command=proceed_submit,
          font=Verd12
          ).grid(row=0, column=1, padx=20)

##### End Proceed Frame -----------------------------------------




##### Window mainloop ------------------------------------------

window.mainloop()





