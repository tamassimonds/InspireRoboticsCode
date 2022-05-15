import motor_controller as mc
import time


mc.stop_all()


mc.motor1_forward()
time.sleep(1)
mc.stop_all()

mc.motor2_forward()
time.sleep(1)
mc.stop_all()

mc.motor3_forward()
time.sleep(1)
mc.stop_all()
