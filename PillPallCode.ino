#define LED_PIN_YELLOW 2
#define LED_PIN_GREEN 3
#define LED_PIN_BLUE 4
#define LED_PIN_RED 5
#define BUTTON_PIN 6
#define BUZZER_PIN 7

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_PIN_YELLOW, OUTPUT);
  pinMode(LED_PIN_GREEN, OUTPUT);
  pinMode(LED_PIN_BLUE, OUTPUT);
  pinMode(LED_PIN_RED, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(BUZZER_PIN, OUTPUT);
  unsigned long starttime, endtime;
  starttime = millis();
  endtime = starttime;
  digitalWrite(LED_PIN_YELLOW,HIGH);
  tone(BUZZER_PIN, 1000, 1);
  delay(1000);
  while ((endtime - starttime) <=30000) // do this loop for up to 1000mS
  {
    digitalWrite(LED_PIN_YELLOW, LOW);
    digitalWrite(LED_PIN_GREEN, LOW);
    digitalWrite(LED_PIN_BLUE, LOW);
    digitalWrite(LED_PIN_RED, LOW);
    Serial.println(digitalRead(BUTTON_PIN));
    endtime = millis();
  }
  while (true){
  int buttonState;
  buttonState = digitalRead(BUTTON_PIN);
  if(buttonState == LOW) {
    break;
  }
  digitalWrite(LED_PIN_GREEN, HIGH);
  digitalWrite(LED_PIN_BLUE, HIGH);
  tone(BUZZER_PIN, 1000);
  }
  noTone(BUZZER_PIN);
  digitalWrite(LED_PIN_GREEN, LOW);
  digitalWrite(LED_PIN_BLUE, LOW);
}

void loop() {

}









