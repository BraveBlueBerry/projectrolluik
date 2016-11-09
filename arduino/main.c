#include <avr/io.h>
#define F_CPU	16000000
#include <avr/interrupt.h>
#include "serial.h"
#include <util/delay.h>

int main(void) {
  initSerial();
  sei();

  while(1){

  }
}
