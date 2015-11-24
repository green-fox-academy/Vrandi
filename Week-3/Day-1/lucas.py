def luca(n):
	if n == 0:
		return 2
	elif n == 1:
		return 1
	elif n > 1:
		return luca(n-1) + luca(n-2)

def luca_list(num):
    for l in range(num+1):
        print("The %sth number of lucas sequence: %s" % (l, luca(l)))

luca_list(int(input("Give a range for lucas numbers: ")))
