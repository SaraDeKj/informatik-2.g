from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()


tello.set_speed(100)
for x in range(4):
    tello.move_forward(50)
    tello.flip_forward()
    tello.rotate_clockwise(90)
    tello.move_forward(50)
    tello.flip_back()




tello.land()



