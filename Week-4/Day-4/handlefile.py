import os

def createfile(file_name):
    with open(file_name, 'a'):
        os.utime(file_name, None)
        
def fileread(file_name):
    with open(file_name, 'r') as todfile:
        return [x.rstrip() for x in todfile]

def writefile(file_name, what):
    with open(file_name, 'w') as out:
        out.write('\n'.join(what))
