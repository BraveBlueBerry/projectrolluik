/* De site waar ik informatie weg heb gehaald over de statements: https://hekilledmywire.wordpress.com/2011/03/16/using-the-adc-tutorial-part-5/
 * Deze terminal gebruikte de man van de site hierboven ook, dus heb ik voor het gemak ook gebruikt om te kijken wat voor waardes hij uitlas: https://sites.google.com/site/terminalbpp/
 * Ik heb mijn lichtsensor verbonden aan de analoge poort 0
 * Verbonden met de ground via de grote weerstand
 * Hij krijgt 5V
 * Het LEDje zit aan pin 13 aangesloten via een kleine weerstand
 */



#include <avr/io.h>
#include <stdlib.h>
#define F_CPU 16000000UL
#include <util/delay.h>
#define BAUDRATE 9600
#define BAUD_PRESCALLER (((F_CPU / (BAUDRATE * 16UL))) - 1)


uint16_t adc_value;                             // Variabele om de waarde van de analoge input (de ADC) in op te slaan
char buffer[5];                                 // Dit is iets voor de itoa functie, hiermee krijg ik het in een terminal zodat ik waardes kan aflezen in normale taal
uint8_t i=0;                                    // Variabele voor de for() loop
int tempC=0;
int lightL=0;
double vout=0;

void adc_init(void);                            // Functie om de ADC te intialiseren/configuren
uint16_t read_adc(uint8_t channel);             // Functie om de waarde van de analoge pin uit te lezen
void USART_init(void);                          // Functie om USART/serial te initialiseren/configuren (om dingen op mijn terminal te krijgen, ik snap nog niet precies hoe dit werkt; is copy-paste)
void USART_send( unsigned char data);           // Functie die een char stuurt over de seriele poort (^^^^^^^^^^^^^^^)
void USART_putstring(char* StringPtr);          // Functie die een string stuurt over de seriele poort (^^^^^^^^^^^^)
int calc_temp(int adc_value);
double calc_light(int adc_value);

int main(void){
    DDRB |= (1<<PB5);                           // Poort B instellen als output, PB5 staat voor pin 13 (pin 5 van poort B) van de digitale poorten

    adc_init();                                 // Roep de functie adc_init aan om ADC klaar te maken voor gebruik
    USART_init();                               // Roep de functie USART_init aan om de USART klaar te maken (dit snap ik zelf dus nog niet echt)

  while(1){
                                        // Een infinite loop, zodat ie door blijft gaan, kan ook while(1) zijn zoals wij dat op school vaak deden
        adc_value = read_adc(0);
                                                // Bij i<x kun je aangeven hoeveel van de poorten je wilt lezen, te beginnen bij poort 0 en dan oplopend. hij leest nu alleen poort 0
        USART_putstring("Temperature : ");    // Dit komt op mijn terminal te staan om aan te geven welke analoge pin hij leest
        calc_temp(adc_value);               // This is a nifty trick when we only want to send a number between 0 and 9 ???? --> het werkt x)
        itoa(tempC, buffer, 10);              // Just to keep things pretty
        USART_putstring(buffer);
        USART_putstring("  ");
        USART_putstring("c");
        _delay_ms(500);
        USART_send('\r');
        USART_send('\n');


        adc_value = read_adc(1);
        USART_putstring("Light: ");
        calc_light(adc_value);
        itoa(adc_value, buffer, 10);
        USART_putstring(buffer);
        USART_putstring("  ");
        USART_putstring("lux");
        _delay_ms(500);
        USART_send('\r');
        USART_send('\n');
}

return 0;
}

void adc_init(void){
 ADCSRA |= ((1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0));  // 16Mhz/128 = 125Khz the ADC reference clock (Om deze benamingen te begrijpen heb ik de site gelezen, zie bovenaan)
 ADMUX |= (1<<REFS0);                           // Voltage reference from Avcc (5v)
 ADCSRA |= (1<<ADEN);                           // Het aanzetten van de ADC (de analoge poort)
 ADCSRA |= (1<<ADSC);                           // Do an initial conversion because this one is the slowest and to ensure that everything is up and running
}

double calc_light(int adc_value){
  double vout = adc_value*0.0048828125;
  int lightL=500/(10*((5-vout)/vout));
  return lightL;
}

int calc_temp(int adc_value){
  tempC = ((adc_value / 1024.0 * 5000)-500) * 0.1;
  return tempC;
}

uint16_t read_adc(uint8_t channel){
 ADMUX &= 0xF0;                                 // Clear de vorige pin die gelezen was
 ADMUX |= channel;                              // Definieert de nieuwe pin die gelezen moet worden, voor poort analoog 3 vul je bijvoorbeeld 3 in bij het aanroepen van de functie
 ADCSRA |= (1<<ADSC);                           // Starts a new conversion --> ????
 while(ADCSRA & (1<<ADSC));                     // Wait until the conversion is done
 return ADCW;                                   // Returnt de waarde van de analoge poort die is gelezen
}

// Hieronder staan functies waarmee ik waardes kan zien in een terminal, maar dit snap ik niet echt. Maar het was om te testen of ie iets deed :)

void USART_init(void){

 UBRR0H = (uint8_t)(BAUD_PRESCALLER>>8);
 UBRR0L = (uint8_t)(BAUD_PRESCALLER);
 UCSR0B = (1<<RXEN0)|(1<<TXEN0);
 UCSR0C = (3<<UCSZ00);
}

void USART_send( unsigned char data){

 while(!(UCSR0A & (1<<UDRE0)));
 UDR0 = data;

}

void USART_putstring(char* StringPtr){

while(*StringPtr != 0x00){
 USART_send(*StringPtr);
 StringPtr++;}

}
