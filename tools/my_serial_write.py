import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200
)

ser.write("$ON;L\n")
