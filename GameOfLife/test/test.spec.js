'use strict';

describe("GameOfLife", function(){
	describe("tick", function(){
		it("returns an empty grid when given an empty grid", function(){
			var gameofLife = new GameOfLife([]);
			expect(gameofLife.tick().length).to.equal(0);
		});
		it("returns a rotated blinker when given a blinker", function(){
			var gameofLife = new GameOfLife([[0,0],[0,1],[0,2]]),
			expectedLiveCells = [[-1,1],[1,1],[0,1]];
			expect(gameofLife.tick()).to.deep.equal(expectedLiveCells);
		});
	});
	describe("getLiveNeighbours", function(){
		var gameofLife = new GameOfLife([[0,0],[0,1],[1,0],[1,1]]);
		it("returns 3 for first cell when given a block", function(){
			expect(gameofLife.getLiveNeighbours([0,0])).to.equal(3);
		})
	})
});