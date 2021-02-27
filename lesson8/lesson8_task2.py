class OwnError:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def zero_division(divider, denominator):
        try:
            return f'Результат - {divider / denominator}'
        except :
            return f'На ноль делить нельзя'


d = OwnError(20, 30)
print(OwnError.zero_division(55, 0))
print(OwnError.zero_division(36, 6))
print(d.zero_division(88, 0))
