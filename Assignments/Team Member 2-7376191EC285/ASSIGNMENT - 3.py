1)Python code for LED blinking using raspberry pi

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
 GPIO.output(8, GPIO.HIGH) # Turn on
 sleep(1) # Sleep for 1 second
 GPIO.output(8, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second

2)Python code for traffic lights using raspberry pi

from gpiozero import Button, TrafficLights, Buzzer    
from time import sleep    
    
buzzer = Buzzer(15)    
button = Button(21)    
lights = TrafficLights(25, 8, 7)    
    
while True:    
           button.wait_for_press()   
           buzzer.on()   
           light.green.on()    
           sleep(1)    
           lights.amber.on()    
           sleep(1)    
           lights.red.on()    
           sleep(1)    
           lights.off()   
           buzzer.off()  