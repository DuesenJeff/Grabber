import serial
import pyautogui
import time

try:
	arduino = serial.Serial("COM4", timeout=1)
except:
	print("Please check the port")

print("Successfully connected!")

currentString = ''
lastString = ''

clicked = False
changed = False

while True:
	currentString = arduino.readline().decode('UTF-8').replace("\r\n", "")
	if(lastString != currentString):
		print(currentString)
		lastString = currentString
		changed = True
	else:
		changed = False
	try: 
		if(int(currentString) > 199):
			if(clicked):
				pyautogui.click(None, None)
				clicked = False
			if(changed):
				clicked = True
				
	except:
		print("No VAL: ", currentString)
	