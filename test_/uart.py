from until import *

# giao tiep
ArduinoSerial = serial.Serial('/dev/ttyUSB0', 115200)
def get_serial(var):
   
    
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
