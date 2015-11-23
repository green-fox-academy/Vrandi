
def prime_writer(r):
    primes = []
    for x in range(1, r):
        d = []
        for y in range(1, r):
            if x%y == 0: d.append(y)
        if len(d)<=2: primes.append(x)
    return primes

print(prime_writer(int(input("Add a range to prime numbers:"))))

def prime_decide(num):
    if num in prime_writer(num): return True
    else: return False

print(prime_decide(int(input("Add a number and I check if it's a prime number: "))))
