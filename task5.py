from time import sleep
class trafficlight:
    def rgy(self):
        sleep(1)
        print("Загарелся красный свет!")
        sleep(0.5)
        print("Загарелся желтый свет!")
        sleep(2)
        print("Загарелся зеленый свет!")


lights = trafficlight()
lights.rgy()
