
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
                    padx=(10,0),
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



##### Sides and Rotation Frame ----------------------

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
                 padx=(10,0),
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
radio_L = tk.Radiobutton(frame_radio,
                         text='Left',
                         font=Verd12,
                         variable=direction,
                         value='left',
                         bg=bgcolor2,
                         activebackground='cyan',
                         borderwidth=0
                         )
radio_R = tk.Radiobutton(frame_radio,
                         text='Right',
                         font=Verd12,
                         variable=direction,
                         value='right',
                         bg=bgcolor2,
                         activebackground='cyan',
                         borderwidth=0
                         )
radio_L.select()
frame_radio.grid(row=5, column=1, sticky=tk.W)
radio_L.pack(side=tk.LEFT)
radio_R.pack(side=tk.RIGHT)


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




##### Color Select Frame ################################

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

### Color Selection Introduction ................
color_start = 'cyan'
color_end = 'magenta'

coltext = (
'Select the inner start color and '
'the outer end color of the spiral.'
)
mess_color_intro = tk.Message(master=frame_colorselect,
           text=coltext,
           bg=bgcolor2,
           width=param_sel_textwidth,
           padx=0,
           font=Verd10
)


### Create function to force widget level RGB validation ................

def validate_RGB(result, insertion, text, index):
    if result:
        print(result, insertion, text, index)
        if result.isdigit() and 0 <= int(result) <= 255 and int(index) < 3:
            return True
        else:
            return False
    else:
        return True

# Register the function, producing a Tcl wrapper around the Python function
RGB_validation = window.register(validate_RGB)

### .............................................



### Start Color Section ...............

# Function to get Start Color
# and print it in the entry box
def start_color_select():
    # Getting color
    color_start = colorstrip.get(colorstrip.curselection()).strip()

    if start_color_source.get() == 'strip':
        # Printing in entry box
        start_strip_entry.delete(0, tk.END)
        start_strip_entry.insert(0, str(color_start))
        # Printing in RGB entry boxes
        start_r_entry.delete(0, tk.END)
        start_r_entry.insert(0, str(colors[color_start][0]))
        start_g_entry.delete(0, tk.END)
        start_g_entry.insert(0, str(colors[color_start][1]))
        start_b_entry.delete(0, tk.END)
        start_b_entry.insert(0, str(colors[color_start][2]))
    else:
        start_strip_entry.delete(0, tk.END)

def erase_start_strip_entry():
    start_strip_entry.delete(0, tk.END)

def erase_RGB_entries():
    start_r_entry.delete(0, tk.END)
    start_g_entry.delete(0, tk.END)
    start_b_entry.delete(0, tk.END)


# Start: Color Label
label_inner_color = tk.Label(frame_colorselect,
         text='Inner Start Color',
         bg=bgcolor2,
         height=1,
         padx=0,
         pady=5,
         font=Verd14
)

# Start: Radiobutton to Select from Color Strip
start_color_source = tk.StringVar()

radio_start_from_strip = tk.Radiobutton(
                        frame_colorselect,
                        text='Select from color strip',
                        font=Verd12,
                        variable=start_color_source,
                        value='strip',
                        bg=bgcolor2,
                        activebackground='cyan',
                        command=erase_RGB_entries
                        )

# Set radiobutton default
radio_start_from_strip.select()

# Start: Color Strip Entry
start_strip_entry = tk.Entry(frame_colorselect, width=17, font=Verd12)
start_strip_entry.insert(0, str(color_start))
    

# Start: Color Select Button
btn_start_select = tk.Button(frame_colorselect,
                  text='Select',
                  command=start_color_select,
                  font=Verd12
                  )

# Start: Radiobutton to Select from RGB values
radio_start_from_RGB = tk.Radiobutton(
                        frame_colorselect,
                        text='Specify RGB values (0 - 255)',
                        font=Verd12,
                        variable=start_color_source,
                        value='rgb',
                        bg=bgcolor2,
                        activebackground='cyan',
                        command=erase_start_strip_entry
                        )


### Start: RGB frame for RGB entries ..................
frame_rgb_start = tk.Frame(frame_colorselect,
                           bg=bgcolor2)

