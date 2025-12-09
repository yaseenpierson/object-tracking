# Arduino Servo Object Tracking (OpenCV)

This project uses OpenCV on a computer to detect an object and sends servo angle values to an Arduino.  
The Arduino controls two servos (horizontal and vertical) to keep the object centered in the camera view.
![img111](https://github.com/user-attachments/assets/0c69f436-d478-47c4-ad88-65c8becae647)
---

## Features
- Real-time object tracking using OpenCV  
- Arduino-controlled servo movement  
- Supports two servos  


---

## Requirements
- Arduino board  
- 2 Servo motors (SG90) 
- Webcam  (laptop)
- Python 3  

Install Python packages:
```
pip install opencv-python numpy pyserial
```

---

## How It Works
1. OpenCV captures frames from the webcam  
2. Python script detects an object
3. Script calculates the object's position  
4. Position is mapped to a servo angle  
5. Angle is sent to Arduino through Serial  
6. Arduino moves the servo to track the object  

---

## Wiring
- Servo signal → **D9**  
- Servo 5V → 5V arduino pin 
- Servo GND → Arduino GND  
- Second servo: Signal → **D10**
- Servo 5V → 5V arduino pin 
- Servo GND → Arduino GND  


## Project Structure
```
forservoarduino.ino
objtrack.py
README.md
```

---

## Running the Project
1. Upload the Arduino code  
2. Run the Python script:
```
objtrack.py
```
3. Move the object → servo follows it  

---

## Notes
- Make sure the correct COM port is selected  

---


