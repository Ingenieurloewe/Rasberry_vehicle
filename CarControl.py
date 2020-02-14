import RPi.GPIO as GPIO

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

    Trig = 7
    Echo = 11

    def __init__(self,dc_a,dc_b):
        self.dc_a=30  # pwm dutycycle to control speed, init with 30, range 0--100
        self.dc_b=30
        GPIO.setup(Car.IN1, GPIO.OUT)
        GPIO.setup(Car.IN2, GPIO.OUT)
        GPIO.setup(Car.ENA, GPIO.OUT)  # PWM

        GPIO.setup(Car.IN3, GPIO.OUT)
        GPIO.setup(Car.IN4, GPIO.OUT)
        GPIO.setup(Car.ENB, GPIO.OUT)  # PWM

        GPIO.setup(Car.Trig, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(Car.Echo, GPIO.IN)

    def forward(self):
        GPIO.PWM(Car.ENA, self.dc_a)
        GPIO.output(Car.IN1, True)
        GPIO.output(Car.IN2, False)

        GPIO.PWM(Car.ENB, self.dc_b)
        GPIO.output(Car.IN3, True)
        GPIO.output(Car.IN4, False)

    def backward(self):
        GPIO.PWM(Car.ENA, self.dc_a)
        GPIO.output(Car.IN1, False)
        GPIO.output(Car.IN2, True)

        GPIO.PWM(Car.ENB, self.dc_b)
        GPIO.output(Car.IN3, False)
        GPIO.output(Car.IN4, True)

    def turnleft(self):
        GPIO.PWM(Car.ENA, self.dc_a)
        GPIO.output(Car.IN1, False)
        GPIO.output(Car.IN2, True)

        GPIO.PWM(Car.ENB, self.dc_b)
        GPIO.output(Car.IN3, True)
        GPIO.output(Car.IN4, False)

    def turnright(self):
        GPIO.PWM(Car.ENA, self.dc_a)
        GPIO.output(Car.IN1, True)
        GPIO.output(Car.IN2, False)

        GPIO.PWM(Car.ENB, self.dc_b)
        GPIO.output(Car.IN3, False)
        GPIO.output(Car.IN4, True)

    def decel(self):
        GPIO.PWM(Car.ENA, self.dc_a - 20)
        GPIO.PWM(Car.ENB, self.dc_b - 20)

    def accel(self):
        GPIO.PWM(Car.ENA, self.dc_a + 20)
        GPIO.PWM(Car.ENB, self.dc_b + 20)

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