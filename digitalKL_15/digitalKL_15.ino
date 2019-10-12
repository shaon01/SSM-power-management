
// realy 1 input pins
#define KL_15_OUTPUT        12   //relay 4
#define KL_30_OUTPUT        7    //relay 2

// realy 2 input pins
#define RELAY_21_OUTPUT      6    //relay 1
#define RELAY_22_OUTPUT      9    //relay 2
#define RELAY_23_OUTPUT      10   //relay 3
#define RELAY_24_OUTPUT      11   //relay 4

//output Status for KL15
#define KL15_IO_ON        LOW
#define KL15_IO_OFF       HIGH	

//output Status for KL30
#define KL30_IO_ON        LOW
#define KL30_IO_OFF       HIGH

//output Status for relay 2.1
#define RELAY_21_ON        HIGH
#define RELAY_21_OFF       LOW

//output Status for relay 2.2
#define RELAY_22_ON        HIGH
#define RELAY_22_OFF       LOW

//output Status for relay 2.3
#define RELAY_23_ON        HIGH
#define RELAY_23_OFF       LOW

//output Status for relay 2.4
#define RELAY_24_ON        HIGH
#define RELAY_24_OFF       LOW

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

//input from user for Q-diode DTCs
#define DTC_EF3011       'z'
#define DTC_EF3012       'x'
#define DTC_EF3013       'c'
#define DTC_None         'v'

boolean debuggState = false;

int kl15State = KL15_IO_ON;
int kl30State = KL30_IO_ON;

int relay21State = RELAY_21_OFF;
int relay22State = RELAY_22_ON;
int relay23State = RELAY_23_OFF;
int relay24State = RELAY_24_ON;


void setup() {
  //initially KL_15 is on
  pinMode(KL_15_OUTPUT,OUTPUT);
  pinMode(KL_30_OUTPUT,OUTPUT);

  // Initialize Relay 2 pins
  pinMode(RELAY_21_OUTPUT,OUTPUT);
  pinMode(RELAY_22_OUTPUT,OUTPUT);
  pinMode(RELAY_23_OUTPUT,OUTPUT);
  pinMode(RELAY_24_OUTPUT,OUTPUT);
  
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

}

void loop() {
 
 //controlling kl_15 output
  digitalWrite(KL_15_OUTPUT,kl15State);
  //controlling kl_30 output
  digitalWrite(KL_30_OUTPUT,kl30State);

  /*Set output for DTC pins*/
  digitalWrite(RELAY_21_OUTPUT,relay21State);
  digitalWrite(RELAY_22_OUTPUT,relay22State);
  digitalWrite(RELAY_23_OUTPUT,relay23State);
  digitalWrite(RELAY_24_OUTPUT,relay24State);
  
}



void serialEvent() {

  char serialInput[10];
  int index = 0;
  static int maxIndexCount = 5;

  while(Serial.available() > 0) // Don't read unless
  {
      
        serialInput[index] = Serial.read();
        Serial.print("current value :");
        Serial.println(serialInput[index]);
        index++;
      
   }

  switch (serialInput[0]){
    
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

    // Short-to-ground, DTC - EF3011
    case DTC_EF3011:
      relay21State = RELAY_21_OFF;
      relay22State = RELAY_22_OFF;
      relay23State = RELAY_23_ON;
      relay24State = RELAY_24_ON;
      break;

    // Short-to-battery, DTC -EF3012
    case DTC_EF3012:
      relay21State = RELAY_21_ON;
      relay22State = RELAY_22_OFF;
      relay23State = RELAY_23_OFF;
      relay24State = RELAY_24_OFF;
      break;

    // Open circuit, DTC - EF3013
    case DTC_EF3013:
      relay21State = RELAY_21_OFF;
      relay22State = RELAY_22_OFF;
      relay23State = RELAY_23_OFF;
      relay24State = RELAY_24_OFF;
      break;
      
    // Normal behavior, DTC - None
    case DTC_None:
      relay21State = RELAY_21_OFF;
      relay22State = RELAY_22_ON;
      relay23State = RELAY_23_OFF;
      relay24State = RELAY_24_ON;
      break;
      
    case IO_STATUS:
      //write kl15 state
      Serial.write('f');
      Serial.print(kl15State);
      //write kl15 state
      Serial.write('t');
      Serial.println(kl30State);
      break;
      
    default:
      break;
    
    
    }
    
  if(debuggState){
    Serial.print("\n KL_15 state :");
    Serial.println(kl15State);
    Serial.println("\n");
    Serial.print("\n SSM_A KL_30 state :");
    Serial.println(kl30State);
    Serial.println("\n");
    
  }
  
}
