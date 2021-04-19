//Nhi Nguyen - Blinking LED - Student ID: 219007981

int name_led = D7; //set name led and pin is D7

void setup() {

  //pinMode(led1, OUTPUT);
  pinMode(name_led, OUTPUT);

}

//An extra function that use to flash the LED
void flash(int deltaTime) {
    digitalWrite(name_led, HIGH);
    delay(deltaTime);
    digitalWrite(name_led, LOW);
    delay(1000);
}

// Main function
void loop() {
  // Morse code for character 'N' : --- -
  flash(3000);
  flash(1000);

  // short break before moving on to new character;
  flash(1000);

  // morse code for character 'H' : - - - -
  for (int i=0; i<4; i++)
  {
      flash(1000);
  }
  
  // short break before moving on to new character;
  flash(1000);
  
  // morse code for character 'I' : - - 
  for (int i=0; i<2; i++)
  {
      flash(1000);
  }
  // And repeat!
}

