var Game = function(){
	this.isFirstRoll = true;
	this.scoreBoard = "";
	this.roll = function(numPins){
		switch(numPins){
			case 0:
				this.scoreBoard += '-';
				this.isFirstRoll = !this.isFirstRoll;
				break;
			case 10:
				this.scoreBoard += (this.isFirstRoll ? "X" : "/");
				this.isFirstRoll = true;
				break;
			default:
				var previousRoll = parseInt(this.scoreBoard.slice(-1) || 0),
					isSpare = !this.isFirstRoll && (numPins + previousRoll === 10);
				this.scoreBoard += (isSpare) ? "/" : numPins;
				this.isFirstRoll = !this.isFirstRoll;
				break;
		}
	};
	this.score = function(){
		var frames = [];
		var i = 0;
		while (i < this.scoreBoard.length && frames.length < 10){
			if (this.scoreBoard[i] === 'X'){
				frames[frames.length] = this.scoreAt(i) + this.scoreAt(i + 1) + this.scoreAt(i + 2);
			}
			else if (this.scoreBoard[i + 1] === '/'){
				frames[frames.length] = 10 + this.scoreAt(i + 2);
				i++;
			}
			else {
				frames[frames.length] = this.scoreAt(i) + this.scoreAt(i + 1);
				i++;
			}
			i++;
		};
		return frames.reduce(function(a,b){return a + b;});
	};
	this.scoreAt = function(index){
		switch (this.scoreBoard[index]){
			case '-':
				return 0;
			case 'X':
				return 10;
			case '/':
				return (10 - parseInt(this.scoreBoard[index - 1]));
			default:
				return parseInt(this.scoreBoard[index]);
		}
	};
}