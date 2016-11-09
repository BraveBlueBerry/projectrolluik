/*
Dit bestand geeft de bodigde functies om seriele te versturen en ontvangen.
Bronnen: humanHardDrive https://www.youtube.com/user/humanHardDrive, avr datasheet
*/
#define BUAD	9600
#define BRC		((F_CPU/16/BUAD) - 1)
#define RX_BUFFER_SIZE 40
#define TX_BUFFER_SIZE 40

uint8_t rxBuffer[RX_BUFFER_SIZE];//Ontvangen verichten worden hier in ondergebracht
uint8_t txBuffer[TX_BUFFER_SIZE];//opslag voor te verzenden berichten

uint8_t rxReadPos = 0;
uint8_t rxWritePos = 0;
uint8_t txReadPos = 0;
uint8_t txWritePos = 0;

/*
Initialiseer de baud rate lees/schrijf registers en nodige interrupts
*/
void initSerial()
{
  UBRR0H = (BRC >> 8);//bautrate registers
  UBRR0L =  BRC;

  UCSR0B = (1 << RXEN0);//zet de serial ontvanger aan
  UCSR0B |= (1 << RXCIE0);//iets klaar om te lezen interrupt
  UCSR0B |= (1 << TXEN0);
  UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);//zet de bit groote
}
/*
Lees de volgende karakter en zet de kijker naar de volgende. Als er geen nieuwe is word \0 teruggestuurd.
*/
char getChar(void)
{
	char ret = '\0';

	if(rxReadPos != rxWritePos)
	{
		ret = rxBuffer[rxReadPos];

		rxReadPos++;

		if(rxReadPos >= RX_BUFFER_SIZE)
		{
			rxReadPos = 0;
		}
  }
  return ret;
}

/*
Deze interrupt gaat af wanneer er een nieuwe kaakter is om gelezen te worden.
*/
ISR(USART_RX_vect)
{
  	rxBuffer[rxWritePos] = UDR0;

  	rxWritePos++;

  	if(rxWritePos >= RX_BUFFER_SIZE)
  	{
  		rxWritePos = 0;
  	}
}

//schrijf deel
/*
Neemt een enkel teken en plaatst deze in de versturen que.
*/
void appendSerial(char c)
{
	txBuffer[txWritePos] = c;
	txWritePos++;

	if(txWritePos >= TX_BUFFER_SIZE)
	{
		txWritePos = 0;
	}
}
/*
Stopt een serie aan tekens in een que (array) om verstuurd te worden.
*/
void serialWrite(char c[])
{
  uint8_t n = sizeof(c) / sizeof(uint8_t);
	for(uint8_t i = 0; i < n; i++)
	{
		appendSerial(c[i]);
	}

	if(UCSR0A & (1 << UDRE0))
	{
		UDR0 = 0;
	}
}

void sendCharacter()
{
  if(txReadPos != txWritePos)
  {
    UDR0 = txBuffer[txReadPos];
    txReadPos++;

    if(txReadPos >= TX_BUFFER_SIZE)
    {
      txReadPos = 0;
    }
  }
}
