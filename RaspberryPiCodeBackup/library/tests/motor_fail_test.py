import motor_controller as mc
import time


mc.set_motor1_speed(100)
mc.stop_all()
mc.motor1_forward()
time.sleep(1)
mc.stop_all()
