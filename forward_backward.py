import serial
import time

ser = serial.Serial('COM4',9600)

while ser.isOpen:
    b = ser.readline()
    flt = b.decode()
    dist = float(flt)
    print(dist)
    if(dist < 40): 
        print('MOVE FORWARD and dist is : '+str(dist))
    elif(dist >=40 and dist < 70):
        print('Stay Neutral and dist is :'+ str(dist))
    elif(dist >= 70 ):
        print('MOVE BACKWARD and dist is :'+ str(dist))           

ser.close()

