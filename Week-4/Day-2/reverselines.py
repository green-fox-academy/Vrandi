
def fileread():
    with open('reversed_zen_lines.txt') as f:
        s = f.readlines()
        new = [x[::-1] for x in s]
        return new

def writetofile(line_list):
    with open('zen_of_python.txt', 'w') as out:
        out.write(''.join(line_list))

writetofile(fileread())
