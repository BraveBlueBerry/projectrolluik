#include <avr/io.h>
#define F_CPU	16000000
#include <avr/interrupt.h>
#include "serial.h"
#include "scheduler.h"
#include "functions.h"
#include "input.h"
#include "sensors.h"
#include "blinds.h"
#include <util/delay.h>

// used in blinds.h, functions.h
int blindState = 0;		// 0 = blind closed, 1 = blind open
int changing = 0;		// 0 = blind not changing, 1 = blind is changing
int changeCounter = 0;	// counter voor het veranderen van de status van de blind

// om de zelfstandigheid te testen (used in blinds.h)
int defaultMinTempTest = 10;
int defaultMaxTempTest = 50;
int defaultMaxLightTest = 800;
int minTempTest = 10;
int maxTempTest = 50;
int maxLightTest = 800;


int main(void) {
	initSerial();
	initScheduler();
	sei();
	adcInit();
	blindsInit();
	
	
	
	addTask(doSomethingWithInput,0,1);
	addTask(calcTemp,0,40);
	addTask(calcLight,0,40);
	addTask(blindShouldChange,0,20);
	addTask(didBlindChange,0,1);
	addTask(printWaarden,0,1);
	
	while(1){
		callTasks();
		_delay_ms(999);
		
	}
}