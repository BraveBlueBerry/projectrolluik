#include <avr/io.h>
#define F_CPU	16000000
#include <avr/interrupt.h>
#include "serial.h"
#include "schedular.h"

int main(void) {
  testInit();
  initSchedular();
  sei();

  while(1){
    callTasks();
  }
  return 0;
}
