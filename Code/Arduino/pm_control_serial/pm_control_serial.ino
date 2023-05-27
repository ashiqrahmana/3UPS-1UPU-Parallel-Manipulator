/* Encoder Library - Basic Example
   http://www.pjrc.com/teensy/td_libs_Encoder.html

   This example code is in the public domain.
*/

#include <PID_v1.h>
#include <Encoder.h>

Encoder myEnc1(0, 1);
Encoder myEnc2(2, 3);
Encoder myEnc3(4, 5);
Encoder myEnc4(6, 7);
Encoder myEnc5(8, 9);

//Define Variables we'll be connecting to
double Setpoint[5], Input[5], Output[5];

//Specify the links and initial tuning parameters
double Kp[5] = {10,10,10,10,10}, Ki[5] = {1,1,1,1,1}, Kd[5] = {0,0,0,0,0};

PID myPID1(&Input[0], &Output[0], &Setpoint[0], Kp[0], Ki[0], Kd[0], DIRECT);
PID myPID2(&Input[1], &Output[1], &Setpoint[1], Kp[1], Ki[1], Kd[1], DIRECT);
PID myPID3(&Input[2], &Output[2], &Setpoint[2], Kp[2], Ki[2], Kd[2], DIRECT);
PID myPID4(&Input[3], &Output[3], &Setpoint[3], Kp[3], Ki[3], Kd[3], DIRECT);
PID myPID5(&Input[4], &Output[4], &Setpoint[4], Kp[4], Ki[4], Kd[4], DIRECT);

//Input[3] = {0.00,0.00,0.00};

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability 
//   Low Performance:  neither pin has interrupt capability

int max_ = 30;
int min_ = 0;

int motor_enb[5] = {10,12,14,19,18};
int motor_dir[5] = {11,13,15,17,16};

int limit[5] = {20,21,22,23,24};

// 28/360 = x/angle ==> angle = x*360/(28*gear ratio)
// new formula ==> x*8/( 28* 300) ==> x / 1050

// 100 rpm - 300.000
// 110 rpm - 272.727
// 120 rpm - 250.000
//     rpm - 180.000

void setup() {
  Serial.begin(9600);
  Serial.println("defining pins");
 
  for (int i = 0; i < 5; i++){
    pinMode(motor_dir[i], OUTPUT);
    pinMode(motor_enb[i], OUTPUT);
    pinMode(limit[i],INPUT);
    Setpoint[i] = 10;
  }
  
  callibrate_motor(1); 
  Serial.println("Setting PID ");
  myPID1.SetMode(AUTOMATIC);
  myPID2.SetMode(AUTOMATIC);
  myPID3.SetMode(AUTOMATIC);
  myPID4.SetMode(AUTOMATIC);
  myPID5.SetMode(AUTOMATIC);
}

float oldPosition[5]  = {-99,-99,-99,-99,-99};

void encode4life(int l,int index) {
    Setpoint[index] = l;
    long newPosition;
    //   avoid using pins with LEDs attached
    if (index == 0){
      newPosition = myEnc1.read();
      if (newPosition != oldPosition[index]) 
        oldPosition[index] = newPosition;
        Input[index] = (newPosition*8/( 28* 180 * 1));
      }
    else if (index == 1){
      newPosition = myEnc2.read();
      if (newPosition != oldPosition[index])
        oldPosition[index] = newPosition;
        Input[index] = (newPosition*8/( 28* 180 * 1.375));
      }
    else if (index == 2){
      newPosition = myEnc3.read();
      if (newPosition != oldPosition[index])
        oldPosition[index] = newPosition;
        Input[index] = (newPosition*8/( 28* 180 * 1.5));
      }
    
    else if (index == 3){
      newPosition = myEnc4.read();
      if (newPosition != oldPosition[index])
        oldPosition[index] = newPosition;
        Input[index] = (newPosition*8/( 28* 180 * 1.5));
      }
      
    else{
      newPosition = myEnc5.read();
      if (newPosition != oldPosition[index])
        oldPosition[index] = newPosition;
        Input[index] = (newPosition*8/( 28* 180 * 1.5));
      }  
    //Serial.println(oldPosition);
    if (index == 0)
      myPID1.Compute();
    else if (index == 1)
      myPID2.Compute();
    else if (index ==  2)
      myPID3.Compute();
    else if ( index == 3)
      myPID4.Compute();
    else if ( index == 4)
      myPID5.Compute();
    
    if (Setpoint[index] > Input[index]) {
      digitalWrite(motor_dir[index], LOW);
      analogWrite(motor_enb[index], Output[index]);
    }
    if (Setpoint[index] < Input[index]) {
      digitalWrite(motor_dir[index], HIGH);
      analogWrite(motor_enb[index], 255 - Output[index]);
//      analogWrite(motor_enb[index], Output[index]);
    }
    if (abs(abs(Setpoint[index])-abs(Input[index])) <= 0.1){
      analogWrite(motor_enb[index],0);
    }
}

