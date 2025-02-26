from UnitConverter import UnitConverter

class TimeConverter(UnitConverter):
    def __init__(self):
        super().__init__()
        self._units = ["Milliseconds (ms)", "Seconds (s)", "Minutes (min)", "Hours (h)", "Days (d)", "Weeks (w)", "Months (m)", "Years (y)"]

    def convert(self):
        if self._unit1 == self._unit2: return self._value

        match self._unit1, self._unit2:
            case "ms",   "s": return self._value / 1e3
            case "ms", "min": return self._value / 1e3 / 60
            case "ms",   "h": return self._value / 1e3 / 3600
            case "ms",   "d": return self._value / 1e3 / 3600 / 24
            case "ms",   "w": return self._value / 1e3 / 3600 / 24 / 7
            case "ms",   "m": return self._value / 1e3 / 3600 / 24 / 7 / 4
            case "ms",   "y": return self._value / 1e3 / 3600 / 24 / 7 / 4 / 12
            
            case "s",  "ms": return self._value * 1e3
            case "s", "min": return self._value / 60
            case "s",   "h": return self._value / 3600
            case "s",   "d": return self._value / 3600 / 24
            case "s",   "w": return self._value / 3600 / 24 / 7
            case "s",   "m": return self._value / 3600 / 24 / 7 / 4
            case "s",   "y": return self._value / 3600 / 24 / 7 / 4 / 12

            case "min","ms": return self._value * 1e3 * 60
            case "min", "s": return self._value * 60
            case "min", "h": return self._value / 60
            case "min", "d": return self._value / 60 / 24
            case "min", "w": return self._value / 60 / 24 / 7
            case "min", "m": return self._value / 60 / 24 / 7 / 4
            case "min", "y": return self._value / 60 / 24 / 7 / 4 / 12

            case "h", "ms": return self._value * 1e3 * 3600
            case "h",  "s": return self._value * 3600
            case "h","min": return self._value * 60
            case "h",  "d": return self._value / 24
            case "h",  "w": return self._value / 24 / 7
            case "h",  "m": return self._value / 24 / 7 / 4
            case "h",  "y": return self._value / 24 / 7 / 4 / 12

            case "d", "ms": return self._value * 1e3 * 3600 * 24
            case "d",  "s": return self._value * 3600 * 24
            case "d","min": return self._value * 60 * 24
            case "d",  "h": return self._value * 24
            case "d",  "w": return self._value / 7
            case "d",  "m": return self._value / 7 / 4
            case "d",  "y": return self._value / 7 / 4 / 12

            case "w", "ms": return self._value * 1e3 * 3600 * 24 * 7
            case "w",  "s": return self._value * 3600 * 24 * 7
            case "w","min": return self._value * 60 * 24 * 7
            case "w",  "h": return self._value * 24 * 7
            case "w",  "d": return self._value * 7
            case "w",  "m": return self._value / 4
            case "w",  "y": return self._value / 4 / 12

            case "m", "ms": return self._value * 1e3 * 3600 * 24 * 7 * 4
            case "m",  "s": return self._value * 3600 * 24 * 7 * 4
            case "m","min": return self._value * 60 * 24 * 7 * 4
            case "m",  "h": return self._value * 24 * 7 * 4
            case "m",  "d": return self._value * 7 * 4
            case "m",  "w": return self._value * 4
            case "m",  "y": return self._value / 12

            case "y", "ms": return self._value * 1e3 * 3600 * 24 * 356
            case "y",  "s": return self._value * 3600 * 24 * 356
            case "y","min": return self._value * 60 * 24 * 356
            case "y",  "h": return self._value * 24 * 356
            case "y",  "d": return self._value * 356
            case "y",  "w": return self._value * 4 * 12
            case "y",  "m": return self._value * 12

            case _: raise f"TimeConverter: default case exception | unit1: {self._unit1}, unit2: {self._unit2}"
