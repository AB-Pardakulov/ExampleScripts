// Abdullojon Pardakulov
// ODD 3/4
// 1/24/2023
// Project 2.A Functional RGB 
int redLED = 9, greenLED = 10, blueLED = 11; //Initalizing all needed variables
// int push_value; Uneeded
float potential_value;
// int cycle_value; Uneeded
float brightness = 1;
void blink(int times) // Blinking the basic rgb int times
{
  for (int i=0; i < times;i++)
  {
     digitalWrite(2, LOW);
     delay(105);
     digitalWrite(2, HIGH);
     delay(105);
  }
  digitalWrite(2, HIGH);
}
void rgb_brightness_or_loop_runtime(int red, int blue, int green) // Controls each LED change and reads potentiometer
{
 // For Anode RGB
 potential_value = analogRead(A0);
 Serial.println(potential_value);
 brightness = potential_value / 1023;
 analogWrite(redLED, (255-red*brightness));
 analogWrite(greenLED, (255-green*brightness));
 analogWrite(blueLED, (255-blue*brightness));
 delay(50);
}
void rgb_shift(int r, int g, int b, int rt, int gt, int bt, int rl, int gl, int bl) // Shifts between 3 rgb values using number interpolation
{
rgb_brightness_or_loop_runtime(r,g,b);
delay(30);
rgb_brightness_or_loop_runtime(r*0.75+rt*0.25,g*0.75+gt*0.25,b*0.75+bt*0.25);
rgb_brightness_or_loop_runtime((r+rt)/2,(g+gt)/2,(b+bt)/2);
rgb_brightness_or_loop_runtime(r*0.25+rt*0.75,g*0.25+gt*0.75,b*0.25+bt*0.75);
rgb_brightness_or_loop_runtime(rt,gt,bt);
delay(30);
rgb_brightness_or_loop_runtime(rl*0.25+rt*0.75,gl*0.25+gt*0.75,bl*0.25+bt*0.75);
rgb_brightness_or_loop_runtime((rl+rt)/2,(gl+gt)/2,(bl+bt)/2);
rgb_brightness_or_loop_runtime(rl*0.75+rt*0.25,gl*0.75+gt*0.25,bl*0.75+bt*0.25);
rgb_brightness_or_loop_runtime(rl,gl,bl);
delay(30);
}
void setup() // Initalizes all needed pins
{
  pinMode(2, OUTPUT);
  pinMode(3, INPUT);
  pinMode(A0, INPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
}
void loop() // Loop initzalizes the fade on each press after it is completed
{
for (int i=0; digitalRead(3) == 1;i++)
{
digitalWrite(2, HIGH);
analogWrite(redLED, 255);
analogWrite(greenLED, 255);
analogWrite(blueLED, 255);
}
blink(1); // Blinking the basic LED
rgb_shift(255,0,0,191,63,0,128,128,0); // The numbers used to create the fade
rgb_shift(128,128,0,63,191,0,0,255,0);
blink(2);
rgb_shift(0,255,0,0,191,63,0,128,128);
rgb_shift(0,128,128,0,63,191,0,0,255);
blink(3);
rgb_shift(0,0,255,63,0,191,128,0,128);
rgb_shift(128,0,128,191,0,63,255,0,0);
}