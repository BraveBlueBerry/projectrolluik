#include <avr/io.h>
#define F_CPU	16000000
#include <avr/interrupt.h>
#include "serial.h"
#include "input.h"
#include <util/delay.h>



int main(void) {
	initSerial();
	sei();

	while(1){
		
		
		_delay_ms(1000);
		
		/*
		if(c != '\0'){
			if(c == 0b00001010){
				sendImmediate('x');
			}
			
		}*/
	}
}