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
  this.tenButton = document.querySelector('.tenlolli-button');

  this.candyButton.addEventListener('click', function() {
    _this.NumberOfCandies++;
    _this.refreschStats();
  })

  this.lollyButton.addEventListener('click', function() {
    _this.NumberOfLollipops++;
    _this.NumberOfCandies -= 10;
    _this.refreschStats();
  })

  this.tenButton.addEventListener('click', function() {
    _this.NumberOfLollipops += 10;
    _this.NumberOfCandies -= 100;
    _this.refreschStats();
  })

  this.init = function() {
      setInterval(function() {
      _this.NumberOfCandies += _this.NumberOfCounter;
      _this.refreschStats();
      if (_this.NumberOfCandies >= 10000) {
        alert("WIN!!!");
      }
    }, 1000);
  };

  this.refreschStats = function() {
    this.candies.innerHTML = this.NumberOfCandies;
    this.lollipops.innerHTML = this.NumberOfLollipops;
    this.NumberOfCounter = this.setCounter();
    this.counter.innerHTML = this.NumberOfCounter;
    this.checkLollipopButtonAbility();
    this.checkTenLollipopButtonAbility();
  };

  this.setCounter = function() {
    return Math.floor(this.NumberOfLollipops/10);
  }

  this.checkLollipopButtonAbility = function() {
    if (this.checkCandyAmountForTen()) {
      this.lollyButton.removeAttribute('disabled');
    } else {
      this.lollyButton.setAttribute('disabled', 'disabled');
    }
  };

  this.checkTenLollipopButtonAbility = function() {
    if (this.checkCandyAmountForHundred()) {
      this.tenButton.removeAttribute('disabled');
    } else {
      this.tenButton.setAttribute('disabled', 'disabled');
    }
  };

  this.checkCandyAmountForTen = function() {
    return this.NumberOfCandies > 9;
  };

  this.checkCandyAmountForHundred = function() {
    return this.NumberOfCandies > 99;
  }

}

var candyGame = new CandyGame();
candyGame.init();