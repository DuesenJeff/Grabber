#The serial module is used for reading the serial port of the arduino.
import serial
#The pyautogui provides a way to perform a mouseclick.
import pyautogui

#The PORT constant saves the port address for the arduino connected serial port.
PORT = "COM4"

#Establishing connection with the Arduino on the in the 'PORT' variable specified port.
try:
	arduino = serial.Serial(PORT, timeout=1)
except:
	print("Please check the port")

print("Successfully connected!")

currentString = ''
lastString = ''

clicked = False
changed = False

#Main loop of the script
while True:
	#Converting the byte encoded string to an UTF-8 encoded string and saving it in the variable 'currentString'. Also removing line breaks.
	currentString = arduino.readline().decode('UTF-8').replace("\r\n", "")
	#This if-branch will be entered if the data from the serial port has changed.
	if(lastString != currentString):
		#This print statement is solely there for debugging purposes.
		print(currentString)
		lastString = currentString
		changed = True
	else:
		changed = False
	#Converting the string data to integer data
	try: 
		#If the value of the data is over 199 then a mouseclick will be executed. 
		if(int(currentString) > 199):
			#These two if branches are there to prevent the script from clicking multiple times at the same time.
			if(clicked):
				pyautogui.click(None, None)
				clicked = False
			if(changed):
				clicked = True
	except:
		print("No VAL: ", currentString)
	