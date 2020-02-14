import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# ultracsonic sensor for distance calculation
Trig = 7
Echo = 11


# ultracsonic senso logic
def checkdist():

    t0 = time.time()

    GPIO.setup(Trig, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Echo, GPIO.IN)
    GPIO.output(Trig, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig, GPIO.LOW)
    while not GPIO.input(Echo):
        pass
    t1 = time.time()
    while GPIO.input(Echo):
        pass
    t2 = time.time()
    distance = (t2 - t1) * 340 * 100 / 2


def diststart():
    while True:
        checkdist()

diststart()
time.sleep(5)
GPIO.cleanup()