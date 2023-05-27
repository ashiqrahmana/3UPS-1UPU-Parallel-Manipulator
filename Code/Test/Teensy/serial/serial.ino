void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 2){
    String data = Serial.readStringUntil("\n");
    Serial.println("Hi I am Teensy");
  }
  else{
    Serial.println("oops!! didnt recieve anything");
  }
}
