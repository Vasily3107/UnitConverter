from UnitConverter import UnitConverter

class AreaConverter(UnitConverter):
    def __init__(self):
        super().__init__()
        self._units = ["Square millimeters (mm^2)", "Square centimeters (cm^2)", "Square meters (m^2)", "Square kilometers (km^2)"]

    def convert(self):
        if self._unit1 == self._unit2: return self._value

        match self._unit1, self._unit2:
            case "mm^2", "cm^2": return self._value * 1e-2
            case "mm^2", "m^2" : return self._value * 1e-6
            case "mm^2", "km^2": return self._value * 1e-12

            case "cm^2", "mm^2": return self._value * 1e2
            case "cm^2", "m^2" : return self._value * 1e-4
            case "cm^2", "km^2": return self._value * 1e-10

            case "m^2", "mm^2" : return self._value * 1e6
            case "m^2", "cm^2" : return self._value * 1e4
            case "m^2", "km^2" : return self._value * 1e-6

            case "km^2", "mm^2": return self._value * 1e12
            case "km^2", "cm^2": return self._value * 1e10
            case "km^2", "m^2" : return self._value * 1e6

            case _: raise f"AreaConverter: default case exception | unit1: {self._unit1}, unit2: {self._unit2}"