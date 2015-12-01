
def fileread():
    with open('encoded_zen_lines.txt') as f:
        s = f.readlines()
        return s

def decoder(line_list):
    new =[]
    for line in line_list:
        st = ''
        for i in line:
            if i == ' ' or i == '\n':
                st += i
            else:
                st += chr(ord(i)-1)

        new.append(st)
    return ''.join(new)

print(decoder(fileread()))
