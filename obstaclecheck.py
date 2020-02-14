import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# infrared sensor for obstacle detection
Obsleft = 38
Obsright = 40
GPIO.setup(Obsleft, GPIO.IN)
GPIO.setup(Obsright, GPIO.IN)


def warn_left():
    if GPIO.input(Obsleft) == 0:  # 当有障碍物时，传感器输出低电平，所以检测低电平
        return True
    else:
        return False


def warn_right():
    if GPIO.input(Obsright) == 0:  # 当有障碍物时，传感器输出低电平，所以检测低电平
        return True
    else:
        return False
