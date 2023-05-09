char data;
int LED=3;
void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  
}
void loop() {
  while (Serial.available())
  {
    data = Serial.read();
  }
  if (data == '0')
  {
    analogWrite (LED ,0);
    delay (1000);
  }
  else if(data == '1')
  {
    analogWrite (LED ,127);
    delay(1000);
  }
  else if(data == '2')
  {
    analogWrite (LED ,150);
    delay(1000);
  }
  else if(data == '3')
  {
    analogWrite (LED ,200);
    delay(1000);
  }
  else if(data == '4')
  {
    analogWrite (LED ,255);
    delay(1000);
  }
}