# Creation
start_r_label = tk.Label(frame_rgb_start, width=1, font=Verd12,
                         text='R', bg=bgcolor2)
start_r_entry = tk.Entry(frame_rgb_start, width=3, font=Verd12,
                         # Callback with registered function +
                         # Sends to the function the intended result (%P),
                         # whether insertion or deletion (%d),
                         # the text to insert (%S), and the index of the attempted
                         # insertion (%i)
                         validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
                         # Validates whenever a keystroke changes the widget's contents
                         validate='key')
start_g_label = tk.Label(frame_rgb_start, width=1, font=Verd12,
                         text='G', bg=bgcolor2)
start_g_entry = tk.Entry(frame_rgb_start, width=3, font=Verd12,
                         # Callback with registered function +
                         # Sends to the function the intended result (%P),
                         # whether insertion or deletion (%d),
                         # the text to insert (%S), and the index of the attempted
                         # insertion (%i)
                         validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
                         # Validates whenever a keystroke changes the widget's contents
                         validate='key')
start_b_label = tk.Label(frame_rgb_start, width=1, font=Verd12,
                         text='B', bg=bgcolor2)
start_b_entry = tk.Entry(frame_rgb_start, width=3, font=Verd12,
                         # Callback with registered function +
                         # Sends to the function the intended result (%P),
                         # whether insertion or deletion (%d),
                         # the text to insert (%S), and the index of the attempted
                         # insertion (%i)
                         validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
                         # Validates whenever a keystroke changes the widget's contents
                         validate='key')

# Placement in frame_rgb_start
start_r_label.grid(row=0, column=0)
start_r_entry.grid(row=0, column=1)
start_g_label.grid(row=0, column=2)
start_g_entry.grid(row=0, column=3)
start_b_label.grid(row=0, column=4)
start_b_entry.grid(row=0, column=5)

# Placement in frame_colorselect
mess_color_intro.grid(row=0, columnspan=3, sticky=tk.W)
label_inner_color.grid(row=1, column=0, sticky=tk.W)
radio_start_from_strip.grid(row=2, column=0, sticky=tk.W)
start_strip_entry.grid(row=2, column=1, padx=5, sticky=tk.W)
btn_start_select.grid(row=2, column=2, padx=5)
radio_start_from_RGB.grid(row=3, column=0, sticky=tk.W)
frame_rgb_start.grid(row=3, column=1)



### End Color Section ...............

# Function to get End Color
# and print it in the entry box
def end_color_select():
    # Getting color
    color_end = colorstrip.get(colorstrip.curselection()).strip()

    if end_color_source.get() == 'strip':
        # Printing in entry box
        end_strip_entry.delete(0, tk.END)
        end_strip_entry.insert(0, str(color_end))
        # Printing in RGB entry boxes
        end_r_entry.delete(0, tk.END)
        end_r_entry.insert(0, str(colors[color_end][0]))
        end_g_entry.delete(0, tk.END)
        end_g_entry.insert(0, str(colors[color_end][1]))
        end_b_entry.delete(0, tk.END)
        end_b_entry.insert(0, str(colors[color_end][2]))
    else:
        end_strip_entry.delete(0, tk.END)

def erase_end_strip_entry():
    end_strip_entry.delete(0, tk.END)

def erase_RGB_entries():
    end_r_entry.delete(0, tk.END)
    end_g_entry.delete(0, tk.END)
    end_b_entry.delete(0, tk.END)


# End: Color Label
label_outer_color = tk.Label(frame_colorselect,
         text='Outer End Color',
         bg=bgcolor2,
         height=1,
         padx=0,
         pady=5,
         font=Verd14
)

# End: Radiobutton to Select from Color Strip
end_color_source = tk.StringVar()

radio_end_from_strip = tk.Radiobutton(
                        frame_colorselect,
                        text='Select from color strip',
                        font=Verd12,
                        variable=end_color_source,
                        value='strip',
                        bg=bgcolor2,
                        activebackground='cyan',
                        command=erase_RGB_entries
                        )

# Set radiobutton default
radio_end_from_strip.select()

