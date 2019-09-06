#include "config.h"
#include "Arduino.h"
#include "DigiCDC.h"

char cdc_input;
boolean relay_state = false;

void setup() {
  pinMode( OUTPUT, PIN_RELAY );
  digitalWrite( PIN_RELAY, 0 );
  SerialUSB.begin();
}



void print_relay_state(){
  if (relay_state) {
    SerialUSB.print("0");
  } else {
    SerialUSB.print("1");
  }
}


void loop() {
  // read serial for relay state
  if ( SerialUSB.available() ) {
    cdc_input = SerialUSB.read();
    // 0 = relay off
    if ( cdc_input == 48 ){
      relay_state = false;
      SerialUSB.print("0");
      digitalWrite( PIN_RELAY, 0 );
    }
    // 1 = relay_state on
    if ( cdc_input == 49 ) {
      relay_state = true;
      SerialUSB.print("1");
      digitalWrite( PIN_RELAY, 1 );
    }
    // 2 = relay toggle
    if ( cdc_input == 50 ) {
      print_relay_state();
      digitalWrite( PIN_RELAY, !relay_state );
      relay_state = !relay_state;
    }
    // 3 = get relay state
    if ( cdc_input == 51 ) {
      print_relay_state();
    }

    // 9 = get identification byte, returns 'r' or byte 114
    if ( cdc_input == 57 ){
      SerialUSB.print("r");
    }
  }

}
