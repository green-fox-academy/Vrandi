
def fileread():
    with open('reversed_zen_order.txt') as f:
        s = f.readlines()
        return s

def reversing(line_list):
    return ''.join(line_list[::-1])

print(reversing(fileread()))
