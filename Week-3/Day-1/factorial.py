
def fact(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    elif n > 1:
        return n * fact(n - 1)

print(fact(5))
