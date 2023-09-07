from time import sleep
import serial
from typing import Callable


class SerialApi:
    def __init__(self, port: str, baudrate: int, data_bit: int) -> None:
        self.serial_port = serial.Serial(
            port=port, baudrate=baudrate, bytesize=data_bit, timeout=2, stopbits=serial.STOPBITS_ONE)
        self.has_buffer = False
        self.event_listener = []

    def open(self):
        try:
            while True:
                if self.serial_port.in_waiting > 0:
                    self.has_buffer = True
                    for i in self.event_listener:
                        i()
                else:
                    self.has_buffer = False
        except serial.SerialException as error:
            print("Failed  {}".format(error))

    def add_listener(self, callback: Callable):
        self.event_listener.append(callback)

    def remove_listener(self, callback: Callable):
        self.event_listener.remove(callback)

    def readline(self) -> str:
        serial_string = self.serial_port.readline()
        capture_data = [ch.replace("\r\n", "")
                        for ch in serial_string.decode()]
        capture_data = "".join(capture_data).replace("\r\n", "")
        return capture_data

    def write(self, text: str):
        self.serial_port.write(f"{text}\n".encode())
