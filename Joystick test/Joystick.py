import socket
import time
import serial

def send_command(command):
    try:
        tello_address = ('192.168.10.1', 8889)
        sock.sendto(command.encode(), tello_address)
        print(f"Sendt: {command}")
    except Exception as e:
        print(f"Fejl: {e}")

ser = serial.Serial('/dev/tty.usbmodem1201', 9600, timeout=1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

send_command("command")
time.sleep(0.5)

send_command("takeoff")
is_flying = True

x_midtenpoint = 497
y_midtenpoint = 511
stop = 20

midten_knap_x = 880
midten_knap_y = 1023
midten_knap_stop = 10

try:
    while True:
        if ser.in_waiting > 0:
            joystick_data = ser.readline().decode().strip()
            x_value, y_value = map(int, joystick_data.split(','))


            if (abs(x_value - midten_knap_x) <= midten_knap_stop) and (abs(y_value - midten_knap_y) <= midten_knap_stop):
                if not is_flying:
                    send_command("takeoff")
                    is_flying = True
                else:
                    send_command("land")
                    is_flying = False
                time.sleep(1)


            else:
                x_and = abs(x_value - x_midtenpoint)
                y_and = abs(y_value - y_midtenpoint)

                if x_and > stop or y_and > stop:
                    if x_and > y_and:
                        if x_value < x_midtenpoint - stop:
                            send_command("left 50")
                        elif x_value > x_midtenpoint + stop:
                            send_command("right 50")
                    else:
                        if y_value < y_midtenpoint - stop:
                            send_command("forward 50")
                        elif y_value > y_midtenpoint + stop:
                            send_command("back 50")

            time.sleep(0.1)

except KeyboardInterrupt:
    send_command("land")
    sock.close()
    ser.close()
