/* Bron: https://hekilledmywire.wordpress.com/2011/03/16/using-the-adc-tutorial-part-5/
 * Lichtsensor op analoge poort 0 (10K ohm weerstand)
 * Temperatuursensor op analoge poort 1
 */

uint16_t adc_value;                             // Variabele om de waarde van de analoge input (de ADC) in op te slaan
char buffer[5];                                 // Dit is iets voor de itoa functie, hiermee krijg ik het in een terminal zodat ik waardes kan aflezen in normale taal
uint8_t i=0;                                    // Variabele voor de for() loop
int tempC=0;
int lightL=0;
double vout=0;

void adc_init(void);                            // Functie om de ADC te intialiseren/configuren
uint16_t read_adc(uint8_t channel);             // Functie om de waarde van de analoge pin uit te lezen
int calc_temp(int adc_value);
double calc_light(int adc_value);


void adc_init(void){
	ADCSRA |= ((1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0));  // 16Mhz/128 = 125Khz the ADC reference clock (Om deze benamingen te begrijpen heb ik de site gelezen, zie bovenaan)
	ADMUX |= (1<<REFS0);                           // Voltage reference from Avcc (5v)
	ADCSRA |= (1<<ADEN);                           // Het aanzetten van de ADC (de analoge poort)
	ADCSRA |= (1<<ADSC);                           // Do an initial conversion because this one is the slowest and to ensure that everything is up and running
}

double calc_light(int adc_value){
	adc_value = read_adc(0);
	double vout = adc_value*0.0048828125;
	int lightL=500/(10*((5-vout)/vout));
	return lightL;
}

int calc_temp(int adc_value){
	adc_value = read_adc(1);
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