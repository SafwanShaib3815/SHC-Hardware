#define MQ2Apin (0)
#define MQ2Dpin (7)
float sensorA_Value;  //variable to store sensor value
float sensorD_Value;
void setup()
{
  Serial.begin(9600); // sets the serial port to 9600
  Serial.println("Gas sensor warming up!");
  delay(20000); // allow the MQ-6 to warm up
}

void loop()
{
  sensorA_Value = analogRead(MQ2Apin); // read analog input pin 0
  sensorD_Value = digitalRead(MQ2Dpin);
  Serial.print("]Sensor Analog Value: ");
  Serial.print(sensorA_Value);
 
  if(sensorA_Value > 300)
  {
    Serial.print(" | Smoke detected!");
  }
  
  Serial.println("");

  Serial.print("\nSensor Digital Value: ");
  Serial.print(sensorD_Value);
  delay(1000); // wait 1s for next reading
}
