
import cv2
import serial
import time

# --- Connect to Arduino (change COM port if needed) ---
arduino = serial.Serial('COM5', 9600)  # example COM5
time.sleep(2)  # allow time for Arduino to reset

# --- Open the camera ---
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Camera not detected.")
    exit()

# --- Let user select the object to track ---
ret, frame = cap.read()
if not ret:
    print("Error: Cannot read camera frame.")
    exit()

bbox = cv2.selectROI("Select Object", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select Object")

# --- Create a CSRT tracker ---
tracker = cv2.TrackerCSRT_create()  # for OpenCV 4.x
tracker.init(frame, bbox)

print("Tracking started... Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # --- Update tracker position ---
    success, box = tracker.update(frame)

    if success:
        (x, y, w, h) = [int(v) for v in box]
        cx, cy = x + w // 2, y + h // 2

        # Draw bounding box and center dot
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        # Send coordinates to Arduino
        data = f"X{cx}Y{cy}\n"
        arduino.write(data.encode())
        print(f"Sent: {data.strip()}")
    else:
        cv2.putText(frame, "Lost track...", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Object Tracking", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()