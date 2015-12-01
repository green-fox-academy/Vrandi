
def fileread():
    with open('duplicate_chars.txt') as f:
        s = f.readlines()
        return s

def decoder(line_list):
    new = []
    for line in line_list:
        st = ''
        for i in range(0,len(line), 2):
            st += line[i]
        new.append(st)
    return ''.join(new)


print(decoder(fileread()))
