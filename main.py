from MotorClass import Motor
import keyboard
import time

MOTOR_CHANNELS = [11, 12, 13, 14, 15]  
ANGLE_STEP = 5
MAX_ANGLE = 180
MIN_ANGLE = 0
CONTINUOUS_SERVO_CHANNEL = 15  

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

if __name__ == "__main__":    
    bitmask = sum(1 << ch for ch in MOTOR_CHANNELS)
    continuous_mask = (1 << CONTINUOUS_SERVO_CHANNEL) if CONTINUOUS_SERVO_CHANNEL is not None else 0
    motor = Motor(bitmask=bitmask, continuous_servos_mask=continuous_mask)
    current_motor_index = 0
    angles = {ch: 90 for ch in MOTOR_CHANNELS if ch != CONTINUOUS_SERVO_CHANNEL}
    print("Use LEFT/RIGHT to select motor. UP/DOWN to adjust angle/speed. ESC to exit.")
    try:
        while True:
            if keyboard.is_pressed('left'):
                current_motor_index = (current_motor_index - 1) % len(MOTOR_CHANNELS)
                print(f"Selected motor: {MOTOR_CHANNELS[current_motor_index]}")
                time.sleep(0.2)

            elif keyboard.is_pressed('right'):
                current_motor_index = (current_motor_index + 1) % len(MOTOR_CHANNELS)
                print(f"Selected motor: {MOTOR_CHANNELS[current_motor_index]}")
                time.sleep(0.2)

            elif keyboard.is_pressed('up'):
                ch = MOTOR_CHANNELS[current_motor_index]
                if ch == CONTINUOUS_SERVO_CHANNEL:
                    motor.setMotor(ch, 1)
                    print(f"Motor {ch} running forward")
                else:
                    angles[ch] = clamp(angles[ch] + ANGLE_STEP, MIN_ANGLE, MAX_ANGLE)
                    motor.setMotor(ch, angles[ch])
                    print(f"Motor {ch} angle: {angles[ch]}")
                time.sleep(0.1)

            elif keyboard.is_pressed('down'):
                ch = MOTOR_CHANNELS[current_motor_index]
                if ch == CONTINUOUS_SERVO_CHANNEL:
                    motor.setMotor(ch, -1)
                    print(f"Motor {ch} running backward")
                else:
                    angles[ch] = clamp(angles[ch] - ANGLE_STEP, MIN_ANGLE, MAX_ANGLE)
                    motor.setMotor(ch, angles[ch])
                    print(f"Motor {ch} angle: {angles[ch]}")
                time.sleep(0.1)

            elif keyboard.is_pressed('esc'):
                break

    except KeyboardInterrupt:
        pass
    finally:
        for ch in MOTOR_CHANNELS:
            if ch == CONTINUOUS_SERVO_CHANNEL:
                motor.setMotor(ch, 0)
            else:
                motor.setMotor(ch, 90)
        print("\nMotors stopped. Exiting.")
