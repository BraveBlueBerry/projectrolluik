/* Het aansturen van de leds
 * Rood led op pin 8 (poort B)
 * Geel led op pin 9 (poort B)
 * Groen led op pin 10 (poort B)
 */

void blinds_init(){
	DDRB = 0xFF;
	PORTB = 0x00;
}

void BlindIsOpen(){
	// Green led is on
	PORTB = 0x00;			// Turn off all leds
	PORTB = 0b00000100;		// Turn on green led
	
}

void BlindIsClosed(){
	// Red led is on
	PORTB = 0x00;			// Turn off all leds
	PORTB = 0b00000001;		// Turn on red led
}

void BlindIsOpening(){
	// Green and yellow led is on
	PORTB = 0x00;			// Turn off all leds
	PORTB = 0b00000110;		// Turn on green and yellow led
}

void BlindIsClosing(){
	// Red and yellow led is on
	PORTB = 0x00;			// Turn off all leds
	PORTB = 0b00000011;		// Turn on red and yellow led
}