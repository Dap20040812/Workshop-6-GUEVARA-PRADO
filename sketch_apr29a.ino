#include <Wire.h>

#define SLAVE_ADDRESS 0x04

int temperaturePin = A0;

void setup() {
  Wire.begin(SLAVE_ADDRESS);
  Wire.onRequest(requestEvent);
}

void loop() {

}

void requestEvent(){
  int temperature = analogRead(temperaturePin);
  float voltage = temperature * (5.0 / 1023.0); 
  float celsius = (voltage - 0.5) * 100.0; 
  Wire.write(temperature); 
}
