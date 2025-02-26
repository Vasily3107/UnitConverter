from UnitConverter import UnitConverter

class TemperatureConverter(UnitConverter):
    def __init__(self):
        super().__init__()
        self._units = ["Celsius (c)", "Faranheit (f)", "Kelvin (k)"]

    def convert(self):
        if self._unit1 == self._unit2: return self._value

        match self._unit1, self._unit2:
            case "c", "f": return self._value * 9/5 + 32
            case "c", "k": return self._value + 273.15

            case "f", "c": return (self._value - 32) * 5/9
            case "f", "k": return((self._value - 32) * 5/9) + 273.15

            case "k", "c": return  self._value - 273.15
            case "k", "f": return((self._value - 273.15) * 9/5) + 32

            case _: raise f"TemperatureConverter: default case exception | unit1: {self._unit1}, unit2: {self._unit2}"
