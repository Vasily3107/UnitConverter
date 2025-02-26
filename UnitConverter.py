class UnitConverter:
    def __init__(self):
        self._unit1 = None
        self._unit2 = None
        self._value = None
        self._units = []


    def get_units(self):
        return self._units


    def get_shortened_units(self):
        return list(map(lambda i: str.lower(i.split("(")[1].split(")")[0]), self._units))


    def set_parameters(self, unit1:str, unit2:str, value:float):
        self._unit1 = unit1
        self._unit2 = unit2
        self._value = value


    def convert(self):
        ...
