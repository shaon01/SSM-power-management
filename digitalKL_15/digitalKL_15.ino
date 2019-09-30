
// realy input pins
#define RELAY_1_OUTPUT      6    //relay 1
#define RELAY_2_OUTPUT      7    //relay 2
#define RELAY_3_OUTPUT      8    //relay 3
#define RELAY_4_OUTPUT      9    //relay 4
#define RELAY_5_OUTPUT      19   //relay 5
#define RELAY_6_OUTPUT      11   //relay 6
#define RELAY_7_OUTPUT      12   //relay 7
#define RELAY_8_OUTPUT      13   //relay 8

//output Status for KL15 A-side
#define RELAY_1_ON        LOW
#define RELAY_1_OFF       HIGH  

//output Status for KL15 B-side
#define RELAY_2_ON        LOW
#define RELAY_2_OFF       HIGH  

//output Status for KL30
#define RELAY_3_ON        LOW
#define RELAY_3_OFF       HIGH

//output Status for relay 4 - Q-didoe
#define RELAY_4_ON        HIGH
#define RELAY_4_OFF       LOW

//output Status for relay 5 - Q-didoe
#define RELAY_5_ON        HIGH
#define RELAY_5_OFF       LOW

//output Status for relay 6 - Q-didoe
#define RELAY_6_ON        HIGH
#define RELAY_6_OFF       LOW

//output Status for relay 7 - Q-didoe
#define RELAY_7_ON        HIGH
#define RELAY_7_OFF       LOW

//output Status for relay 8
//#define RELAY_8_ON        HIGH
//#define RELAY_8_OFF       LOW

//input from user over serial for kl15 A-side
#define KL_15_A_ON    'q'
#define KL_15_A_OFF   'w'

//input from user over serial for kl15 B-side
#define KL_15_B_ON    'e'
#define KL_15_B_OFF   'r'

//input from user over serial for kl30
#define KL_30_ON    'a'
#define KL_30_OFF   's'

//input from user over serial for turning all the power
#define SYSTEM_ON        'd'
#define SYSTEM_DOWN      'f'

#define IO_STATUS        'i'

//input from user for Q-diode DTCs
#define DTC_EF3011       'z'
#define DTC_EF3012       'x'
#define DTC_EF3013       'c'
#define DTC_None         'v'

boolean debuggState = false;

int kl15_A_State = RELAY_1_ON;
int kl15_B_State = RELAY_2_ON;
int kl30State = RELAY_3_ON;

int relay4State = RELAY_4_OFF;
int relay5State = RELAY_5_ON;
int relay6State = RELAY_6_OFF;
int relay7State = RELAY_7_ON;


void setup() {
  // Initialize Relay pins
  pinMode(RELAY_1_OUTPUT,OUTPUT);
  pinMode(RELAY_2_OUTPUT,OUTPUT);
  pinMode(RELAY_3_OUTPUT,OUTPUT);
  pinMode(RELAY_4_OUTPUT,OUTPUT);
  pinMode(RELAY_5_OUTPUT,OUTPUT);
  pinMode(RELAY_6_OUTPUT,OUTPUT);
  pinMode(RELAY_7_OUTPUT,OUTPUT);
  //pinMode(RELAY_8_OUTPUT,OUTPUT);
  
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

}

void loop() {
 
  /*Set output for DTC pins*/
  digitalWrite(RELAY_1_OUTPUT,kl15_A_State);
  digitalWrite(RELAY_2_OUTPUT,kl15_B_State);
  digitalWrite(RELAY_3_OUTPUT,kl30State);
  digitalWrite(RELAY_4_OUTPUT,relay4State);
  digitalWrite(RELAY_1_OUTPUT,relay5State);
  digitalWrite(RELAY_2_OUTPUT,relay6State);
  digitalWrite(RELAY_3_OUTPUT,relay7State);
  //digitalWrite(RELAY_4_OUTPUT,relay8State);
}



void serialEvent() {
  
  char serialInput;
  while (Serial.available()) {
    // get the new byte:
    serialInput = (char)Serial.read();

    if(debuggState){
      Serial.print("\n serial reading of KL_15 :");
      Serial.println(serialInput);
    }

  }

  switch (serialInput){

    // Enable/disable KL15 (A and B side)
    case KL_15_A_ON:
      kl15_A_State = RELAY_1_ON;
      break;

    case KL_15_A_OFF:
      kl15_A_State = RELAY_1_OFF;
      break;

    case KL_15_B_ON:
      kl15_B_State = RELAY_2_ON;
      break;

    case KL_15_B_OFF:
      kl15_B_State = RELAY_2_OFF;
      break;

    // Enable/disable KL30
    case KL_30_ON:
      kl30State = RELAY_3_ON;
      break;

    case KL_30_OFF:
      kl30State = RELAY_3_OFF;
      break;

    // Enable/disable Systm down
    case SYSTEM_DOWN:
      kl15_A_State = RELAY_1_OFF;
      kl15_B_State = RELAY_2_OFF;
      kl30State = RELAY_3_OFF;
      break;

    case SYSTEM_ON:
      kl15_A_State = RELAY_1_ON;
      kl15_B_State = RELAY_2_ON;
      kl30State = RELAY_3_ON;
      break;

    // Short-to-ground, DTC - EF3011
    case DTC_EF3011:
      relay4State = RELAY_4_OFF;
      relay5State = RELAY_5_OFF;
      relay6State = RELAY_6_ON;
      relay7State = RELAY_7_ON;
      break;

    // Short-to-battery, DTC -EF3012
    case DTC_EF3012:
      relay4State = RELAY_4_ON;
      relay5State = RELAY_5_OFF;
      relay6State = RELAY_6_OFF;
      relay7State = RELAY_7_OFF;
      break;

    // Open circuit, DTC - EF3013
    case DTC_EF3013:
      relay4State = RELAY_4_OFF;
      relay5State = RELAY_5_OFF;
      relay6State = RELAY_6_OFF;
      relay7State = RELAY_7_OFF;
      break;
      
    // Normal behavior, DTC - None
    case DTC_None:
      relay4State = RELAY_4_OFF;
      relay5State = RELAY_5_ON;
      relay6State = RELAY_6_OFF;
      relay7State = RELAY_7_ON;
      break;
      
    case IO_STATUS:
      //write kl15 state
      Serial.print("KL15 A-side: ");
      Serial.print(kl15_A_State);

      Serial.print("KL15 B-side: ");
      Serial.print(kl15_B_State);    
      
      //write kl15 state
      Serial.print("KL30: ");
      Serial.println(kl30State);
      break;
      
    default:
      break;
    
    }
    
  if(debuggState){
    Serial.print("\n KL_15_A state :");
    Serial.println(kl15_A_State);
    Serial.print("\n KL_15_B state :");
    Serial.println(kl15_B_State);
    Serial.println("\n");
    Serial.print("\n SSM_A KL_30 state :");
    Serial.println(kl30State);
    Serial.println("\n");
    
  }
  
}
