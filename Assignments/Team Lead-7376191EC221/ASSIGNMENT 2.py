import random
import winsound
import time
while(1):
    temp = random.randint(97,100) #noraml temp range starts from 97
    print("Temperature  = ",format(temp))
    humidity = random.randint(0,100)         #ideal humidity range for human survival is 30 to 60
    print("Humidity = ",format(humidity))
    print(end='\n')
    if(temp>98 and (humidity < 30 or humidity > 60)):
        print("Oh no! temperature is high and humidity is worse")
        winsound.PlaySound("mixkit-emergency-alert-alarm-1007.wav", winsound.SND_FILENAME)
        print("----------------------------------------------------------------------------")
    elif(temp>98):
        print("Oh no! temperature is high")
        winsound.PlaySound("mixkit-morning-clock-alarm-1003.wav", winsound.SND_FILENAME)
        print("----------------------------------------------------------------------------")
    elif(humidity < 30 or humidity > 60):
        print("Oh no! not suitable humidity")
        winsound.PlaySound("mixkit-classic-alarm-995.wav", winsound.SND_FILENAME)
        print("----------------------------------------------------------------------------")
    else:
        print("Everything is Normal")
        time.sleep(3)
        print("----------------------------------------------------------------------------")
        
    
