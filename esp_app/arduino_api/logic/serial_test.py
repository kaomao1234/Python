from time import sleep
import serial
PORT = "COM1"
BAUDRATE = 9600
BYTESIZE = 8

try:
    serialPort = serial.Serial(port=PORT, baudrate=BAUDRATE,
                               bytesize=BYTESIZE, timeout=2, stopbits=serial.STOPBITS_ONE)
    print("OK the port is opend!")
    while True:
        if serialPort.in_waiting > 0:
            serialString = serialPort.readline()
            # print(serialString.decode())
            capture_data = [ch.replace("\r\n", "")
                            for ch in serialString.decode()]
            capture_data= "".join(capture_data).replace("\r\n","")
            print(capture_data)
            sleep(1)
            serialPort.write(capture_data.encode())
except serial.SerialException as error:
    print("Failed  {}".format(error))
