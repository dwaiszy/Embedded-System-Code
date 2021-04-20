// This #include statement was automatically added by the Particle IDE.
#include <BH1750Lib.h>

//debug to serial port
#define UARTDEBUG 1

//initialize device
BH1750Lib bh1750 = BH1750Lib();

void setup() {
    bh1750.begin(BH1750LIB_MODE_CONTINUOUSHIGHRES);
    
  
#if UARTDEBUG == 1
    Serial.begin(9600);
    Serial.println("Starting...");
#endif
}

void loop() {
    int luxvalue = bh1750.lightLevel();
    //monitoring the light lelvel using BH1750 Lib and set as luxvalue

    char szEventInfo[64];
    sprintf(szEventInfo, "Light = %d lux", luxvalue);
    //print lux value

    //Add on 
    Particle.variable("Warning: bh1750", &luxvalue, INT);
    //Use this line to send data to IFTTT
    Spark.publish("bh1750", szEventInfo);
    //print lux value 
    
#if UARTDEBUG == 1
    //read
    Serial.print("Light: ");
    Serial.print(luxvalue);
    Serial.println("lux");
    //serial print
    
#endif
    
    //wait for the next reading
    delay(2000);
}
