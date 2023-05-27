int motor_enb[5] = {10,12,14,19,18};
int motor_dir[5] = {11,13,15,17,16};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 2; i++){
    pinMode(motor_dir[i], OUTPUT);
    pinMode(motor_enb[i], OUTPUT);
  }
  Serial.println("Done assiging pins");
  Serial.println("Lets Begin the encoder test");
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 0; i < 1; i++){
      digitalWrite(motor_dir[i], HIGH);
      analogWrite(motor_enb[i], 10);
      Serial.println("Forward");
      delay(3000);
      digitalWrite(motor_dir[i], LOW
      );
      analogWrite(motor_enb[i], 10);
      Serial.println("Backward");
      delay(3000);
      analogWrite(motor_enb[i], 0);
      Serial.println("Stopped");   
      delay(3000);   
      Serial.println(i);
  } 
}