void callibrate_motor(int a){
    while ( a == 1) {
        for(int i = 0; i < 5; i++){
          if (digitalRead(limit[i]) == 0){
              analogWrite(motor_enb[i],0);
            }
          else{
              digitalWrite(motor_dir[i], HIGH);
              analogWrite(motor_enb[i], 200);
            }
        }
        
        if (digitalRead(limit[0]) == 0 && digitalRead(limit[1]) == 0 && digitalRead(limit[2]) == 0 && digitalRead(limit[3]) == 0 && digitalRead(limit[4]) == 0){
      
          myEnc1.write(0);
          myEnc2.write(0);
          myEnc3.write(0);
          myEnc4.write(0);
          myEnc5.write(0);     
      
        for(int i = 0; i < 5; i++){
          digitalWrite(motor_dir[i], LOW);
          analogWrite(motor_enb[i], 255);
        }
        delay(2000);
        break;
      }
  }
}

void loop() {
  int index_1 = 0;
  int index_2 = 0;
  int index_3 = 0;
  int index_4 = 0;
  
  int l[5] = {0,0,0,0,0};
  String setpoints = "";
  setpoints = Serial.readStringUntil('f');
  Serial.setTimeout(0.01);
  
  index_1 = setpoints.indexOf(byte('b'));
  index_2 = setpoints.indexOf(byte('c'));
  index_3 = setpoints.indexOf(byte('d'));
  index_4 = setpoints.indexOf(byte('e'));

  // Setpoints all assigned 
  l[0] = (setpoints.substring(        0,          index_1)).toFloat();
  l[1] = (setpoints.substring(index_1+1,          index_2)).toFloat();
  l[2] = (setpoints.substring(index_2+1,          index_3)).toFloat();
  l[3] = (setpoints.substring(index_3+1,          index_4)).toFloat();
  l[4] = (setpoints.substring(index_4+1,setpoints.length())).toFloat();

  // Calling the encoder function
  for(int index=0; index<3; index++){
    encode4life(l[index],index);
  }
  
  Serial.println(" Input0:" + String(Input[0])+" Setpoint0:"+String(Setpoint[0])+" Input1:"+String(Input[1])+" Setpoint1:"+String(Setpoint[1])+" Input2:"+String(Input[2])+" Setpoint2:"+String(Setpoint[2])+" Input3:"+String(Input[3])+" Setpoint3:"+String(Setpoint[3])+" Input4:"+String(Input[4])+" Setpoint4:"+String(Setpoint[4]));
  
  if (digitalRead(limit[0]) == 0 || digitalRead(limit[1]) == 0 || digitalRead(limit[2]) == 0 || digitalRead(limit[3]) == 0 || digitalRead(limit[4]) == 0){
      analogWrite(motor_enb[0],0);
      analogWrite(motor_enb[1],0);
      analogWrite(motor_enb[2],0);
      analogWrite(motor_enb[3],0);
      analogWrite(motor_enb[4],0);
  }
}  
