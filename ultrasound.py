# Import required Python libraries
import time
import RPi.GPIO as GPIO

class UltraSound(object):
    def __init__(self, trigger, echo):
        self.trigger = trigger
        self.echo = echo
        # Use BCM GPIO references
        GPIO.setmode(GPIO.BCM)
        
        # Set pins as output and input
        GPIO.setup(trigger,GPIO.OUT)  # Trigger
        GPIO.setup(echo,GPIO.IN)      # Echo

        # Set trigger to False (Low)
        GPIO.output(trigger, False)

    def measure_once(self):
        # Send 10us pulse to trigger
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)
        start = time.time()
        while GPIO.input(self.echo)==0:
            start = time.time()

        while GPIO.input(self.echo)==1:
            stop = time.time()

        # Calculate pulse length
        elapsed = stop-start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distance = elapsed * 34000

        # That was the distance there and back so halve the value
        distance = distance / 2
        return distance
    
    def measure(self):
        li =[]
        for i in range(4):
            li.append( self.measure_once())
        li.sort()
        #print(li)
        dist = (li[1]+li[2])/2.0
        return dist


