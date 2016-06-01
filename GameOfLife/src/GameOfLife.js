var GameOfLife = function(liveCells){
	this.liveCells = liveCells;
	this.tick = function(){
		var newLiveCells = [],
		gameOfLife = this;
		liveCells.forEach(function(cell){
			if (gameOfLife.getLiveNeighbours(cell) >= 2 && gameOfLife.getLiveNeighbours(cell) <= 3){
				newLiveCells.push(cell);
			}
			gameOfLife.getNeighbours(cell).forEach(function(neighbour){
				if (gameOfLife.getLiveNeighbours(neighbour) === 3 && !gameOfLife.liveCells.contains(neighbour) && !newLiveCells.contains(neighbour)){
					newLiveCells.push(neighbour);
				}
			})
		});
		this.liveCells = newLiveCells;
		console.log(newLiveCells);
		return this.liveCells;
	};

	this.getNeighbours = function(cell){
		var neighbours = [];
		for (var i = -1; i<2; i++){
			for (var j = -1;j<2;j++){
				if (i !== 0 || j !== 0){
					neighbours.push([cell[0] + i,cell[1] + j]);
				}
			}
		}
		return neighbours;	
	};

	this.getLiveNeighbours = function(cell){
		var numNeighbours = 0,
		gameOfLife = this;
		gameOfLife.getNeighbours(cell).forEach(function(neighbour){
			if (gameOfLife.liveCells.contains(neighbour)){
				numNeighbours++;
			}
		})
		return numNeighbours;
	};
}

Array.prototype.contains = function(cell){
	for (var k = 0; k< this.length; k++){
		if (this[k][0] === cell[0] && this[k][1] === cell[1]){
			return true;
		}
	}
	return false;
}
