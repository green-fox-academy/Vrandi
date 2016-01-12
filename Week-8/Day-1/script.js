'use strict';


function CandyGame() {
  var _this = this;

  this.candies = document.querySelector('.candies');
  this.NumberOfCandies = Number(this.candies.innerHTML);

  this.lollipops = document.querySelector('.lollipops');
  this.NumberOfLollipops = Number(this.lollipops.innerHTML);

  this.counter = document.querySelector('.counter');
  this.NumberOfCounter = Number(this.counter.innerHTML);

  this.candyButton = document.querySelector('.candy-button');
  this.lollyButton = document.querySelector('.lollipop-button');

  this.candyButton.addEventListener('click', function() {
    _this.NumberOfCandies++;
    _this.refreschStats();
  })

  this.lollyButton.addEventListener('click', function() {
    _this.NumberOfLollipops++;
    _this.NumberOfCandies -= 10;
    _this.refreschStats();
  })

  this.init = function() {
      setInterval(function() {
      _this.NumberOfCandies += _this.NumberOfCounter;
      _this.refreschStats();
    }, 1000);
  };

  this.refreschStats = function() {
    this.candies.innerHTML = this.NumberOfCandies;
    this.lollipops.innerHTML = this.NumberOfLollipops;
    this.NumberOfCounter = this.setCounter();
    console.log(this.NumberOfCounter);
    this.counter.innerHTML = this.NumberOfCounter;
    this.buttonDisability();
  };

  this.setCounter = function() {
    return Math.floor(this.NumberOfLollipops/10);
  }

  this.buttonDisability = function() {
    if (this.checkCandyAmount()) {
      this.lollyButton.removeAttribute('disabled');
    } else {
      this.lollyButton.setAttribute('disabled', 'disabled');
    }
  };

  this.checkCandyAmount = function() {
    return this.NumberOfCandies > 9;
  };

}

var candyGame = new CandyGame();
candyGame.init();