import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
# your Serial port should be different!
#arduino = serial.Serial('/dev/tty.usbmodem1411', 9600)
arduino = serial.Serial(port='COM3')

def onOffFunction():
	command = input("Type something..: (on/ off / bye )")
	if command =="on":
		print("The LED is on...")
		time.sleep(1) 
		arduino.write('H'.encode()) 
		onOffFunction()
	elif command =="off":
		print("The LED is off...")
		time.sleep(1) 
		arduino.write('L'.encode())
		onOffFunction()
	elif command =="bye":
		print("See You!...")
		time.sleep(1) 
		arduino.close()
	else:
		print("Sorry..type another thing..!")
		onOffFunction()

time.sleep(2) #waiting the initialization...

onOffFunction()
