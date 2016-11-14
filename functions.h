extern int blindState;

void setStatus(int status){
	
}

void getStatus(){
	sendImmediate(blindState);
}

void setMinTemp(int temp){
	
}

void getMinTemp(){
	
}

void setMaxTemp(int temp){
	
}

void getMaxTemp(){
	
}

void getTemp(){
	int value = calcTemp();
	uint8_t valueH = (uint8_t)((value & 0xFF00) >> 8);
	uint8_t valueL = (uint8_t)(value & 0x00FF);
	sendImmediate(valueH);
	sendImmediate(valueL);
}

void setMaxLight(int light){
	
}

void getMaxLight(){
	
}

void getLight(){
	int value = calcLight();
	uint8_t valueH = (uint8_t)((value & 0xFF00) >> 8);
	uint8_t valueL = (uint8_t)(value & 0x00FF);
	sendImmediate(valueH);
	sendImmediate(valueL);
}

void setMinHeightBlind(int minheightblind){
	
}

void setMaxHeightBlind(int maxheightblind){
	
}

void getHeightBlind(){
	
}

void reset(){
	
}

void setID(int id){
	
}

void getID(){
	
}

void debug(){
	
}

void sendOk(){
	sendImmediate(1);
}

void sendFail(){
	
}
