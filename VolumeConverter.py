from UnitConverter import UnitConverter

class VolumeConverter(UnitConverter):
    def __init__(self):
        super().__init__()
        self._units = ["Milliliters (ml)", "Liters (l)", "Cubic centimeters (cm^3)", "Cubic meters (m^3)"]

    def convert(self):
        if self._unit1 == self._unit2: return self._value

        match self._unit1, self._unit2:
            case "ml",    "l": return self._value * 1e-3
            case "ml", "cm^3": return self._value
            case "ml",  "m^3": return self._value * 1e-6

            case "l",   "ml": return self._value * 1e3
            case "l", "cm^3": return self._value * 1e3
            case "l",  "m^3": return self._value * 1e-3

            case "cm^3",  "ml": return self._value
            case "cm^3",   "l": return self._value * 1e-3
            case "cm^3", "m^3": return self._value * 1e-6

            case "m^3",   "ml": return self._value * 1e6
            case "m^3",    "l": return self._value * 1e3
            case "m^3", "cm^3": return self._value * 1e6

            case _: raise f"VolumeConverter: default case exception | unit1: {self._unit1}, unit2: {self._unit2}"
