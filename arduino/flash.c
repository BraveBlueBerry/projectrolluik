/*
 * GccApplication3.c
 *
 * Created: 14-11-2016 18:00:17
 *  Author: Pieter
 */
#include <avr/io.h>
#define F_CPU 16000000UL
#include <D:/Libraries/Documents/Atmel Studio/GccApplication3/GccApplication3/serial.h>
#include <avr/eeprom.h>
#include <util/delay.h>
#include <avr/interrupt.h>
uint32_t ID = 1479142404;


	void setID(uint32_t ID)
        {
            eeprom_write_dword((uint32_t*)12, ID);
        }

	void updateID(uint32_t ID)
        {
            eeprom_update_dword((uint32_t*)12, ID);

        }

	uint32_t getID(void)
		{
		 uint32_t data;
         data = eeprom_read_dword((uint32_t*)12);
         return data;
         }

int main(void) {
 initSerial();
 sei();
  setID(ID);
    while(1)
    {
	 sendMultipleImediate(getID());
       _delay_ms(5000);
    }
}
