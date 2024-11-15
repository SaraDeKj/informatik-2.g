import serial
import time
from djitellopy import Tello

ser = serial.Serial('/dev/cu.usbmodem1201', 9600)

tello = Tello()
tello.connect()
tello.takeoff()


calibration = {
    'forward': {'x': 22.65, 'y': -119.86, 'z': -5.17},
    'right': {'x': -300.15, 'y': 907.18, 'z': -778.98},
    'still': {'x': 35.29, 'y': -93.68, 'z': 5.63},
    'left': {'x': 37.85, 'y': 77.71, 'z': -99.47}
}

lock = False
lock_duration = 0.5
movement_duration = 1

try:
    while True:
        if not lock:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()

                if line.startswith("Accel:") and " | " in line:
                    try:
                        parts = line.split(" | ")
                        if len(parts) >= 2:
                            accel_data = parts[0]
                            accel_values = accel_data.replace("Accel:", "").split(",")
                            accel_x_raw, accel_y_raw, accel_z_raw = map(float, accel_values)
                        else:
                            continue
                    except ValueError:
                        continue

                    rc_l_r, rc_f_b = 0, 0
                    direction = None


                    # Venstre: x > 0, y > 0, z < 0
                    if accel_x_raw > 0 and accel_y_raw > 0 and accel_z_raw < 0:
                        rc_l_r = -20  # Bevæg til venstre
                        direction = "Venstre"

                    # Fremad: x > 0, y < 0, z < 0
                    elif accel_x_raw > 0 and accel_y_raw < 0 and accel_z_raw < 0:
                        rc_f_b = 20  # Bevæg fremad
                        direction = "Fremad"

                    # Højre: x < 0, y > 0, z < 0
                    elif accel_x_raw < 0 and accel_y_raw > 0 and accel_z_raw < 0:
                        rc_l_r = 20  # Bevæg til højre
                        direction = "Højre"

                    if direction:
                        # Udfør bevægelsen i et bestemt tid
                        tello.send_rc_control(rc_l_r, rc_f_b, 0, 0)
                        print(f"Dronen bevæger sig: {direction}")

                        time.sleep(movement_duration)  # Bevægelsesvarighed

                        # Stop dronen efter bevægelsen
                        tello.send_rc_control(0, 0, 0, 0)
                        print("Dronen stopper bevægelsen.")

                        lock = True
                        lock_start_time = time.time()

                else:
                    continue
            else:
                # Ingen data tilgængelig, gør ingenting
                continue
        else:
            # Tjek om låsen skal deaktiveres
            if time.time() - lock_start_time >= lock_duration:
                lock = False
                print("Dronen er klar til en ny vej")

except KeyboardInterrupt:
    try:
        tello.land()
    except Exception as e:
        print(f"Fejl ved landing: {e}")
    ser.close()
    print("Du landede")

except Exception as e:
    print(f"Fejl: {e}")
    try:
        tello.land()
    except Exception as e:
        print(f"Fejl ved landing: {e}")
    ser.close()
    print("Der var en fejl.")
