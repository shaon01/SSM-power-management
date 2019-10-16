
// realy input pins
#define RELAY_1_OUTPUT      13    //relay 1
#define RELAY_2_OUTPUT      12    //relay 2
#define RELAY_3_OUTPUT      11    //relay 3
#define RELAY_4_OUTPUT      10    //relay 4
#define RELAY_5_OUTPUT      9     //relay 5
#define RELAY_6_OUTPUT      8     //relay 6
#define RELAY_7_OUTPUT      7     //relay 7
#define RELAY_8_OUTPUT      6     //relay 8

//output Status for KL15
#define RELAY_1_ON        LOW
#define RELAY_1_OFF       HIGH  

//output Status for KL30 A-side
#define RELAY_2_ON        LOW
#define RELAY_2_OFF       HIGH  

//output Status for KL30 B-side
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

//input from user over serial for kl15
#define KL_15_ON    'k'
#define KL_15_OFF   'f'

//input from user over serial for kl30 A-side
#define KL_30_A_ON    'q'
#define KL_30_A_OFF   'w'

//input from user over serial for kl30 B-side
#define KL_30_B_ON    'e'
#define KL_30_B_OFF   'r'

//input from user over serial for kl30 (both sides)
#define KL_30_ON    'p'
#define KL_30_OFF   's'

//input from user over serial for turning all the power
#define SYSTEM_ON        'd'
#define SYSTEM_DOWN      'h'

#define IO_STATUS        'i'

//input from user for Q-diode DTCs
#define DTC_EF3011       'z'
#define DTC_EF3012       'x'
#define DTC_EF3013       'c'
#define DTC_None         'v'

boolean debuggState = false;

int kl15_State = RELAY_1_ON;
int kl30_A_State = RELAY_2_ON;
int kl30_B_State = RELAY_3_ON;

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
  digitalWrite(RELAY_1_OUTPUT,kl15_State);
  digitalWrite(RELAY_2_OUTPUT,kl30_A_State);
  digitalWrite(RELAY_3_OUTPUT,kl30_B_State);
  digitalWrite(RELAY_4_OUTPUT,relay4State);
  digitalWrite(RELAY_5_OUTPUT,relay5State);
  digitalWrite(RELAY_6_OUTPUT,relay6State);
  digitalWrite(RELAY_7_OUTPUT,relay7State);
  //digitalWrite(RELAY_8_OUTPUT,relay8State);
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

    // Enable/disable KL15 
    case KL_15_ON:
      kl15_State = RELAY_1_ON;
      break;

    case KL_15_OFF:
      kl15_State = RELAY_1_OFF;
      break;

    // Enable/disable KL30 (A and B side)

    case KL_30_A_ON:
      kl30_A_State = RELAY_2_ON;
      break;

    case KL_30_A_OFF:
      kl30_A_State = RELAY_2_OFF;
      break;
      
    case KL_30_B_ON:
      kl30_B_State = RELAY_3_ON;
      break;

    case KL_30_B_OFF:
      kl30_B_State = RELAY_3_OFF;
      break;

    case KL_30_ON:
      kl30_A_State = RELAY_3_ON;
      kl30_B_State = RELAY_3_ON;
      break;

    case KL_30_OFF:
      kl30_A_State = RELAY_3_OFF;
      kl30_B_State = RELAY_3_OFF;
      break;

      

    // Enable/disable Systm down
    case SYSTEM_DOWN:
      kl15_State = RELAY_1_OFF;
      kl30_A_State = RELAY_2_OFF;
      kl30_B_State = RELAY_3_OFF;
      break;

    case SYSTEM_ON:
      kl15_State = RELAY_1_ON;
      kl30_A_State = RELAY_2_ON;
      kl30_B_State = RELAY_3_ON;
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
      Serial.write('f');
      Serial.print(kl15_State);
      //write kl15 state
      Serial.write('t');
      Serial.println(kl30_A_State);
      break;
      
    default:
      break;
    
    }
    
  if(debuggState){
    Serial.print("\n KL_15_A state :");
    Serial.println(kl15_State);
    Serial.println("\n");
    Serial.print("\n SSM_A KL_30 state A-side:");
    Serial.println(kl30_A_State);
    Serial.print("\n SSM_A KL_30 state B-side:");
    Serial.println(kl30_B_State);
    Serial.println("\n");
    
  }
  
}
