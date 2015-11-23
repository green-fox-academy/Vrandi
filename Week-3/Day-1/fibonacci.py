
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n > 1:
		return fibonacci(n-1) + fibonacci(n-2)

def fibo_list(num):
    for fib in range(num+1):
        print("The %sth number of fibonacci sequence: %s" % (fib, fibonacci(fib)))

fibo_list(int(input("Give a range for fibonacci numbers: ")))
