from MotorClass import Motor
import time
if __name__ == "__main__":
    # Channels 0, 4, 8, 12 enabled (bits 15, 11, 7, 3 → value = 0b1000100010001000 = 34952)
    # Channel 12 is continuous (bit 3 → 0b0000000000001000 = 8)
    motor = Motor(bitmask=0b1000100010001000, continuous_servos_mask=0b0000000000001000)

    try:
        while True:
            motor.setMotor(0, 180)
            motor.setMotor(4, 180)
            motor.setMotor(8, 180)
            motor.setMotor(12, 1)
            time.sleep(1)

            motor.setMotor(0, 0)
            motor.setMotor(4, 0)
            motor.setMotor(8, 0)
            motor.setMotor(12, -1)
            time.sleep(1)
    except KeyboardInterrupt:
        motor.setMotor(12, 0)
        print("\nMotors stopped.")