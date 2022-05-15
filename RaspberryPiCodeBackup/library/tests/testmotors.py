import motor_controller as mc
import time

mc.motor1_backward()
mc.motor2_backward()
mc.motor3_backward()
time.sleep(1)

mc.stop_all()
mc.motor1_forward()
mc.motor2_forward()
mc.motor3_forward()

time.sleep(1)

mc.stop_all()
