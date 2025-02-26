from AreaConverter          import AreaConverter
from LengthConverter        import LengthConverter
from TemperatureConverter   import TemperatureConverter
from VolumeConverter        import VolumeConverter
from MassConverter          import MassConverter
from DataConverter          import DataConverter
from SpeedConverter         import SpeedConverter
from TimeConverter          import TimeConverter

from tkinter import *
from tkinter.ttk import Combobox, Style

w = Tk()
w.geometry("800x400")

BUTTON_WIDTH = 13

converet_choice_frame = Frame(w, width = 800, height = 50)
converet_choice_frame.grid(row = 0, column = 0, columnspan = 3)

def change_converter(constructor):
    global current_converter
    current_converter = constructor()

    units = current_converter.get_units()

    convert_from_menu.config(values = units)
    convert_to_menu.config(values = units)

    convert_from_menu.set(units[0])
    convert_to_menu.set(units[1])

converet_choice_buttons = [
   Button(converet_choice_frame, text = "Area"        , command = lambda: change_converter( AreaConverter        )),
   Button(converet_choice_frame, text = "Lenght"      , command = lambda: change_converter( LengthConverter      )),
   Button(converet_choice_frame, text = "Temperature" , command = lambda: change_converter( TemperatureConverter )),
   Button(converet_choice_frame, text = "Volume"      , command = lambda: change_converter( VolumeConverter      )),
   Button(converet_choice_frame, text = "Mass"        , command = lambda: change_converter( MassConverter        )),
   Button(converet_choice_frame, text = "Data"        , command = lambda: change_converter( DataConverter        )),
   Button(converet_choice_frame, text = "Speed"       , command = lambda: change_converter( SpeedConverter       )),
   Button(converet_choice_frame, text = "Time"        , command = lambda: change_converter( TimeConverter        ))
]
for i, button in enumerate(converet_choice_buttons):
    button.config(width = BUTTON_WIDTH)
    button.grid(row = 0, column = i)

theme_is_white = True
def change_theme():
    global theme_is_white

    if theme_is_white:
        new_fg = "white"
        new_bg = "black"
        theme_is_white = False

    else:
        new_fg = "black"
        new_bg = "white"
        theme_is_white = True
    
    w.config(bg = new_bg)

    for i in converet_choice_buttons:
        i.config(foreground = new_fg, background = new_bg)

    unit_choice_frame.config(bg = new_bg)
    for i in unit_choice_elements:
        try:
            i.config(foreground = new_fg, background = new_bg)
        except:
            i.config(foreground = new_fg, bg = new_bg)

change_theme_button = Button(text = "Change theme", command = change_theme)
change_theme_button.place(x = 5, y = 30)

unit_choice_frame = Frame(w, width = 800, height = 200, borderwidth = 20)
unit_choice_frame.grid(row = 2, column = 1, columnspan = 1)

convert_from_label = Label(unit_choice_frame, text = "Convert from:", borderwidth = 5)
convert_from_label.grid(row = 1, column = 0)

convert_from_menu = Combobox(unit_choice_frame, values = AreaConverter().get_units(), width = 30, state="readonly")
convert_from_menu.set(AreaConverter().get_units()[0])
convert_from_menu.grid(row = 1, column = 1)

convert_to_label = Label(unit_choice_frame, text = "Convert to:", borderwidth = 5)
convert_to_label.grid(row = 2, column = 0)

convert_to_menu = Combobox(unit_choice_frame, values = AreaConverter().get_units(), width = 30, state="readonly")
convert_to_menu.set(AreaConverter().get_units()[1])
convert_to_menu.grid(row = 2, column = 1)

convert_value_label = Label(unit_choice_frame, text = "Convert value:", borderwidth = 5)
convert_value_label.grid(row = 3, column = 0)

convert_value_entry = Entry(unit_choice_frame, width = 33)
convert_value_entry.grid(row = 3, column = 1)

def convert():
    global current_converter

    u1 = convert_from_menu.get().split("(")[1].split(")")[0]
    u2 =   convert_to_menu.get().split("(")[1].split(")")[0]

    try:
        value = float(convert_value_entry.get())
    except:
        convert_result_label.config(text = "Please enter a floating point number as a convert value", fg = "red")

        from time import sleep
        for _ in range(3):
            convert_value_entry.config(bg = "yellow", fg = "black" if theme_is_white else "white"); w.update()
            sleep(0.1)
            convert_value_entry.config(bg = "white" if theme_is_white else "black");  w.update()
            sleep(0.1)

        return

    current_converter.set_parameters(u1, u2, value)

    res = current_converter.convert()

    convert_result_label.config(text = f"Result: {res}", fg="black" if theme_is_white else "white")

convert_button = Button(unit_choice_frame, text = "Convert", command = convert, width = BUTTON_WIDTH*3)
convert_button.grid(row = 4, column = 0, columnspan = 2)

convert_result_label = Label(unit_choice_frame, text = "", borderwidth = 5)
convert_result_label.grid(row = 5, column = 0, columnspan = 2)

current_converter = AreaConverter()

unit_choice_elements = [
    change_theme_button,
    convert_from_label,
    convert_to_label,
    convert_value_label,
    convert_value_entry,
    convert_button,
    convert_result_label
]

mainloop()
