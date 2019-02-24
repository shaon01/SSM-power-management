

#define KL_15_OUTPUT  7
#define KL_30_OUTPUT  6

#define KL15_IO_ON       HIGH
#define KL15_IO_OFF      LOW
#define KL30_IO_ON       HIGH
#define KL30_IO_OFF      LOW

#define KL_15_USER_ON    'k'
#define KL_15_USER_OFF   'f'

#define KL_30_USER_ON    'p'
#define KL_30_USER_OFF   's'

#define SYSTEM_ON        'h'
#define SYSTEM_DOWN      'd'
#define SYSTEM_REBOOT    'r'

boolean debuggState = true;

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
  // put your main code here, to run repeatedly:
  


 //controlling kl_15 output
  digitalWrite(KL_15_OUTPUT,kl15State);
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

    case SYSTEM_REBOOT:
      rebootSystem();
      break;
      
    default:
      break;
    
    
    }
  if(debuggState){
    Serial.print("\n KL_15 state :");
    Serial.println(kl15State);
    Serial.println("\n");
    Serial.print("\n KL_30 state :");
    Serial.println(kl30State);
  }
}

void rebootSystem(){

  digitalWrite(KL_15_OUTPUT,KL15_IO_OFF);
  digitalWrite(KL_30_OUTPUT,KL30_IO_OFF);

  delay(1000);

  digitalWrite(KL_15_OUTPUT,KL15_IO_ON);
  digitalWrite(KL_30_OUTPUT,KL30_IO_ON);
  
  }
