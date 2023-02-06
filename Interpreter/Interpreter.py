import sys

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
z = 0
x = 0
m = 0
temp = 0

try:
    if sys.argv[1].endswith(".ol"):
        path = sys.argv[1]
    else:
        print("Interpreter Error: Incorrect extension.")
        sys.exit()
except:
    print("Interpreter Error: No code path supplied.")
    sys.exit()

def init():
    codefile = open(path)
    code = codefile.read()
    codefile.close()
    global line
    line = code.split(":")

def interpret():
    r = range(len(line))
    for i in r:
        cline = line[i].split()
        if cline[0] == "mov":
            if cline[1] == "a" or "b" or "c" or "d" or "e" or "f" or "z" or "x" or "m" and cline[2] == "a" or "b" or "c" or "d" or "e" or "f" or "z" or "x" or "m":
                if cline[1] == "a":
                    if cline[2] == "a":
                        a = a
                    elif cline[2] == "b":
                        b = a
                    elif cline[2] == "c":
                        c = a
                    elif cline[2] == "d":
                        d = a
                    elif cline[2] == "e":
                        e = a
                    elif cline[2] == "f":
                        f = a
                    elif cline[2] == "z":
                        z = a
                    elif cline[2] == "x":
                        x = a
                    else:
                        print("Interpreter Error: Invalid MOV Destination.")
                        sys.exit
                    a = 0
                elif cline[1] == "b":
                    pass
                elif cline[1] == "c":
                    pass
                elif cline[1] == "d":
                    pass
                elif cline[1] == "e":
                    pass
                elif cline[1] == "f":
                    pass
                elif cline[1] == "z":
                    pass
                elif cline[1] == "x":
                    pass
                elif cline[1] == "m":
                    pass

init()
interpret()