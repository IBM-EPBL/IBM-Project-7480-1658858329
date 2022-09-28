import random
import winsound

while(1):
    temp = random.randint(0,110)
    hum =random.randint(0,60)
    if(temp>98.5 and((hum>30)and(hum<60))):
        print("alarm is ON")
        winsound.Beep(400, 500)
        print("alarm is OFF")
        print("-----------------------------------------------------")
    elif((hum>30)and(hum<60)):
        print("humidity is high alarm is ON")
        winsound.Beep(420, 500)
        print("alarm is OFF")
        print("-----------------------------------------------------")
    elif(temp>98.5):
        print("temperature is high alarm is ON")
        winsound.Beep(440, 500)
        print("alarm is OFF")
        print("-----------------------------------------------------")

