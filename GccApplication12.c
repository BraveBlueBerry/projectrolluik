#include <avr/io.h>
#define F_CPU	16000000
#include <avr/interrupt.h>
#include <avr/eeprom.h>
#include "serial.h"
#include "scheduler.h"
#include "functions.h"
#include "input.h"
#include "sensors.h"
#include "blinds.h"
#include <util/delay.h>

// waarden om de zonneschermen aan te kunnen sturen (used in blinds.h, functions.h)
int blindState = 0;		// 0 = blind closed, 1 = blind open
int changing = 0;		// 0 = blind not changing, 1 = blind is changing
int changeCounter = 0;	// counter voor het veranderen van de status van de blind
int manual = 0;

// default waarden en aanpasbare waarden voor instellingen (used in blinds.h, functions.h)
int defaultMinTemp = 10;
int defaultMaxTemp = 50;
int defaultMaxLight = 800;
int defaultMinHeightBlind = 5;
int defaultMaxHeightBlind = 300;
int minTemp = 10;
int maxTemp = 50;
int maxLight = 800;
int minHeightBlind = 5;
int maxHeightBlind = 300;
int valueBlind = 300;
uint32_t ID = 'e';
uint32_t data;


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
	//addTask(printWaarden,0,1);
	
	while(1){
		callTasks();
		_delay_ms(999);
		
	}
}