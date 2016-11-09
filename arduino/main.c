#include <avr/io.h>
#define F_CPU	16000000
#include <avr/interrupt.h>
#include "serial.h"

int main(void) {
  initSerial();
  //Sei();
  while(1){

  }
}
