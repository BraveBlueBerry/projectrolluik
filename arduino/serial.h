#include <avr/interrupts.h>
#define BUAD	9600
#define BRC		((F_CPU/16/BUAD) - 1)

void initSerial()
{
  UBRR0H = (BRC >> 8);//bautrate registers
  UBRR0L =  BRC;

  UCSR0B = (1 << RXEN0);//zet de serial ontvanger aan
  UCSR0B |= (1 << RXCIE0);//iets klaar om te lezen interrupt
  UCSR0B |= (1 << TXEN0);
  UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);//zet de bit groote
}
