/*
Bron: http://maxembedded.com/2011/06/avr-timers-timer0/ , https://maxembedded.wordpress.com/2011/06/28/avr-timers-timer1/
https://sites.google.com/site/qeewiki/books/avr-guide/timers-on-the-atmega328
*/
#include <util/delay.h>
#define led_TIME 20
uint8_t secondCount;
uint8_t ledTime;
void initSchedular(void)
{
    secondCount = 0;
    uint8_t ledTime = led_TIME;
    DDRB |= (1 << PB0);
    PORTB |= (1 << PB0);
}
void led()
{
  PORTB ^= (1 << PD0);
}
void second(void)
{
  _delay_ms(900);
  secondCount++;
  if (secondCount >= 60) {
    secondCount = 0;
  }
}
void callTasks(void)
{
  if (secondCount == ledTime) {
    ledTime = ledTime + 60 - (60 - led_TIME);
    led();
  }
  second();
}
