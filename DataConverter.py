from UnitConverter import UnitConverter

class DataConverter(UnitConverter):
    def __init__(self):
        super().__init__()
        self._units = ["Bits (bit)", "Bytes (B)", "Kilobytes (KB)", "Megabytes (MB)", "Gigabytes (GB)", "Terabytes (TB)"]

    def convert(self):
        if self._unit1 == self._unit2: return self._value

        match self._unit1, self._unit2:
            case "bit",  "B": return self._value / 8
            case "bit", "KB": return self._value / (8 * 1024)
            case "bit", "MB": return self._value / (8 * 1024**2)
            case "bit", "GB": return self._value / (8 * 1024**3)
            case "bit", "TB": return self._value / (8 * 1024**4)

            case "B","bit": return self._value * 8
            case "B", "KB": return self._value / 1024
            case "B", "MB": return self._value / 1024**2
            case "B", "GB": return self._value / 1024**3
            case "B", "TB": return self._value / 1024**4

            case "KB","bit": return self._value * 8 * 1024
            case "KB",  "B": return self._value * 1024
            case "KB", "MB": return self._value / 1024
            case "KB", "GB": return self._value / 1024**2
            case "KB", "TB": return self._value / 1024**3

            case "MB","bit": return self._value * 8 * 1024**2
            case "MB",  "B": return self._value * 1024**2
            case "MB", "KB": return self._value * 1024
            case "MB", "GB": return self._value / 1024
            case "MB", "TB": return self._value / 1024**2

            case "GB","bit": return self._value * 8 * 1024**3
            case "GB",  "B": return self._value * 1024**3
            case "GB", "KB": return self._value * 1024**2
            case "GB", "MB": return self._value * 1024
            case "GB", "TB": return self._value / 1024

            case "TB","bit": return self._value * 8 * 1024**4
            case "TB",  "B": return self._value * 1024**4
            case "TB", "KB": return self._value * 1024**3
            case "TB", "MB": return self._value * 1024**2
            case "TB", "GB": return self._value * 1024

            case _: raise f"DataConverter: default case exception | unit1: {self._unit1}, unit2: {self._unit2}"