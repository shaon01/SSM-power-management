
// realy input pins
#define KL_15_OUTPUT        12   //relay 4
#define KL_30_OUTPUT        7    //relay 2

//output Status for KL15
#define KL15_IO_ON        LOW
#define KL15_IO_OFF       HIGH
//output Status for KL30
#define KL30_IO_ON        LOW
#define KL30_IO_OFF       HIGH

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
  pinMode(KL_15_OUTPUT,OUTPUT);
  pinMode(KL_30_OUTPUT,OUTPUT);
  
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
