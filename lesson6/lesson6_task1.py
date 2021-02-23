from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def switching(self):
        el = 0
        while el < 3:
            print(f' переключение \n '
                  f'{TrafficLight.__color[el]}')
            if el == 0:
                sleep(7)
            elif el == 1:
                sleep(5)
            elif el == 2:
                sleep(3)
            el += 1

trafficLight = TrafficLight()
trafficLight.switching()