
def fileread():
    with open('reversed_zen_lines.txt') as f:
        s = f.readlines()
        new = [x[::-1] for x in s]
        return new

def writeconsole(line_list):
    return ''.join(line_list)

print(writeconsole(fileread()))
