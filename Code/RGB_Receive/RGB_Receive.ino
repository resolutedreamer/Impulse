// color swirl! connect an RGB LED to the PWM pins as indicated
// in the #defines
// public domain, enjoy!

#define REDPIN 3
#define GREENPIN 5
#define BLUEPIN 6

#define FADESPEED 5     // make this higher to slow down
int color = 0;
void setup() {
  Serial.begin(9600);
  pinMode(REDPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT);
}


void loop() {
  if(Serial.available()>0){
    char data = Serial.read();
    char str[2];
    str[0] = data;
    str[1] = '\0';
    color = String(str).toInt();
  }
    switch(color){
      case 0:
        digitalWrite(BLUEPIN, HIGH);
        digitalWrite(GREENPIN, LOW);
        digitalWrite(REDPIN, LOW);
        break;      
      case 1:
        digitalWrite(BLUEPIN, LOW);
        digitalWrite(GREENPIN, HIGH);
        digitalWrite(REDPIN, LOW);
        break;       
      case 2:
        digitalWrite(BLUEPIN, HIGH);
        digitalWrite(GREENPIN, HIGH);
        digitalWrite(REDPIN, LOW);
        break;
      case 3:
        digitalWrite(BLUEPIN, LOW);
        digitalWrite(GREENPIN, LOW);
        digitalWrite(REDPIN, HIGH);
        break;
      case 4:
        digitalWrite(BLUEPIN, HIGH);
        digitalWrite(GREENPIN, LOW);
        digitalWrite(REDPIN, HIGH);
        break;          
      case 5:
        digitalWrite(BLUEPIN, LOW);
        digitalWrite(GREENPIN, HIGH);
        digitalWrite(REDPIN, HIGH);
        break;        
      case 6:
        digitalWrite(REDPIN, HIGH);
        digitalWrite(GREENPIN, HIGH);
        digitalWrite(BLUEPIN, HIGH); 
        break;         
    }
  }
