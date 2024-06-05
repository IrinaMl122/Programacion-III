int buzzPin = 8;
int number;
String msgl = "Por favor INGRESE su numero";
int dt = 500;

void setup()
{
  Serial.begin (9600);
  pinMode (buzzPin, OUTPUT);
}

void loop()
{
  Serial.println();
  Serial.println(msgl);
  while (Serial.available() == 0) {
  }
  number = Serial.parseInt();
  if (number > 10) {
    digitalWrite (buzzPin, HIGH);
    delay (dt);
    digitalWrite (buzzPin, LOW);
}
}
