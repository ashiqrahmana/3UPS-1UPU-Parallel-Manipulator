int count = 0;

void detectChange(){
  Serial.println(count++);
}

void setup() {
  // put your setup code here, to run once:
  attachInterrupt(digitalPinToInterrupt(0),detectChange,CHANGE);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(0,LOW);
  delay(1000);
}
