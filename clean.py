from adafruit_servokit import ServoKit

def clean_all_servos():
    try:
        kit = ServoKit(channels=16)
        for i in range(16):
            try:
                kit.servo[i].angle = None  # Releases standard servo
            except Exception:
                pass
            try:
                kit.continuous_servo[i].throttle = 0  # Stops continuous servo
            except Exception:
                pass
        print("All motors cleaned up safely.")
    except Exception as e:
        print(f"Failed to initialize ServoKit: {e}")

if __name__ == "__main__":
    clean_all_servos()