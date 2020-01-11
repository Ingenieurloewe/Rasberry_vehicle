import RPi.GPIO as GPIO
import CarControl
import distance
GPIO.setmode(GPIO.BOARD)


def main ():
   car = CarControl.Car()


def go():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    Trig = 11
    Echo = 15
    GPIO.setup(12,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(33,GPIO.OUT) 
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(35,GPIO.OUT)
    GPIO.setup(Trig, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Echo, GPIO.IN)

    t0 = time.time()
    
    while (time.time()-t0) <=20:
        GPIO.output(33,True)
        GPIO.output(35,True)
        GPIO.output(12,True)
        GPIO.output(16,False)  
        GPIO.output(18,True)
        GPIO.output(22,False)
        GPIO.output(Trig, GPIO.HIGH)
        time.sleep(0.00015)
        GPIO.output(Trig, GPIO.LOW)
        while not GPIO.input(Echo):
            pass
        t1 = time.time()
        while GPIO.input(Echo):
            pass
        t2 = time.time()
        distance =  (t2-t1)*340*100/2
        
        if  distance <=30 :
            GPIO.output(33,False)
            GPIO.output(35,False)
            GPIO.output(12,False)
            GPIO.output(16,False)  
            GPIO.output(18,False)
            GPIO.output(22,False)
            GPIO.cleanup()
    else:
        time.sleep(1)
        GPIO.cleanup() 
go()
time.sleep(5)
GPIO.cleanup()
