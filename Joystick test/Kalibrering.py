import serial
import time

ser = serial.Serial('/dev/tty.usbmodem1201', 9600, timeout=1)

try:
    while True:
        if ser.in_waiting > 0:
            joystick_data = ser.readline().decode().strip()
            x_value, y_value = map(int, joystick_data.split(','))

            print(f"X: {x_value}, Y: {y_value}")
            time.sleep(0.1)
except KeyboardInterrupt:
    ser.close()
