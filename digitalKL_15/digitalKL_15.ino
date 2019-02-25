

#define KL_15_OUTPUT        6
#define KL_30_OUTPUT_SSM_A  7
#define KL_30_OUTPUT_SSM_B  8

#define KL15_IO_ON              LOW
#define KL15_IO_OFF             HIGH

#define SSM_A_KL30_IO_ON        LOW
#define SSM_A_KL30_IO_OFF       HIGH

#define SSM_B_KL30_IO_ON        HIGH
#define SSM_B_KL30_IO_OFF       LOW

#define KL_15_USER_ON    'k'
#define KL_15_USER_OFF   'f'

#define SSM_A_KL_30_USER_ON    'p'
#define SSM_A_KL_30_USER_OFF   's'

#define SSM_B_KL_30_USER_ON    'a'
#define SSM_B_KL_30_USER_OFF   'c'

#define SYSTEM_ON        'h'
#define SYSTEM_DOWN      'd'
#define SYSTEM_REBOOT    'r'

boolean debuggState = true;

int kl15State = KL15_IO_ON;
int SSM_A_kl30State = SSM_A_KL30_IO_ON;
int SSM_B_kl30State = SSM_B_KL30_IO_ON;

void setup() {
  //initially KL_15 is on
  pinMode(KL_15_OUTPUT,OUTPUT);
  pinMode(KL_30_OUTPUT_SSM_A,OUTPUT);
  pinMode(KL_30_OUTPUT_SSM_B,OUTPUT);
  
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
  digitalWrite(KL_30_OUTPUT_SSM_A,SSM_A_kl30State);
  digitalWrite(KL_30_OUTPUT_SSM_B,SSM_B_kl30State);
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

    case SSM_A_KL_30_USER_ON:
      SSM_A_kl30State = SSM_A_KL30_IO_ON;
      break;

    case SSM_A_KL_30_USER_OFF:
      SSM_A_kl30State = SSM_A_KL30_IO_OFF;
      break;

     case SSM_B_KL_30_USER_ON:
      SSM_B_kl30State = SSM_B_KL30_IO_ON;
      break;

    case SSM_B_KL_30_USER_OFF:
      SSM_B_kl30State = SSM_B_KL30_IO_OFF;
      break;

    case SYSTEM_DOWN:
      kl15State = KL15_IO_OFF;
      SSM_A_kl30State = SSM_A_KL30_IO_OFF;
      SSM_B_kl30State = SSM_B_KL30_IO_OFF;
      break;

    case SYSTEM_ON:
      kl15State = KL15_IO_ON;
      SSM_A_kl30State = SSM_A_KL30_IO_ON;
      SSM_B_kl30State = SSM_B_KL30_IO_ON;
      break;

      
    default:
      break;
    
    
    }
  if(debuggState){
    Serial.print("\n KL_15 state :");
    Serial.println(kl15State);
    Serial.println("\n");
    Serial.print("\n SSM_A KL_30 state :");
    Serial.println(SSM_A_kl30State);
    Serial.println("\n");
    Serial.print("\n SSM_B KL_30 state :");
    Serial.println(SSM_B_kl30State);
  }
}
