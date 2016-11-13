#include <avr/io.h>
#define F_CPU	16000000
#include <avr/interrupt.h>
#include "serial.h"
#include "functions.h"
#include "input.h"
#include "sensors.h"
#include "blinds.h"
#include <util/delay.h>



int main(void) {
	initSerial();
	sei();
	adc_init();
	blinds_init();
	
	while(1){
		doSomethingWithInput();
		_delay_ms(1000);
		
	}
}