int Counts[5]     = {0,0,0,0,0};
double distance[5] = {0,0,0,0,0};
double lead[5] = {0.8/90,0.8/90,0.8/90,360*6.92/1166,360*6.92/1166};
float CPR[5]      = {28,28,28,28,28};

const int enA[5] = {0,2,4,6,8};
const int enB[5] = {1,3,5,7,9};

volatile bool A[5]  = {0,0,0,0,0};
volatile bool B[5]  = {0,0,0,0,0};

float l[5] = {-99,-99,-99,-99,-99};
  
int curr_motor = 0;

void init_encoder(){
  /* Setup the interrupt pin */
  // put your setup code here, to run once:
  Serial.println("Initiating encoders ");
  for( int i  = 0; i < 5;i++){
    pinMode(enA[i], INPUT);
    pinMode(enB[i], INPUT);
  }
  attachInterrupt(digitalPinToInterrupt(enA[0]), enAUpdate0, CHANGE);
  attachInterrupt(digitalPinToInterrupt(enB[0]), enBUpdate0, CHANGE);
  
  attachInterrupt(digitalPinToInterrupt(enA[1]), enAUpdate1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(enB[1]), enBUpdate1, CHANGE);
  
  attachInterrupt(digitalPinToInterrupt(enA[2]), enAUpdate2, CHANGE);
  attachInterrupt(digitalPinToInterrupt(enB[2]), enBUpdate2, CHANGE);
  
  attachInterrupt(digitalPinToInterrupt(enA[3]), enAUpdate3, CHANGE);
  attachInterrupt(digitalPinToInterrupt(enB[3]), enBUpdate3, CHANGE);
  
  attachInterrupt(digitalPinToInterrupt(enA[4]), enAUpdate4, CHANGE);
  attachInterrupt(digitalPinToInterrupt(enB[4]), enBUpdate4, CHANGE);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);
  init_encoder();
  Serial.println("Done Initialising");
}

void loop() {
  serialInput();
  
  Serial.println( "Link "+ String(curr_motor) +  ": " + String(distance[curr_motor])+" || Setpoint "+ String(curr_motor) +  " : " + String(l[curr_motor])); 
  //Serial.println("------------------------------------------------------");
  if(abs(abs(distance[curr_motor]) - abs(l[curr_motor])) < 5 && distance[curr_motor]/l[curr_motor] > 0 ){
    curr_motor += 1;
  }
  curr_motor = 3;
  //distance[curr_motor] = PI*diameter[curr_motor]*Counts[curr_motor]/CPR[curr_motor];
  // put your main code here, to run repeatedly:
  for (int i = 0; i < 5; i++){
    distance[i] = lead[i]*Counts[i]/CPR[i];
    if ( i > 2){
      distance[i] = distance[i] + 90;
    }
    //Serial.println(distance[i]);
  }
  delay(50);
}
