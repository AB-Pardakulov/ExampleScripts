// Abdullojon Pardakulov
// 3/4 ODD
// Project 2.B I see what you did Theremin
// 1/24/2024
int buzz_pin = 7; // Initalizing all variables
int trigPin = 13;    
int echoPin = 12;
int potential_pin = A0;
int letter_index;
float potential_raw;
float potential_map;
float duration;   
float distance;
float sonic_distance;
float potential_value;
int c = 262, d = 294, e = 330, f = 349; //Defining the letters
int g = 392, a = 440, b = 494, C = 523;
float letter_list[] = {440, 494, 262, 523, 294, 330, 349, 392};
float read_sonic() //Reading the ultrasonic sensor
{
 digitalWrite(trigPin, HIGH);
 delayMicroseconds(10);
 digitalWrite(trigPin, LOW);
 duration = pulseIn(echoPin, HIGH);
 distance = 0.017 * duration;
 return distance;
}
int potential_read() //Reading the potentiometer
{
  potential_raw = analogRead(A0);
  potential_map = map(potential_raw, 0, 1023, 3, 30);
  return potential_map;
}
int passive_sing(int frequency, int delay1, int delay2) //Using the passive buzzer using frequency and delay
{
  tone(buzz_pin, frequency);
  delay(delay1);
  noTone(buzz_pin);
  delay(delay2);
  return 200;
}
void setup()
{
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT); //initzaling all pins
  pinMode(echoPin, INPUT);
  pinMode(buzz_pin, OUTPUT);
  pinMode(A0, INPUT);
}
void loop()
{
  sonic_distance = read_sonic();
  potential_value = potential_read();
  letter_index = int(floor(sonic_distance/3)); //Determing which note to play
  letter_index = letter_index % 8;
  passive_sing(letter_list[letter_index], potential_value*6, potential_value*3); //Inputting the needed paramters
  // Serial.println(sonic_distance);
  // Serial.println(potential_value);
  Serial.println(letter_index); //Printing which letter index is being played to the monitor
}
