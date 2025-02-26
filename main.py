from AreaConverter          import AreaConverter
from LengthConverter        import LengthConverter
from TemperatureConverter   import TemperatureConverter
from VolumeConverter        import VolumeConverter
from MassConverter          import MassConverter
from DataConverter          import DataConverter
from SpeedConverter         import SpeedConverter
from TimeConverter          import TimeConverter

from os import system
def cls(): system("cls")
def wait(): input("\nPress \"Enter\" to continue...")

def logic(constructor):
    conv = constructor()
    conv_name = constructor.__name__[:-9]

    units = conv.get_units()
    shortened_units = conv.get_shortened_units()

    def unit_input_error(unit):
        cls()
        print(f"There's no \"{unit}\" unit. Please enter one of options below:")
        for i in shortened_units:
            print(f" - {i}")
        wait()

    u1 = None; u2 = None
    result = None
    while True:
        cls()
        print(f"{conv_name} converter menu: \n")

        print("Available units:")
        for i in conv.get_units():
            print(f" - {i}")

        print("\nPlease type units abbreviations in parentheses:\n")

        if not u1:
            u1 = input("   convert from: ")
            if u1 not in shortened_units:
                unit_input_error(u1)
                u1 = None
                continue
        else:
            print(f"   convert from: {u1}")

        if not u2:
            u2 = input("     convert to: ")
            if u2 not in shortened_units:
                unit_input_error(u2)
                u2 = None
                continue
        else:
            print(f"     convert to: {u2}")

        val= input("    enter value: ")
        try:
            val = float(val)
        except:
            cls()
            print(f"Value error: {val}. Please enter a loating point number")
            wait()
            continue
        
        conv.set_parameters(u1, u2, val)
        result = conv.convert()
        break

    print(f"\nResults: {result}")
    print(f"\n{val} {u1} to {u2} = {result} {u2}")

    del conv
    wait()

while True:
    cls()
    print("Converter main menu: \n")

    print("1 - Area")
    print("2 - Lenght")
    print("3 - Temperature")
    print("4 - Volume")
    print("5 - Mass")
    print("6 - Data")
    print("7 - Speed")
    print("8 - Time")
    print("9 - Exit \n")

    match input("Enter choice: "):
        case "1": logic( AreaConverter        )
        case "2": logic( LengthConverter      )
        case "3": logic( TemperatureConverter )
        case "4": logic( VolumeConverter      )
        case "5": logic( MassConverter        )
        case "6": logic( DataConverter        )
        case "7": logic( SpeedConverter       )
        case "8": logic( TimeConverter        )

        case "9": break
        case   _: pass

cls()
print("Goodbye")