# End: Color Strip Entry
end_strip_entry = tk.Entry(frame_colorselect, width=17, font=Verd12)
end_strip_entry.insert(0, str(color_end))
    

# End: Color Select Button
btn_end_select = tk.Button(frame_colorselect,
                  text='Select',
                  command=end_color_select,
                  font=Verd12
                  )

# End: Radiobutton to Select from RGB values
radio_end_from_RGB = tk.Radiobutton(
                        frame_colorselect,
                        text='Specify RGB values (0 - 255)',
                        font=Verd12,
                        variable=end_color_source,
                        value='rgb',
                        bg=bgcolor2,
                        activebackground='cyan',
                        command=erase_end_strip_entry
                        )


### End: RGB frame for RGB entries ..................
frame_rgb_end = tk.Frame(frame_colorselect,
                           bg=bgcolor2)

# Creation
end_r_label = tk.Label(frame_rgb_end, width=1, font=Verd12,
                         text='R', bg=bgcolor2)
end_r_entry = tk.Entry(frame_rgb_end, width=3, font=Verd12,
                         # Callback with registered function +
                         # Sends to the function the intended result (%P),
                         # whether insertion or deletion (%d),
                         # the text to insert (%S), and the index of the attempted
                         # insertion (%i)
                         validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
                         # Validates whenever a keystroke changes the widget's contents
                         validate='key')
end_g_label = tk.Label(frame_rgb_end, width=1, font=Verd12,
                         text='G', bg=bgcolor2)
end_g_entry = tk.Entry(frame_rgb_end, width=3, font=Verd12,
                         # Callback with registered function +
                         # Sends to the function the intended result (%P),
                         # whether insertion or deletion (%d),
                         # the text to insert (%S), and the index of the attempted
                         # insertion (%i)
                         validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
                         # Validates whenever a keystroke changes the widget's contents
                         validate='key')
end_b_label = tk.Label(frame_rgb_end, width=1, font=Verd12,
                         text='B', bg=bgcolor2)
end_b_entry = tk.Entry(frame_rgb_end, width=3, font=Verd12,
                         # Callback with registered function +
                         # Sends to the function the intended result (%P),
                         # whether insertion or deletion (%d),
                         # the text to insert (%S), and the index of the attempted
                         # insertion (%i)
                         validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
                         # Validates whenever a keystroke changes the widget's contents
                         validate='key')

# Placement in frame_rgb_end
end_r_label.grid(row=0, column=0)
end_r_entry.grid(row=0, column=1)
end_g_label.grid(row=0, column=2)
end_g_entry.grid(row=0, column=3)
end_b_label.grid(row=0, column=4)
end_b_entry.grid(row=0, column=5)

# Placement in frame_colorselect
label_outer_color.grid(row=4, column=0, sticky=tk.W)
radio_end_from_strip.grid(row=5, column=0, sticky=tk.W)
end_strip_entry.grid(row=5, column=1, padx=5, sticky=tk.W)
btn_end_select.grid(row=5, column=2, padx=5)
radio_end_from_RGB.grid(row=6, column=0, sticky=tk.W)
frame_rgb_end.grid(row=6, column=1)





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
colorstrip.select_set(len(colors) - 1)   
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



### Proceed Function ###################
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

    sides = int(sides_combo.get())

    dir_of_rot = direction.get()

    degree_of_rot = int(degree_combo.get())

    color_start = start_strip_entry.get()
    color_end = end_strip_entry.get()

    mess_proceed = f'''Your Selection is...\t\t\t
Sides:\t\t{sides}
Direction of Rotation:\t{dir_of_rot}
Degree of Rotation:\t{degree_of_rot}
Start Color:\t{color_start}
End Color:\t{color_end}
'''
    box.showinfo('', mess_proceed)
    
    draw_spiral(sides, dir_of_rot, degree_of_rot, color_start, color_end)

### End Proceed Function #################

                         
tk.Button(frame_proceed,
          text='Proceed',
          command=proceed_submit,
          font=Verd12
          ).grid(row=0, column=1, padx=20)

##### End Proceed Frame -----------------------------------------




##### Window mainloop ------------------------------------------

window.mainloop()





