// This #include statement was automatically added by the Particle IDE.
#include <BH1750Lib.h>

//debug to serial port
#define UARTDEBUG 1

//initialize device
BH1750Lib bh1750 = BH1750Lib();

int led = D7;
int luxValue;

void setup() {
    pinMode(led, OUTPUT);
    
    bh1750.begin(BH1750LIB_MODE_CONTINUOUSHIGHRES);
    Particle.subscribe("bh1750", handler);
  
#if UARTDEBUG == 1
    Serial.begin(9600);
    Serial.println("Starting...");
#endif
}

//Buddy system
void handler(const char *event, const char* data) {
    if (luxValue > 200) {
        if (luxValue > 500) {
            digitalWrite(led, HIGH);
            delay(100);
            digitalWrite(led, LOW);
            delay(100);
        }
        
        digitalWrite(led, HIGH);
        delay(1000);
        digitalWrite(led, LOW);
        delay(1000);
    }
}

void loop() {
    luxValue = bh1750.lightLevel();
    //monitoring the light lelvel using BH1750 Lib and set as luxvalue

    char szEventInfo[64];
    sprintf(szEventInfo, "Light = %d lux", luxValue);
    //print lux value

    Particle.variable("Warning: bh1750", &luxValue, INT);
    //Use this line to send data to IFTTT
    Particle.publish("bh1750", szEventInfo);
    //print lux value 
    
#if UARTDEBUG == 1
    //read
    Serial.print("Light: ");
    Serial.print(luxValue);
    Serial.println("lux");
    //serial print
    
#endif
    
    //wait for the next reading
    delay(5000);
}
