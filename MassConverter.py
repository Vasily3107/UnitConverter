from UnitConverter import UnitConverter

class MassConverter(UnitConverter):
    def __init__(self):
        super().__init__()
        self._units = ["Milligrams (mg)", "Grams (g)", "Kilograms (kg)", "Tons (t)"]

    def convert(self):
        if self._unit1 == self._unit2: return self._value

        match self._unit1, self._unit2:
            case "mg",  "g": return self._value * 1e-3
            case "mg", "kg": return self._value * 1e-6
            case "mg",  "t": return self._value * 1e-9

            case "g", "mg": return self._value * 1e+3
            case "g", "kg": return self._value * 1e-3
            case "g",  "t": return self._value * 1e-6

            case "kg", "mg": return self._value * 1e+6
            case "kg",  "g": return self._value * 1e+3
            case "kg",  "t": return self._value * 1e-3

            case "t", "mg": return self._value * 1e+9
            case "t",  "g": return self._value * 1e+6
            case "t", "kg": return self._value * 1e+3

            case _: raise f"MassConverter: default case exception | unit1: {self._unit1}, unit2: {self._unit2}"