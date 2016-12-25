from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()


def pressure():
    pressure = sense.get_pressure()
    return [{'dt': int(round(time.time())), 'pressure': pressure}]
