import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


class Car(object):
    # left side motors gpio definition
    ENA = 33
    IN1 = 12
    IN2 = 16

    # right si de motors gpio definition
    ENB = 35
    IN3 = 18
    IN4 = 22

    Trig = 11
    Echo = 15

    def __init__(self,dc_a,dc_b):
        self.dc_a=50  # pwm dutycycle to control speed, init with 50, range 0--100
        self.dc_b=50
        GPIO.setup(Car.IN1, GPIO.OUT)
        GPIO.setup(Car.IN2, GPIO.OUT)
        GPIO.setup(Car.ENA, GPIO.OUT)  # PWM

        GPIO.setup(Car.IN3, GPIO.OUT)
        GPIO.setup(Car.IN4, GPIO.OUT)
        GPIO.setup(Car.ENB, GPIO.OUT)  # PWM

        GPIO.setup(Car.Trig, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(Car.Echo, GPIO.IN)

    @staticmethod
    def forward(self):
        GPIO.output(Car.ENA,True)
        GPIO.output(Car.IN1, True)
        GPIO.output(Car.IN2, False)

        GPIO.output(Car.ENB, True)
        GPIO.output(Car.IN3, True)
        GPIO.output(Car.IN4, False)

    @staticmethod
    def backward(self):
        GPIO.output(Car.ENA,True)
        GPIO.output(Car.IN1, False)
        GPIO.output(Car.IN2, True)

        GPIO.output(Car.ENB, True)
        GPIO.output(Car.IN3, False)
        GPIO.output(Car.IN4, True)

    @staticmethod
    def turnleft(self):
        GPIO.output(Car.ENA,True)
        GPIO.output(Car.IN1, False)
        GPIO.output(Car.IN2, True)

        GPIO.output(Car.ENB,True)
        GPIO.output(Car.IN3, True)
        GPIO.output(Car.IN4, False)

    @staticmethod
    def turnright(self):
        GPIO.output(Car.ENA,True)
        GPIO.output(Car.IN1, True)
        GPIO.output(Car.IN2, False)

        GPIO.output(Car.ENB,True)
        GPIO.output(Car.IN3, False)
        GPIO.output(Car.IN4, True)

    def decel(self):
        pwm_left = GPIO.PWM(Car.ENA, 100)
        pwm_left.start(self.dc_a-20)
        pwm_right = GPIO.PWM(Car.ENB, 100)
        pwm_right.start(self.dc_b-20)

    def accel(self):
        pwm_left = GPIO.PWM(Car.ENA, 100)
        pwm_left.start(self.dc_a+20)
        pwm_right = GPIO.PWM(Car.ENB, 100)
        pwm_right.start(self.dc_b+20)

    @staticmethod
    def stop(self):
        GPIO.output(Car.IN1, False)
        GPIO.output(Car.IN2, False)

        GPIO.output(Car.IN3, False)
        GPIO.output(Car.IN4, False)

    @staticmethod
    def exit(self):
        GPIO.output(Car.ENA, False)
        GPIO.output(Car.IN1, False)
        GPIO.output(Car.IN2, False)

        GPIO.output(Car.ENB, False)
        GPIO.output(Car.IN3, False)
        GPIO.output(Car.IN4, False)
        GPIO.cleanup()