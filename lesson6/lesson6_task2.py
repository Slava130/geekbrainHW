class Road:
    _length = None
    _width = None
    thickness = None

    def __init__(self, width, length, thickness):
        self.width = width
        self.length = length
        self.thickness = thickness

    def weight(self, weight_on_sqm=25):
        weight = self.length * self.width * self.thickness * weight_on_sqm
        print(f'На дарогу необходимо', weight / 1000, 'тон асфальта.')
        return weight


street = Road(10, 10, 2)
street.weight()
