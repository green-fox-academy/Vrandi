
def fileread():
    with open('reversed_zen_order.txt') as f:
        s = f.readlines()
        return s

def write_reversed_to_file(line_list):
    with open('zen_of_python.txt', 'w') as out:
        out.write(''.join(line_list[::-1]))

write_reversed_to_file(fileread())
