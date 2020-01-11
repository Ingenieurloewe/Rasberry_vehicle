import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# ultracsonic sensor for distance calculation
Trig = 11
Echo = 15

# infrared sensor for obstacle detection
Obs = N.A.
GPIO.setup(Obs, GPIO.IN)

# ultracsonic senso logic
def checkdist():
    Trig = 11
    Echo = 15
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

# infrared sensor logic
def obstaclewarn():
    # if obstacle is in range, sensor return no no value to IO
    while GPIO.input(Obs):
        return False
    else:
        return True


diststart()
time.sleep(5)
GPIO.cleanup()