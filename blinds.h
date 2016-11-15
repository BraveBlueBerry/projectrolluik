/* Het aansturen van de leds
 * Rood led op pin 8 (poort B)
 * Geel led op pin 9 (poort B)
 * Groen led op pin 10 (poort B)
 */

extern int blindState;
extern int changing;
extern int changeCounter;
extern int manual;

extern int minTemp;
extern int maxTemp;
extern int maxLight;

void blindsInit(){
	DDRB = 0xFF;
	PORTB = 0x00;
	blindIsClosed();
}

void blindIsOpen(){
	// Green led is on
	PORTB = 0x00;			// Turn off all leds
	PORTB = 0b00000100;		// Turn on green led
	
}

void blindIsClosed(){
	// Red led is on
	PORTB = 0x00;			// Turn off all leds
	PORTB = 0b00000001;		// Turn on red led
}

void blindIsOpening(){
	// Green and yellow led is on
	PORTB = 0x00;			// Turn off all leds
	PORTB = 0b00000110;		// Turn on green and yellow led
}

void blindIsClosing(){
	// Red and yellow led is on
	PORTB = 0x00;			// Turn off all leds
	PORTB = 0b00000011;		// Turn on red and yellow led
}

/* Deze functie wordt elke 60 seconden aangeroepen om te kijken of de blind
 * open of dicht moet gaan. Zoja, dan zet hij changing en newState op 1 en 
 * past hij de blindState aan.
 */
void blindShouldChange(){
	if(manual == 0){
		int newState = 0;
		if(calcLight() > maxLight){
			if(calcTemp() < maxTemp && calcTemp() > minTemp){
				newState = 1;
			}
		}
		if(newState != blindState){
			changing = 1;
		}
		blindState = newState;
	}	
}
/* Deze functie kijkt elke seconde of changing op 1 staat (want dan moet de 
 * blind iets gaan doen) en welke state de blind moet gaan hebben. Hij laat
 * een counter lopen voor het veranderen van de state (het gele lampje). 
 */
void didBlindChange(){
	if(changing == 1 && blindState == 0){
		changeCounter++;
		blindIsClosing();
		if(changeCounter == 10){
			changing = 0;
			blindIsClosed();
			changeCounter = 0;
		}	
	}
	if(changing == 1 && blindState == 1){
		changeCounter++;
		blindIsOpening();
		if(changeCounter == 10){
			changing = 0;
			blindIsOpen();
			changeCounter = 0;
		}
	}
}