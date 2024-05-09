
import turtle
import tkinter as tk
import tkinter.messagebox as box
from tkinter.font import Font
from tkinter import ttk
import Colorpaths
import Spiral
import RandomFunctions



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



####### tkinter window #####################


## tkinter Spiral Control window configuration

window = tk.Tk()
window.title('Spiral Muse - Spiral Control')
window.geometry('1400x700')
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

frame_descript = tk.Frame(
    window, bg=bgcolor2,
    padx=10, pady=5,
    relief=tk.RIDGE,
    borderwidth=5
)

# Create label as frame title
tk.Label(
    frame_descript,
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
mess_descript1 = tk.Message(
    master=frame_descript,
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
tk.Label(
    frame_descript,
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
mess_descript2 = tk.Message(
    master=frame_descript,
    text=description2,
    bg=bgcolor2,
    width=350,
    padx=5,
    font=Verd10
)
mess_descript2.grid(row=2, column=1)



##### Sides and Rotation Frame ----------------------

mess_textwidth = 560

# Create frame
frame_params = tk.Frame(
    window, bg=bgcolor2,
    padx=10, pady=5,
    relief=tk.RIDGE,
    borderwidth=5
)


## Sides Section


# Sides text message
sidestext = ('How many sides would you like for the base polygon? '
               'Select a number from 3 to 10.'
)
tk.Message(
    master=frame_params,
    text=sidestext,
    bg=bgcolor2,
    width=mess_textwidth,
    padx=5,
    font=Verd10
).grid(row=0, columnspan=2)

# Create Label
tk.Label(
    frame_params,
    text='Base Polygon Sides',
    bg=bgcolor2,
    height=1,      # height in lines, not pixels
    padx=10,
    pady=5,
    font=Verd14
).grid(row=1, column=0, sticky=tk.E)

# Create Sides Combobox
num_sides = tk.StringVar()

sides_combo = ttk.Combobox(
    frame_params,
    width=2,
    textvariable=num_sides,
    values=[i for i in range(2, 11)],
    font=Verd12
)
sides_combo.grid(row=1, column=1, sticky='W')

sides_combo.current(1)



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
tk.Message(
    master=frame_params,
    text=rottext,
    bg=bgcolor2,
    width=mess_textwidth,
    padx=5,
    font=Verd10
).grid(row=4, columnspan=2)

# Create label as title
tk.Label(
    frame_params,
    text='Direction of Rotation',
    bg=bgcolor2,
    height=1,      # height in lines, not in pixels
    padx=10, pady=5,
    font=Verd14
).grid(row=5, column=0, sticky=tk.E)
tk.Label(
    frame_params,
    text='Degree of Rotation',
    bg=bgcolor2,
    height=1,      # height in lines, not in pixels
    padx=10, pady=5,
    font=Verd14
).grid(row=6, column=0, sticky=tk.E)


# Create Direction of Rotation Radio Buttons
frame_radio = tk.Frame(
    frame_params, 
    bg=bgcolor2,
    padx=10, pady=0,
    borderwidth=0
)
radio_L = tk.Radiobutton(
    frame_radio,
    text='Left',
    font=Verd12,
    variable=direction,
    value='left',
    bg=bgcolor2,
    activebackground='cyan',
    borderwidth=0
)
radio_R = tk.Radiobutton(
    frame_radio,
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

degree_rot = tk.StringVar()

degree_combo = ttk.Combobox(
    frame_params,
    width=2,
    textvariable=degree_rot,
    values=[i for i in range(0, 21)],
    font=Verd12
)
degree_combo.grid(row=6, column=1, sticky='W')

degree_combo.current(1)




##### Color Select Frame ################################

# Create frame
frame_colorselect = tk.Frame(
    window,
    bg=bgcolor2,
    padx=10,
    pady=5,
    relief=tk.RIDGE,
    borderwidth=5
)


### Color Selection Introduction ................
color_start = 'cyan'
color_end = 'magenta'

coltext = (
'Select the inner start color and '
'the outer end color of the spiral.'
)
mess_color_intro = tk.Message(
    master=frame_colorselect,
    text=coltext,
    bg=bgcolor2,
    width=mess_textwidth,
    padx=0,
    font=Verd10
)


### Create function to force widget level RGB validation ................

def validate_RGB(result, insertion, text, index):
    
    if start_color_source.get() == 'strip':
        return True
    else:
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

def from_start_strip_selection():
    # Getting color
    color_start = colorstrip.get(colorstrip.curselection()).strip()
    # Printing in label
    start_text_var.set(color_start)
    start_strip_label['background'] = color_start
    # Enable RGB entry boxes
    start_r_entry.config(state='normal')
    start_g_entry.config(state='normal')
    start_b_entry.config(state='normal')
    # Printing in RGB entry boxes
    start_r_entry.delete(0, tk.END)
    start_r_entry.insert(0, str(colors[color_start][0]))
    start_g_entry.delete(0, tk.END)
    start_g_entry.insert(0, str(colors[color_start][1]))
    start_b_entry.delete(0, tk.END)
    start_b_entry.insert(0, str(colors[color_start][2]))
    # Disable RGB entry boxes
    start_r_entry.config(state='disabled')
    start_g_entry.config(state='disabled')
    start_b_entry.config(state='disabled')

def from_start_RGB_selection():
    start_text_var.set('')
    start_strip_label['background'] = bgcolor2
    # Enable RGB entry boxes
    start_r_entry.config(state='normal')
    start_g_entry.config(state='normal')
    start_b_entry.config(state='normal')
    # Reinitialize values
    start_r_entry.delete(0, tk.END)
    start_r_entry.insert(0, str(255))
    start_g_entry.delete(0, tk.END)
    start_g_entry.insert(0, str(255))
    start_b_entry.delete(0, tk.END)
    start_b_entry.insert(0, str(255))

# Function when start Select button is pushed
def start_color_select():

    if start_color_source.get() == 'strip':
        from_start_strip_selection()

    else:
        from_start_RGB_selection()



# Start: Color Label
label_inner_color = tk.Label(
    frame_colorselect,
    text='Inner Start Color',
    bg=bgcolor2,
    height=1,
    padx=0, pady=5,
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
    command=from_start_strip_selection
)

# Set radiobutton default
radio_start_from_strip.select()

start_text_var = tk.StringVar()

# Start: Color Strip Entry
start_strip_label = tk.Label(
    frame_colorselect, width=17,
    font=Verd12, bg=color_start,
    textvariable=start_text_var
)
start_text_var.set(color_start)

# Start: Color Select Button
btn_start_select = tk.Button(
    frame_colorselect,
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
    command=from_start_RGB_selection
)


### Start: RGB frame for RGB entries ..................
frame_rgb_start = tk.Frame(frame_colorselect,
                           bg=bgcolor2)

start_r_var = tk.StringVar()
start_g_var = tk.StringVar()
start_b_var = tk.StringVar()

# Creation
start_r_label = tk.Label(
    frame_rgb_start, width=1, font=Verd12,
    text='R', bg=bgcolor2
)
start_r_entry = tk.Entry(
    frame_rgb_start, width=3, font=Verd12,
    textvariable=start_r_var,
    # Callback with registered function +
    # Sends to the function the intended result (%P),
    # whether insertion or deletion (%d),
    # the text to insert (%S), and the index of the attempted
    # insertion (%i)
    validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
    # Validates whenever a keystroke changes the widget's contents
    validate='key',
    disabledforeground='black',
    state='disabled'
)
start_g_label = tk.Label(
    frame_rgb_start, width=1, font=Verd12,
    text='G', bg=bgcolor2
)
start_g_entry = tk.Entry(
    frame_rgb_start, width=3, font=Verd12,
    textvariable=start_g_var,
    # Callback with registered function +
    # Sends to the function the intended result (%P),
    # whether insertion or deletion (%d),
    # the text to insert (%S), and the index of the attempted
    # insertion (%i)
    validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
    # Validates whenever a keystroke changes the widget's contents
    validate='key',
    disabledforeground='black',
    state='disabled'
)
start_b_label = tk.Label(
    frame_rgb_start, width=1, font=Verd12,
    text='B', bg=bgcolor2
)
start_b_entry = tk.Entry(
    frame_rgb_start, width=3, font=Verd12,
    textvariable=start_b_var,
    # Callback with registered function +
    # Sends to the function the intended result (%P),
    # whether insertion or deletion (%d),
    # the text to insert (%S), and the index of the attempted
    # insertion (%i)
    validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
    # Validates whenever a keystroke changes the widget's contents
    validate='key',
    disabledforeground='black',
    state='disabled'
)

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
start_strip_label.grid(row=2, column=1, padx=5, sticky=tk.W)
btn_start_select.grid(row=2, column=2, padx=5)
radio_start_from_RGB.grid(row=3, column=0, sticky=tk.W)
frame_rgb_start.grid(row=3, column=1)



### End Color Section ...............

def from_end_strip_selection():
    # Getting color
    color_end = colorstrip.get(colorstrip.curselection()).strip()
    # Printing in label
    end_text_var.set(color_end)
    end_strip_label['background'] = color_end
    # Enable RGB entry boxes
    end_r_entry.config(state='normal')
    end_g_entry.config(state='normal')
    end_b_entry.config(state='normal')
    # Printing in RGB entry boxes
    end_r_entry.delete(0, tk.END)
    end_r_entry.insert(0, str(colors[color_end][0]))
    end_g_entry.delete(0, tk.END)
    end_g_entry.insert(0, str(colors[color_end][1]))
    end_b_entry.delete(0, tk.END)
    end_b_entry.insert(0, str(colors[color_end][2]))
    # Disable RGB entry boxes
    end_r_entry.config(state='disabled')
    end_g_entry.config(state='disabled')
    end_b_entry.config(state='disabled')

def from_end_RGB_selection():
    end_text_var.set('')
    end_strip_label['background'] = bgcolor2
    # Enable RGB entry boxes
    end_r_entry.config(state='normal')
    end_g_entry.config(state='normal')
    end_b_entry.config(state='normal')
    # Reinitialize values
    end_r_entry.delete(0, tk.END)
    end_r_entry.insert(0, str(255))
    end_g_entry.delete(0, tk.END)
    end_g_entry.insert(0, str(255))
    end_b_entry.delete(0, tk.END)
    end_b_entry.insert(0, str(255))

# Function when end Select button is pushed
def end_color_select():

    if end_color_source.get() == 'strip':
        from_end_strip_selection()

    else:
        from_end_RGB_selection()



# End: Color Label
label_outer_color = tk.Label(
    frame_colorselect,
    text='Outer End Color',
    bg=bgcolor2,
    height=1,
    padx=0, pady=5,
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
    command=from_end_strip_selection
)

# Set radiobutton default
radio_end_from_strip.select()

end_text_var = tk.StringVar()

# End: Color Strip Entry
end_strip_label = tk.Label(
    frame_colorselect, width=17,
    font=Verd12, bg=color_end,
    textvariable=end_text_var
)
end_text_var.set(color_end)

# End: Color Select Button
btn_end_select = tk.Button(
    frame_colorselect,
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
    command=from_end_RGB_selection
)


### End: RGB frame for RGB entries ..................
frame_rgb_end = tk.Frame(
    frame_colorselect,
    bg=bgcolor2
)

end_r_var = tk.StringVar()
end_g_var = tk.StringVar()
end_b_var = tk.StringVar()

# Creation
end_r_label = tk.Label(
    frame_rgb_end, width=1, font=Verd12,
    text='R', bg=bgcolor2
)
end_r_entry = tk.Entry(
    frame_rgb_end, width=3, font=Verd12,
    textvariable=end_r_var,
    # Callback with registered function +
    # Sends to the function the intended result (%P),
    # whether insertion or deletion (%d),
    # the text to insert (%S), and the index of the attempted
    # insertion (%i)
    validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
    # Validates whenever a keystroke changes the widget's contents
    validate='key',
    disabledforeground='black',
    state='disabled'
)
end_g_label = tk.Label(
    frame_rgb_end, width=1, font=Verd12,
    text='G', bg=bgcolor2
)
end_g_entry = tk.Entry(
    frame_rgb_end, width=3, font=Verd12,
    textvariable=end_g_var,
    # Callback with registered function +
    # Sends to the function the intended result (%P),
    # whether insertion or deletion (%d),
    # the text to insert (%S), and the index of the attempted
    # insertion (%i)
    validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
    # Validates whenever a keystroke changes the widget's contents
    validate='key',
    disabledforeground='black',
    state='disabled'
)
end_b_label = tk.Label(
    frame_rgb_end, width=1, font=Verd12,
    text='B', bg=bgcolor2
)
end_b_entry = tk.Entry(
    frame_rgb_end, width=3, font=Verd12,
    textvariable=end_b_var,
    # Callback with registered function +
    # Sends to the function the intended result (%P),
    # whether insertion or deletion (%d),
    # the text to insert (%S), and the index of the attempted
    # insertion (%i)
    validatecommand=(RGB_validation, '%P', '%d', '%S', '%i'),
    # Validates whenever a keystroke changes the widget's contents
    validate='key',
    disabledforeground='black',
    state='disabled'
)

# Placement in frame_rgb_end
end_r_label.grid(row=0, column=0)
end_r_entry.grid(row=0, column=1)
end_g_label.grid(row=0, column=2)
end_g_entry.grid(row=0, column=3)
end_b_label.grid(row=0, column=4)
end_b_entry.grid(row=0, column=5)




## Random Noise Section ------------------------

random_noise = tk.BooleanVar()

# Random Noise text message
randtext = (
    'Select the amount of random '
    'noise to add to the color evolution.  '
    'At low levels, '
    'noise can add an organic touch.  '
    'At hight levels, '
    'there is an explosion of colors, '
    'but it can overwhelm the start-to-end '
    'color path evolution.'
)
mess_rand = tk.Message(
    master=frame_colorselect,
    text=randtext,
    bg=bgcolor2,
    width=mess_textwidth,
    padx=5,
    font=Verd10
)

# Create label as title
label_rand = tk.Label(
    frame_colorselect,
    text='Random Noise',
    bg=bgcolor2,
    height=1,      # height in lines, not in pixels
    padx=0, pady=5,
    font=Verd14
)


# Create Random Noise Radio Buttons
frame_radio_rand = tk.Frame(
    frame_colorselect, 
    bg=bgcolor2,
    padx=10, pady=0,
    borderwidth=0
)
radio_rand_OFF = tk.Radiobutton(
    frame_radio_rand,
    text='Off',
    font=Verd12,
    variable=random_noise,
    value=False,
    bg=bgcolor2,
    activebackground='cyan',
    borderwidth=0
)
radio_rand_ON = tk.Radiobutton(
    frame_radio_rand,
    text='On',
    font=Verd12,
    variable=random_noise,
    value=True,
    bg=bgcolor2,
    activebackground='cyan',
    borderwidth=0
)

radio_rand_OFF.select()

radio_rand_OFF.pack(side=tk.LEFT)
radio_rand_ON.pack(side=tk.RIGHT)


# Create Noise Factor
noise = tk.StringVar()

label_noise_factor = tk.Label(
    frame_colorselect,
    text='Noise Factor',
    bg=bgcolor2,
    height=1,      # height in lines, not in pixels
    padx=0, pady=5,
    font=Verd14
)

combo_noise_factor = ttk.Combobox(
    frame_colorselect,
    width=3,
    textvariable=noise,
    values=['0.5', '1', '1.5', '2', '3', '4'],
    font=Verd12,
)
combo_noise_factor.current(1)



# Placement in frame_colorselect
label_outer_color.grid(row=4, column=0, sticky=tk.W)
radio_end_from_strip.grid(row=5, column=0, sticky=tk.W)
end_strip_label.grid(row=5, column=1, padx=5, sticky=tk.W)
btn_end_select.grid(row=5, column=2, padx=5)
radio_end_from_RGB.grid(row=6, column=0, sticky=tk.W)
frame_rgb_end.grid(row=6, column=1)
mess_rand.grid(row=7, column=0, columnspan=3, sticky=tk.W, pady=(20,0))
label_rand.grid(row=8, column=0, sticky=tk.W)
frame_radio_rand.grid(row=9, column=0, sticky=tk.W)
label_noise_factor.grid(row=8, column=1, sticky=tk.W)
combo_noise_factor.grid(row=9, column=1, sticky=tk.W, padx=(20,0))





##### Color Path Selection Frame -------------------------------------

frame_colorpath = tk.Frame(
    window, bg=bgcolor2,
    padx=10, pady=5,
    relief=tk.RIDGE,
    borderwidth=5
)

label_colorpath = tk.Label(
    frame_colorpath,
    text='Color Path',
    bg=bgcolor2,
    height=1,      # height in lines, not pixels
    padx=10,
    pady=5,
    font=Verd14
)

text_colorpath = (
    'Select a path through RGB space.  '
    'Different paths can produce different '
    'intermediate colors.'
)


mess_colorpath = tk.Message(
    master=frame_colorpath,
    text=text_colorpath,
    width=mess_textwidth,
    bg=bgcolor2,
    padx=5,
    font=Verd10
)


path_var = tk.StringVar()

radio_straightline = tk.Radiobutton(
    frame_colorpath,
    text='Straight Line Path',
    font=Verd12,
    variable=path_var,
    value='straightline',
    bg=bgcolor2,
    activebackground='cyan'
)

radio_straightline.select()  # Set radiobutton default

frame_Mpath = tk.Frame(
    frame_colorpath,
    bg=bgcolor2,
)

radio_manhattan = tk.Radiobutton(
    frame_Mpath,
    text='Manhattan Path',
    font=Verd12,
    variable=path_var,
    value='manhattan',
    bg=bgcolor2,
    activebackground='cyan',
)
radio_manhattan.pack(side=tk.LEFT, padx=(0, 10))

# Manhattan Path Combobox
Mpath = tk.StringVar()

combo_Mpath = ttk.Combobox(
    frame_Mpath,
    width=4,
    textvariable=Mpath,
    values=['RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR'],
    font=Verd12,
)
combo_Mpath.current(0)
combo_Mpath.pack(side=tk.LEFT)

radio_randomwalk = tk.Radiobutton(
    frame_colorpath,
    text='Random Walk',
    font=Verd12,
    variable=path_var,
    value='randomwalk',
    bg=bgcolor2,
    activebackground='cyan'
)

# Placement in frame_colorpath
label_colorpath.grid(row=0, column=0, sticky=tk.W)
mess_colorpath.grid(row=1, column=0)
radio_straightline.grid(row=2, column=0, sticky=tk.W)
frame_Mpath.grid(row=3, column=0, sticky=tk.W)
radio_randomwalk.grid(row=4, column=0, sticky=tk.W)





##### Color Strip Frame ------------------------------------

frame_colorstrip = tk.Frame(
    window, bg=bgcolor2,
    padx=10, pady=5,
    relief=tk.RIDGE,
    borderwidth=5
)


# Create listbox
colorstrip = tk.Listbox(
    frame_colorstrip,
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

frame_proceed = tk.Frame(
    window,
    bg=bgcolor2,
    padx=10, pady=5,
    relief=tk.RIDGE,
    borderwidth=5
)


tk.Label(
    frame_proceed,
    text='Proceed with Drawing?',
    bg=bgcolor2,
    height=1,     # height in lines, not pixels
    padx=0, pady=5,
    font=Verd14
).grid(row=0, column=0)



### Proceed Function ###################
counter = 0

def proceed_submit():
    global counter
    global color_start
    global color_end

    # Get spiral parameters

    sides = int(num_sides.get())

    dir_of_rot = direction.get()

    degree_of_rot = int(degree_rot.get())

    # Get rgb_start
    if start_color_source.get() == 'strip':
        color_start = start_text_var.get()
        rgb_start = colors[color_start]
        start_color_source_message = f'Start Color:  {color_start.capitalize()}'
    else:
        start_r = start_r_var.get()
        start_g = start_g_var.get()
        start_b = start_b_var.get()
        rgb_start = (int(start_r) if (start_r != '') else 0,
                     int(start_g) if (start_g != '') else 0,
                     int(start_b) if (start_b != '') else 0)
        start_color_source_message = f'End RGB Color Values:  {rgb_start}'
    print('RGB Start: ', rgb_start)

    # Get rgb_end
    if end_color_source.get() == 'strip':
        color_end = end_text_var.get()
        rgb_end = colors[color_end]
        end_color_source_message = f'End Color:  {color_end.capitalize()}'
    else:
        end_r = end_r_var.get()
        end_g = end_g_var.get()
        end_b = end_b_var.get()
        rgb_end = (int(end_r) if (end_r != '') else 0,
                   int(end_g) if (end_g != '') else 0,
                   int(end_b) if (end_b != '') else 0)
        end_color_source_message = f'End RGB Color Values:  {rgb_end}'
    print('RGB End: ', rgb_end)

    # Get path and noise info
    path = path_var.get()
    rgb_order = Mpath.get()
    noise_on = random_noise.get()
    noise_factor = noise.get()
    noise_interval_size = int(float(noise_factor) * 64)
    
    # Create message box
    mess_proceed = f'''Your Selection is...\t\t

Sides:  {sides}
Direction of Rotation:  {dir_of_rot.capitalize()}
Degree of Rotation:  {degree_of_rot}

{start_color_source_message}
{end_color_source_message}

Color Path:  {path.capitalize()} {f'- {rgb_order}' if path == 'manhattan' else ''}

Random Noise:  {'On' if noise_on else 'Off'}
Noise Factor:  {noise_factor}
'''
    box.showinfo('', mess_proceed)

    # Engage turtle drawing program
    if counter == 0:
        ### Turtle Window Setup
        turtle.setup(width=1280, height=960)
    else:                             # Skips clear on 1st iteration
        turtle.Screen().clear()       # Deletes all drawings and turtles
    counter += 1


    # Set numloops variable
    numloops = 360

    # Set scale variable
    scale = 1

    # Create rgb_list depending on chosen path
    if path == 'straightline':
        rgb_list = Colorpaths.straightline(numloops, rgb_start, rgb_end)
    elif path == 'manhattan':
        rgb_list = Colorpaths.Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    elif path == 'randomwalk':
        rgb_list = Colorpaths.randomwalk(numloops, rgb_start, noise_interval_size)
    else:
        rgb_list = Colorpaths.randompath(numloops, rgb_start, rgb_end)

    # Add random noise if selected
    if noise_on:
        rgb_list = RandomFunctions.noisy_list(rgb_list, noise_interval_size)
        

    # Draw spiral
    Spiral.draw_spiral(turtle, sides, dir_of_rot, degree_of_rot, numloops, rgb_list, scale)

### End Proceed Function #################

                         
tk.Button(
    frame_proceed, text='Proceed',
    command=proceed_submit,
    font=Verd12
).grid(row=0, column=1, padx=20)

##### End Proceed Frame -----------------------------------------



##### Main Frame Placement ------------------------------------------
frame_descript.grid(
    row=0, column=0,
    padx=0, pady=0,
    sticky=tk.N
)
frame_params.grid(
    row=1, column=0,
    padx=0, pady=0,
    sticky=tk.N
)
frame_colorselect.grid(
    row=0, column=1,
    pady=0,
    sticky=tk.N
)
frame_colorpath.grid(
    row=1, column=1,
    pady=0,
    sticky=tk.N
)
frame_proceed.grid(
    row=2, column=1,
    pady=0,
    sticky=tk.N
)
frame_colorstrip.grid(
    row=0, column=2, rowspan=3,
    pady=0
)


##### Window mainloop ------------------------------------------

window.mainloop()





