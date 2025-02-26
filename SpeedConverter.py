from UnitConverter import UnitConverter

class SpeedConverter(UnitConverter):
    def __init__(self):
        super().__init__()
        self._units = ["Meters per second (m/s)", "Meters per hour (m/h)", "Kilometers per second (km/s)", "Kilometers per hour (km/h)"]

    def convert(self):
        if self._unit1 == self._unit2: return self._value

        match self._unit1, self._unit2:
            case "m/s", "m/h": return self._value * 3600
            case "m/s","km/s": return self._value * 1e-3
            case "m/s","km/h": return self._value * 3.6

            case "m/h", "m/s": return self._value / 3600
            case "m/h","km/s": return self._value * 3.6e-6
            case "m/h","km/h": return self._value * 1e-3

            case "km/s", "m/s": return self._value * 1e3
            case "km/s", "m/h": return self._value * 3.6e6
            case "km/s","km/h": return self._value * 3600

            case "km/h", "m/s": return self._value / 3.6
            case "km/h", "m/h": return self._value * 1e3
            case "km/h","km/s": return self._value / 3600

            case _: raise f"SpeedConverter: default case exception | unit1: {self._unit1}, unit2: {self._unit2}"