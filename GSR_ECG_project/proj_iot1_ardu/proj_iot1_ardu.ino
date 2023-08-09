#include <SensorCommunicationLib.h>
#include <Smoothed.h>

const int ECG=15;
const int GSR=4;
float gsr_val= 2;
float ecg_val=2;
float ecg_avg=0;
float gsr_avg=0;
 

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
  pinMode (16, INPUT);
  pinMode (17, INPUT);
  pinMode (GSR, INPUT);
  pinMode (ECG, INPUT);
}

//((1024+2(gsr_val/4)10000)/(512-(gsr_val/4))
void loop() {
  // put your main code here, to run repeatedly:

 if((digitalRead(16) == 1)||(digitalRead(17) == 1)){
//if(true){
    Serial.println('!');
}
else{

// gsr_val=((1024+2(gsr_val/4))/(512-(gsr_val/4));


float sum_ecg=0;
float sum_gsr=0;
 for(int i=0;i<16;i++){
  ecg_val=analogRead(ECG);
  gsr_val=analogRead(GSR);
  gsr_val=(gsr_val/4);
//  sensorVal= analogRead(GSR);
  sum_ecg+=ecg_val;
  sum_gsr+=gsr_val;
  delay(0.5);
 }
 ecg_avg=sum_ecg/16;
 gsr_avg=sum_gsr/16;
    Serial.print(gsr_avg);
  Serial.print(',');
  Serial.print(ecg_avg);
  Serial.print('\n');
}


 
  
 
}
