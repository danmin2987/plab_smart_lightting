from Init_.until import *

# giao tiep
ArduinoSerial = serial.Serial('/dev/ttyUSB0', 115200)
def get_serial(var):
   
    
    if (var == "1"):
        ArduinoSerial.write('1'.encode())
        #print('1')
    elif(var == "0" ):
        ArduinoSerial.write('0'.encode())
        #print('0')
    elif(var == "2" ):
        ArduinoSerial.write('2'.encode())
        #print('2')
    elif(var == "3"):
        ArduinoSerial.write('3'.encode())
        #print('3')
    elif(var == "4"):
        ArduinoSerial.write('4'.encode())
