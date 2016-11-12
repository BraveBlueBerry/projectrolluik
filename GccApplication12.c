#include <avr/io.h>
#define F_CPU	16000000
#include <avr/interrupt.h>
#include "serial.h"
#include "functions.h"
#include "input.h"
#include "sensors.h"
#include <util/delay.h>



int main(void) {
	initSerial();
	sei();
	adc_init();

	while(1){
		
		
		_delay_ms(1000);
		
	}
}