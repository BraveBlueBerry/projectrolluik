void doSomethingWithInput(){
	char c = getChar();
	if(c==0){				// opcode 0000 0000
		// set status
	}
	if(c==1){				// opcode 0000 0001
		// set min temp
	}
	if(c==2){				// opcode 0000 0010
		// set max temp	
	}
	if(c==3){				// opcode 0000 0011
		// set licht
	}
	if(c==4){				// opcode 0000 0100
		// set min hoogte rolluik
	}
	if(c==5){				// opcode 0000 0101
		// set max hoogte rolluik
	}
	if(c==6){				// opcode 0000 0110
		// reset
	}
	if(c==7){				// opcode 0000 0111
		// set id
	}
	if(c==8){				// opcode 0000 1000
		// vraag id
	}
	if(c==9){				// opcode 0000 1001
		// debug
	}
	if(c==10){				// opcode 0000 1010
		// vraag temperatuur
	}
	if(c==11){				// opcode 0000 1011
		// vraag licht
	}
	if(c==12){				// opcode 0000 1100
		// vraag rolluik status
	}
	if(c==13){				// opcode 0000 1101
		// vraag hoogte rolluik
	}
	if(c==14){				// opcode 0000 1110
		// vraag min temp
	}
	if(c==15){				// opcode 0000 1111
		// vraag max temp
	}
	if(c==16){				// opcode 0001 0000
		// vraag max licht
	}
}