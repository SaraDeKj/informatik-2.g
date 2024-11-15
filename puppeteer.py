import serial
import time
from djitellopy import Tello

ser = serial.Serial('/dev/cu.usbmodem11201', 9600, timeout=1)

tello = Tello()
tello.connect()
#tello.takeoff()

calibration = {
    'backward': {'x': -26.42, 'y': -1051.32, 'z': -663.8},
    'forward': {'x': 22.65, 'y': -119.86, 'z': -5.17},
    'right': {'x': 57.99, 'y': 907.18, 'z': -778.98},
    'still': {'x': 35.29, 'y': -93.68, 'z': 5.63},
    'left': {'x': 37.85, 'y': 77.71, 'z': -99.47}
}

lock = False
lock_duration = 1  # låser i 1 sekund
movement_duration = 3  # bevægelse i sekunder
message_shown = False  # stoppe dumme beskeder

try:
    while True:
        if not lock:
            # vent på den nye data (hvilken vej)
            line = ser.readline().decode('utf-8').strip()

            #kontroller dataen, ift. hvad der kommer fra arduinoen
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
                direction = "Hovrer"   # Standard


                # 1. Bagud: x, y, z er negative
                if accel_x_raw < 0 and accel_y_raw < 0 and accel_z_raw < 0:
                    rc_f_b = -20  # Bevæg bagud
                    direction = "Bagud"

                # 2. Fremad: x > 0, y < 0, z < 0
                elif accel_x_raw > 0 and accel_y_raw < 0 and accel_z_raw < 0:
                    rc_f_b = 20  # Bevæg fremad
                    direction = "Fremad"

                # 3. Højre: x > 0, y > 0, z er meget negativ
                elif accel_x_raw > 0 and accel_y_raw > 0 and accel_z_raw < -700:
                    rc_l_r = 20  # Bevæg til højre
                    direction = "Højre"

                # 5. Venstre: x > 0, y > 0, z er lidt negativ
                elif accel_x_raw > 0 and accel_y_raw > 0 and -700 < accel_z_raw < 0:
                    rc_l_r = -20  # Bevæg til venstre
                    direction = "Venstre"

                # 4. Hovre: x > 0, z > 0, y < 0
                else:
                    rc_l_r, rc_f_b = 0, 0  # Hovrer
                    direction = "Hovrer"

                # Udfør bevægelsen i et bestemt tid
                tello.send_rc_control(rc_l_r, rc_f_b, 0, 0)
                print(f"Dronen bevæger sig: {direction}")

                time.sleep(movement_duration)  # Bevægelsesvarighed

                # Stop dronen efter bevægelsen
                tello.send_rc_control(0, 0, 0, 0)
                print("Dronen er stoppet med at bevæge sig")

                # Aktivér låsen
                lock = True
                lock_start_time = time.time()
                message_shown = False

            else:
                time.sleep(0.1)

        else:
            # Tjek om låsen skal deaktiveres
            if time.time() - lock_start_time >= lock_duration:
                lock = False
                print("Dronen er klar til en ny vej")

                ser.reset_input_buffer()

            else:
                if not message_shown:
                    print("Venter på cooldown er over")
                    message_shown = True
                time.sleep(0.1)

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
