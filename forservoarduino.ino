#include <Servo.h>

Servo servoX;
Servo servoY;
int servoXpos = 90;
int servoYpos = 90;

void setup() {
  servoX.attach(9);
  servoY.attach(10);
  Serial.begin(9600);
  Serial.println("Ready...");
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    int xIndex = data.indexOf('X');
    int yIndex = data.indexOf('Y');

    if (xIndex != -1 && yIndex != -1) {
      int x = data.substring(xIndex + 1, yIndex).toInt();
      int y = data.substring(yIndex + 1).toInt();

      Serial.print("Received: ");
      Serial.print(x);
      Serial.print(", ");
      Serial.println(y);

      servoXpos = map(x, 0, 640, 0, 180);
      servoYpos = map(y, 0, 480, 0, 180);

      // keep angles in safe range
      servoXpos = constrain(servoXpos, 0, 180);
      servoYpos = constrain(servoYpos, 0, 180);

      servoX.write(servoXpos);
      servoY.write(servoYpos);
      delay(15);
    }
  }
}
