import serial
import time
from pynput.keyboard import Key, Controller

PORT = "COM4"

valueArray = []
keyboardByte = 0

keyboard = Controller()

def get_integer(string):
	value = 0
	try:
		value = int(string)
	except:
		pass
	return value

def resetArray():
	global valueArray
	valueArray.clear()

def addElement(index, value):
	global valueArray
	if(index >= len(valueArray)):
		valueArray.append(value)
	
def updateKeyboardByte():
	global valueArray
	global keyboardByte
	global keyboardCount
	bit = 0
	sum = 0
	for x in valueArray:
		sum += x
	average = sum/len(valueArray)
	if(average >= 100):
		bit = 1
	keyboardByte += bit*(2**keyboardCount)
	keyboardCount+=1;
	print("Average: ", average, " Bit Value: ", bit, " Count: ", keyboardCount-1)
	if(keyboardCount >= 8):
		print(keyboardByte)
		keyboard.press(chr(keyboardByte))
		keyboard.release(chr(keyboardByte))
		keyboardByte = 0
		keyboardCount = 0

try:
	arduino = serial.Serial(PORT, 9600, timeout=1)
except:
	print("Please chech the port!")

time.sleep(1)

print("Successfully connected!")

currentString = ""
lastString = ""

currentVal = 0
lastVal = 0

timeCount = 0

keyboardCount = 0

while True:
	currentString = arduino.readline().decode('UTF-8').replace("\r\n", "")
	if(lastString != currentString):
		lastString = currentString
		currentVal = get_integer(lastString)
	if(currentVal != lastVal):
		if(currentVal == 0):
			currentVal = lastVal
		lastVal = currentVal
		#print("O: ", lastVal, " ", arduino.in_waiting)
	time.sleep(0.1)
	addElement(timeCount, lastVal)
	timeCount+=1
	if(timeCount >= 19):
		timeCount = 0
		updateKeyboardByte()
		resetArray()
	arduino.reset_input_buffer()