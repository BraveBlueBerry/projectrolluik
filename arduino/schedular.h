/*
Deze header geeft de mogelijkheid om taken eens in de x seconden uit te voeren.
Voor gebruik dient de initSchedular() te zijn aangeroepen.
Om een taak in de schedular te zetten moet addTask() worden aangeroepen.
Om de schedular verder te laten functioneren moet callTasks() constant worden aangeroepen.
*/
//#include <util/delay.h>
#define NUMBER_OF_TASKS 2
uint8_t secondCount;
void (*task[NUMBER_OF_TASKS]) (void);
uint8_t taskStart[NUMBER_OF_TASKS];
uint8_t taskDelay[NUMBER_OF_TASKS];
uint8_t taskindex;

/*
addTask() voegt een taak toe aan de schedular.
Hiervoor wordt om 3 parameters gevraagt.
Dit zijn de functie die moet worden aangroepen,
Het moment dat deze taak voor het eerst moet worden uitgevoerd
en hoeveel tijd er tussen het uitvoeren van de taak zit
NOTE begin en delay moeten gelijk of groter dan 0 zijn en kleiner dan 60.
*/
void addTask(void(*function)(), uint8_t begin, uint8_t delay)
{
  task[taskindex] = function;
  taskStart[taskindex] = begin;
  taskDelay[taskindex] = delay;
  taskindex++;
}
/*
initSchedular() Initialiseerd de globale variabelen die vereist zijn.
*/
void initSchedular(void)
{
  OCR1A = 0x3D08;          //Zet de waarde van het CTC compare register
  TCCR1B |= (1 << WGM12); // Mode 4, CTC on OCR1A
  TIMSK1 |= (1 << OCIE1A);//Set interrupt on compare match
  TCCR1B |= (1 << CS12) | (1 << CS10);// set prescaler to 1024 and start the timer

  taskindex = 0;
  secondCount = 0;
}
/*
second verhoogt de secondenteller (secondCount) elke seconde mits aangeroepen.
Verder wordt secondCount verlaagt bij het overschrijden van correcte waarden (60 en hoeger)
*/
void second(void)
{
  //_delay_ms(999);
  secondCount++;
  if (secondCount >= 60) {
    secondCount = 0;
  }
}
/*
Berekend wat het volgende tijstip is waarop een taak weer al moeten worden aangeroepn.
*/
uint8_t calcTime(uint8_t delay)
{
  uint8_t new;
  new = secondCount + 60 - (60 - delay);
  if (new >= 60) {
    new = 0;
  }
  return new;
}
/*
callTasks(void) kijkt over er taken zijn die moeten worden uitgevoerd.
*/
void callTasks(void)
{
    if (taskStart[i] == secondCount) {
      (*task[i]) ();
      taskStart[i] = calcTime(taskDelay[i]);
    }
  }
  //second();
}
/*
Deze interrupt verhoogt de secondenteller (secondCount) elke seconde.
Verder wordt secondCount verlaagt bij het overschrijden van correcte waarden (60 en hoger).
*/
ISR (TIMER1_COMPA_vect)
{
  secondCount++;
  if (secondCount >= 60) {
    secondCount = 0;
  }
}
