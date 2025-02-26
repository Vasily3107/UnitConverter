from UnitConverter import UnitConverter

class LengthConverter(UnitConverter):
    def __init__(self):
        super().__init__()
        self._units = ["Millimeters (mm)", "Centimeters (cm)", "Meters (m)", "Kilometers (km)"]

    def convert(self):
        if self._unit1 == self._unit2: return self._value

        match self._unit1, self._unit2:
            case "mm", "cm": return self._value * 1e-1
            case "mm", "m" : return self._value * 1e-3
            case "mm", "km": return self._value * 1e-6

            case "cm", "mm": return self._value * 1e1
            case "cm", "m" : return self._value * 1e-2
            case "cm", "km": return self._value * 1e-5

            case "m", "mm" : return self._value * 1e3
            case "m", "cm" : return self._value * 1e2
            case "m", "km" : return self._value * 1e-3

            case "km", "mm": return self._value * 1e6
            case "km", "cm": return self._value * 1e5
            case "km", "m" : return self._value * 1e3

            case _: raise f"LengthConverter: default case exception | unit1: {self._unit1}, unit2: {self._unit2}"