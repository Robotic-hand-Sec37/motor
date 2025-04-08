import time
import threading # MULTI THREADING FOR EFFIN SERVOS XAXAXAXAXA
from adafruit_servokit import ServoKit

class Motor:
    def __init__(self, bitmask: int, continuous_servos_mask: int = 0):
        self.kit = ServoKit(channels=16)
        self.connected_servos = []
        self.continuous_servos = []

        for bit in range(16):
            channel = 15 - bit  # bit 15 maps to channel 0
            if bitmask & (1 << bit):
                self.connected_servos.append(channel)
            if continuous_servos_mask & (1 << bit):
                self.continuous_servos.append(channel)

    def setMotor(self, motorid, angle):
        if motorid not in self.connected_servos:
            print(f"Motor channel {motorid} not enabled.")
            return

        thread = threading.Thread(target=self._set_motor_internal, args=(motorid, angle))
        thread.daemon = True
        thread.start()

    def _set_motor_internal(self, motorid, angle):
        if motorid in self.continuous_servos:
            print(f"Setting continuous motor {motorid} throttle to {angle}")
            self.kit.continuous_servo[motorid].throttle = angle
        else:
            print(f"Setting servo motor {motorid} angle to {angle}")
            self.kit.servo[motorid].angle = angle