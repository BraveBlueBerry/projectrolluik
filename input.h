void doSomethingWithInput(){
	char c = getChar();
	if(c==0){				// opcode 0000 0000
		setStatus();
	}
	if(c==1){				// opcode 0000 0001
		setMinTemp();		
	}
	if(c==2){				// opcode 0000 0010
		setMaxTemp();
	}
	if(c==3){				// opcode 0000 0011
		setMaxLight();
	}
	if(c==4){				// opcode 0000 0100
		setMinHeightBlind();
	}
	if(c==5){				// opcode 0000 0101
		setMaxHeightBlind();
	}
	if(c==6){				// opcode 0000 0110
		reset();
	}
	if(c==7){				// opcode 0000 0111
		setID();
	}
	if(c==8){				// opcode 0000 1000
		getID();
	}
	if(c==9){				// opcode 0000 1001
		//debug();
	}
	if(c==10){				// opcode 0000 1010
		getTemp();
	}
	if(c==11){				// opcode 0000 1011
		getLight();
	}
	if(c==12){				// opcode 0000 1100
		getStatus();
	}
	if(c==13){				// opcode 0000 1101
		getHeightBlind();
	}
	if(c==14){				// opcode 0000 1110
		getMinTemp();
	}
	if(c==15){				// opcode 0000 1111
		getMaxTemp();
	}
	if(c==16){				// opcode 0001 0000
		getMaxLight();
	}
}