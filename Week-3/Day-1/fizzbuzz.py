
def fizzbuzz(r):
	for x in range(r):
	    if (x%3 == 0) and (x%5 ==0): print("FizzBuzz")
	    elif ('3' in str(x)) and ('5' in str(x)):
	        print("FizzzzzzzBuzzzzzzz")
	    elif x % 3 == 0: print("Fizz")
	    elif x % 5 == 0: print("Buzz")
	    elif '3' in str(x): print("Fizzzzz")
	    elif '5' in str(x): print("Buzzzzz")
	    else: print(x)

fizzbuzz(int(input("Add the range:")))
