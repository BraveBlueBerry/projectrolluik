extern int blindState;
extern int manual;
extern int changing;
extern int minTemp;
extern int maxTemp;
extern int maxLight;
extern int minHeightBlind;
extern int maxHeightBlind;
extern int defaultMinTemp;
extern int defaultMaxTemp;
extern int defaultMaxLight;
extern int defaultMinHeightBlind;
extern int defaultMaxHeightBlind;
extern int valueBlind;
extern uint32_t ID;

void sendOk();
void sendFail();

void setStatus(){
	uint8_t status = getChar();
	if(status == 0){								// zet terug op automatishc, manual = 0 (status = 0)
		manual = 0;
		sendOk();
	}
	else if(status == 1 && blindState == 0){		// blinds are now closed (blindState = 0), forced open (status = 1)
		blindState = 1;
		changing = 1;
		manual = 1;
		sendOk();
	}
	else if(status == 1 && blindState == 1){		// blinds are now open (blindState = 1), forced open (status = 1)
		changing = 0;
		manual = 1;
		sendOk();
	}
	else if(status == 2 && blindState == 0){		// blinds are now closed (blindState = 0), forced closed (status = 2)
		changing = 0;
		manual = 1;
		sendOk();
	}
	else if(status == 2 && blindState == 1){		// blinds are now open (blindState = 1), forced open (status = 2)
		blindState = 0;
		changing = 1;
		manual = 1;
		sendOk();
	}
	else {
		sendFail();
	}

}

void getStatus(){
	if(blindState == 0 && manual == 0){		// Blind is closed and controlled automatic
		sendImmediate(0);
	}
	if(blindState == 1 && manual == 0){		// Blind is open and controlled automatic
		sendImmediate(1);
	}
	if(blindState == 0 && manual == 1){		// Blind is closed and controlled manually
		sendImmediate(2);
	}
	if(blindState == 1 && manual == 1){		//Blind is open and controlled manually
		sendImmediate(3);
	}
}

void setMinTemp(){
	uint8_t newMinTemp = getChar();
	minTemp = newMinTemp;
	sendOk();
}

void getMinTemp(){
	uint8_t value = minTemp;
	sendImmediate(value);
}

void setMaxTemp(){
	uint8_t newMaxTemp = getChar();
	maxTemp = newMaxTemp;
	sendOk();
}

void getMaxTemp(){
	uint8_t value = maxTemp;
	sendImmediate(value);
}

void getTemp(){
 	int value = calcTemp();
 	sendImmediate(value);
}

void setMaxLight(){
	uint8_t newMaxLightH = getChar();
	uint8_t newMaxLightL = getChar();
	maxLight = (newMaxLightH << 8) | (newMaxLightL);
	sendOk();
}

void getMaxLight(){
	int value = maxLight;
	uint8_t valueH = (uint8_t)((value & 0xFF00) >> 8);
	uint8_t valueL = (uint8_t)(value & 0x00FF);
	sendImmediate(valueH);
	sendImmediate(valueL);
}

void getLight(){
	int value = calcLight();
	uint8_t valueH = (uint8_t)((value & 0xFF00) >> 8);
	uint8_t valueL = (uint8_t)(value & 0x00FF);
	sendImmediate(valueH);
	sendImmediate(valueL);
}

void setMinHeightBlind(){
	uint8_t newMinHeightBlindH = getChar();
	uint8_t newMinHeightBlindL = getChar();
	minHeightBlind = (newMinHeightBlindH << 8) | (newMinHeightBlindL);
	sendOk();
}

void setMaxHeightBlind(){
	uint8_t newMaxHeightBlindH = getChar();
	uint8_t newMaxHeightBlindL = getChar();
	maxHeightBlind = (newMaxHeightBlindH << 8) | (newMaxHeightBlindL);
	sendOk();
}

void getHeightBlind(){
	if(blindState == 0){
		valueBlind = maxHeightBlind;
	}
	else if(blindState == 1){
		valueBlind = minHeightBlind;
	}
	uint8_t valueH = (uint8_t)((valueBlind & 0xFF00) >> 8);
	uint8_t valueL = (uint8_t)(valueBlind & 0x00FF);
	sendImmediate(valueH);
	sendImmediate(valueL);
}

void reset(){
	minTemp = defaultMinTemp;
	maxTemp = defaultMaxTemp;
	maxLight = defaultMaxLight;
	minHeightBlind = defaultMinHeightBlind;
	maxHeightBlind = defaultMaxHeightBlind;
	manual = 0;
	sendOk();
}

void debug(){

}

void sendOk(){
	sendImmediate(1);
}

void sendFail(){
	sendImmediate(0);
}
