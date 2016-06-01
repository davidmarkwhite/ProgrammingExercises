'use strict';

describe("Game", function(){
	describe("roll", function(){
		it("should allow a second roll if less than 10 knocked down", function(){
			var game = new Game();
			game.roll(0);
			expect(game.isFirstRoll).to.equal(false);
		});
		it("should not allow a second roll if 10 knocked down", function(){
			var game = new Game();
			game.roll(10);
			expect(game.isFirstRoll).to.equal(true);
		});
		it("should record a spare after 0 and 10", function(){
			var game = new Game();
			game.roll(0);
			game.roll(10);
			expect(game.scoreBoard).to.equal("-/");
		});
		it("should record a spare after 7 and 3", function(){
			var game = new Game();
			game.roll(7);
			game.roll(3);
			expect(game.scoreBoard).to.equal("7/");
		});
		it("should record a complex series of rolls correctly", function(){
			var game = new Game();
			game.roll(10);
			game.roll(3);
			game.roll(7);
			game.roll(6);
			game.roll(0);
			expect(game.scoreBoard).to.equal("X3/6-");
		});
	});
	describe("score", function(){
		it("should score a series of numbers correctly", function(){
			var game = new Game();
			game.roll(3);
			game.roll(4);
			game.roll(5);
			game.roll(1);
			game.roll(2);
			game.roll(7);
			game.roll(3);
			game.roll(5);
			expect(game.score()).to.equal(30);
		});
		it("should score spares correctly", function(){
			var game = new Game();
			game.roll(3);
			game.roll(7);
			game.roll(5);
			game.roll(4);
			expect(game.score()).to.equal(24);
		});
		it("should score strikes correctly", function(){
			var game = new Game();
			game.roll(10);
			game.roll(3);
			game.roll(5);
			game.roll(4);
			game.roll(4);
			expect(game.score()).to.equal(34);
		});
		it("should score strikes followed by spares correctly", function(){
			var game = new Game();
			game.roll(10);
			game.roll(3);
			game.roll(7);
			game.roll(4);
			game.roll(4);
			expect(game.score()).to.equal(42);
		});
		it("should allow bonus throws and only count them for bonuses", function(){
			var game = new Game();
			for (var i = 0; i < 12; i++){
				game.roll(10);
			}
			expect(game.score()).to.equal(300);
		});
		it("should return 90 for 9-9-9-9-9-9-9-9-9-9-", function(){
			var game = new Game();
			for (var i = 0; i < 10; i++){
				game.roll(9);
				game.roll(0);
			}
			expect(game.score()).to.equal(90);
		});
		it("should return 150 for 5/5/5/5/5/5/5/5/5/5/5", function(){
			var game = new Game();
			for (var i = 0; i < 21; i++){
				game.roll(5);
			}
			expect(game.score()).to.equal(150);
		});
		it("should ignore more than 10 frames", function(){
			var game = new Game();
			for (var i = 0; i < 25; i++){
				game.roll(5);
			}
			expect(game.score()).to.equal(150);
		});
	})
});