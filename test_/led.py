import serial
import time

ArduinoSerial = serial.Serial('/dev/ttyUSB0', 9600)

while True :
    var = input("bam 1 led sang, bam 0 led tat")
    if (var == "1"):
        ArduinoSerial.write( "0x31".encode())
        
    elif(var == "0" ):
        ArduinoSerial.write("0x30".encode())
    elif(var == "2" ):
        ArduinoSerial.write("0x32".encode())
    elif(var == "3"):
        ArduinoSerial.write("0x33".encode())
    elif(var == "4"):
        ArduinoSerial.write("0x34".encode())
    elif(var == "5"):
        ArduinoSerial.write("0x35".encode())
