import infos

l = infos.data()
newl = [x[len(x)-5:len(x)] for x in l]

def number_frequency(lis):
    dicty = {}
    for week in lis:
        for num in week:
            if num not in dicty: dicty[num] = 1
            else: dicty[num] += 1
    tosort_list = []
    for key, value in dicty.items():
        t = (value, key)
        tosort_list.append(t)
    sortedl = sorted(tosort_list)
    sortedl.reverse()
    print("The first five most frequent number is: ")
    for tup in sortedl[0:5]:
        num, f = tup
        print("number: {}, frequency: {}".format(f, num))
    return sortedl

number_frequency(newl)
