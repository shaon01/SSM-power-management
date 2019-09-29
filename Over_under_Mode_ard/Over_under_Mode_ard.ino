#ifdef ARDUINO_SAMD_VARIANT_COMPLIANCE
  #define RefVal 3.3
  #define SERIAL SerialUSB
#else
  #define RefVal 5.0
  #define SERIAL Serial
#endif
//An OLED Display is required here
//use pin A0
#define CURNT_SENS_PIN A5

// Take the average of 500 times

const int averageValue = 1000;

long int sensorValue = 0;

float sensitivity = 1000.0 / 200.0; //1000mA per 200mV 


float Vref = 1508.79;

#define PWM_VALUE 20
#define PWM_PIN   3

void setup() 
{
  TCCR2B = TCCR2B & B11111000 | B00000001; // for PWM frequency of 31372.55 Hz
  pinMode(PWM_PIN,OUTPUT);
  SERIAL.begin(9600);
}

void loop() 
{
  //control PWM signal
  analogWrite(PWM_PIN,PWM_VALUE);

  // Read the value 500 times:
  for (int i = 0; i < averageValue; i++)
  {
    sensorValue += analogRead(CURNT_SENS_PIN);

    // wait 2 milliseconds before the next loop
    delay(2);

  }

  float averageSensorValue = sensorValue / averageValue;
  SERIAL.print("Average ADC reading: ");
  SERIAL.println(averageSensorValue);


  // The on-board ADC is 10-bits 
  // Different power supply will lead to different reference sources
  // example: 2^10 = 1024 -> 5V / 1024 ~= 4.88mV
  //          unitValue= 5.0 / 1024.0*1000 ;
  float unitValue= RefVal / 1024.0*1000 ;
  float voltage = unitValue * averageSensorValue; 

  //When no load,Vref=initialValue
  SERIAL.print("initialValue: ");
  SERIAL.print(voltage);
  SERIAL.println("mV"); 

  // Calculate the corresponding current
  float current = (voltage - Vref) * sensitivity;

  // Print display voltage (mV)
  // This voltage is the pin voltage corresponding to the current
  /*
  voltage = unitValue * sensorValue-Vref;
  SERIAL.print(voltage);
  SERIAL.println("mV");
  */

  // Print display current (mA)
  SERIAL.print(current);
  SERIAL.println("mA");

  SERIAL.print("\n");

  // Reset the sensorValue for the next reading
  sensorValue = 0;
  // Read it once per second
  delay(1000);
}
