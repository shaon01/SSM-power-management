
// realy input pins
#define KL_15_OUTPUT        12   //relay 4
#define KL_30_OUTPUT        7    //relay 3

/*CAN bus controlling relay defination*/
#define CAN_H_2_GND_REL_1     9 //realy 1
#define CAN_L_2_KL30_REL_2    10 //realy 2
#define CAN_H_2_CAN_L_REL_3   11 //realy 3

/*CAN bus relay status*/
#define CAN_RELAY_ON      HIGH
#define CAN_RELAY_OFF     LOW

//output Status for KL15
#define KL15_IO_ON        LOW
#define KL15_IO_OFF       HIGH
//output Status for KL30
#define KL30_IO_ON        LOW
#define KL30_IO_OFF       HIGH



/*CAN error generation key*/
#define CAN_H_2_GND_ON      'a'
#define CAN_H_2_GND_OFF     'b'
#define CAN_L_2_KL30_ON     'c'
#define CAN_L_2_KL30_OFF    'f'
#define CAN_H_2_CAN_L_ON    'e'
#define CAN_H_2_CAN_L_OFF   'g'

/*Bus off time for can*/
#define BUS_OFF_TIME_L2         1000
#define BUS_OFF_TIME_L1         10

//input from user over serial for kl15
#define KL_15_USER_ON    'k'
#define KL_15_USER_OFF   'f'

//input from user over serial for kl15
#define KL_30_USER_ON    'p'
#define KL_30_USER_OFF   's'

//input from user over serial for turning all the power
#define SYSTEM_ON        'h'
#define SYSTEM_DOWN      'd'

#define IO_STATUS        'i'

boolean debuggState = false;

int kl15State = KL15_IO_ON;
int kl30State = KL30_IO_ON;



void setup() {
  //initially KL_15 is on
  pinMode(KL_15_OUTPUT, OUTPUT);
  pinMode(KL_30_OUTPUT, OUTPUT);
  /*CAN realy Initialize*/
  pinMode(CAN_H_2_GND_REL_1, OUTPUT);
  pinMode(CAN_L_2_KL30_REL_2, OUTPUT);
  pinMode(CAN_H_2_CAN_L_REL_3, OUTPUT);

  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

}

void loop() {

  //controlling kl_15 output
  digitalWrite(KL_15_OUTPUT, kl15State);
  //controlling kl_30 output
  digitalWrite(KL_30_OUTPUT, kl30State);
}



void serialEvent() {

  char serialInput[10];
  float temp = 0;
  float temp1 = 0;
  int index = 0;
  float exp1 = 0;
  static int maxIndexCount = 5;
  int busOffDelayTime = 0;
  
  while(Serial.available())
  {
    while (Serial.available() > 0) // Don't read unless
    {
      serialInput[index] = Serial.read();
      //Serial.print("current value :");
      //Serial.println(serialInput[index]);
      index++;
      delay(10);
        
    }

  }

  if (index <3)
  {
    busOffDelayTime = BUS_OFF_TIME_L1;
  }
  else
  {
    for (int i = 1; i < index-1; i++) {
      temp1 = (int(serialInput[i]) - '0');
      exp1 = pow(10, index-i-2);
      temp = temp + temp1 * exp1;
    }
    busOffDelayTime = int(round(temp)); // int(serialInput.substring(1))
  }
  
  Serial.print(" index:");
  Serial.println(index);
  Serial.print(" value  temp:");
  Serial.println(temp);
  Serial.print(" Bus off time:");
  Serial.println(busOffDelayTime);
  

  switch (serialInput[0]) {

    case KL_15_USER_ON:
      kl15State = KL15_IO_ON;
      break;

    case KL_15_USER_OFF:
      kl15State = KL15_IO_OFF;
      break;

    case KL_30_USER_ON:
      kl30State = KL30_IO_ON;
      break;

    case KL_30_USER_OFF:
      kl30State = KL30_IO_OFF;
      break;

    case SYSTEM_DOWN:
      kl15State = KL15_IO_OFF;
      kl30State = KL30_IO_OFF;
      break;

    case SYSTEM_ON:
      kl15State = KL15_IO_ON;
      kl30State = KL30_IO_ON;
      break;

    case IO_STATUS:
      //write kl15 state
      Serial.write('f');
      Serial.print(kl15State);
      //write kl15 state
      Serial.write('t');
      Serial.println(kl30State);
      break;

    case CAN_H_2_GND_ON:
      Serial.println("turning on can high to grownd");
      digitalWrite(CAN_H_2_GND_REL_1, CAN_RELAY_ON);
      Serial.print(" Bus off time:");
      Serial.println(busOffDelayTime);
      delay(busOffDelayTime);
      digitalWrite(CAN_H_2_GND_REL_1, CAN_RELAY_OFF);
      Serial.println("turning OFF can high to grownd");
      Serial.println("*******************************");
      break;

    case CAN_L_2_KL30_ON:
      Serial.println("turning on can low to KL30");
      digitalWrite(CAN_L_2_KL30_REL_2, CAN_RELAY_ON);
      Serial.print(" Bus off time:");
      Serial.println(busOffDelayTime);
      delay(busOffDelayTime);
      digitalWrite(CAN_L_2_KL30_REL_2, CAN_RELAY_OFF);
      Serial.println("turning OFF can low to KL30");
      Serial.println("*******************************");
      break;

    case CAN_H_2_CAN_L_ON:
      Serial.println("turning on can low to can high");
      digitalWrite(CAN_H_2_CAN_L_REL_3, CAN_RELAY_ON);
      Serial.print(" Bus off time:");
      Serial.println(busOffDelayTime);
      delay(busOffDelayTime);
      digitalWrite(CAN_H_2_CAN_L_REL_3, CAN_RELAY_OFF);
      Serial.println("turning OFF can low to can high");
      Serial.println("*******************************");
      break;

    default:
      break;


  }

  if (debuggState) {
    Serial.print("\n KL_15 state :");
    Serial.println(kl15State);
    Serial.println("\n");
    Serial.print("\n SSM_A KL_30 state :");
    Serial.println(kl30State);
    Serial.println("\n");

  }

}
