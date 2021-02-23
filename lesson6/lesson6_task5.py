class Stationery:
    def __init__(self, title='Этим можно рисовать '):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки. {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Это ручка.{self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Это карандаш.{self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Это маркар.{self.title}')

office_mat = Stationery()
office_mat.draw()

pen = Pen()
pencil = Pencil()
marker = Handle()

pencil.draw()
marker.draw()
pen.draw()
