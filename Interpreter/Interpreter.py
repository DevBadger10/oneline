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
                    if cline[2] == "a":
                        a = b
                    elif cline[2] == "b":
                        b = b
                    elif cline[2] == "c":
                        c = b
                    elif cline[2] == "d":
                        d = b
                    elif cline[2] == "e":
                        e = b
                    elif cline[2] == "f":
                        f = b
                    elif cline[2] == "z":
                        z = b
                    elif cline[2] == "x":
                        x = b
                    else:
                        print("Interpreter Error: Invalid MOV Destination.")
                        sys.exit
                    b = 0
                elif cline[1] == "c":
                    if cline[2] == "a":
                        a = c
                    elif cline[2] == "b":
                        b = c
                    elif cline[2] == "c":
                        c = c
                    elif cline[2] == "d":
                        d = c
                    elif cline[2] == "e":
                        e = c
                    elif cline[2] == "f":
                        f = c
                    elif cline[2] == "z":
                        z = c
                    elif cline[2] == "x":
                        x = c
                    else:
                        print("Interpreter Error: Invalid MOV Destination.")
                        sys.exit
                    c = 0
                elif cline[1] == "d":
                    if cline[2] == "a":
                        a = d
                    elif cline[2] == "b":
                        b = d
                    elif cline[2] == "c":
                        c = d
                    elif cline[2] == "d":
                        d = d
                    elif cline[2] == "e":
                        e = d
                    elif cline[2] == "f":
                        f = d
                    elif cline[2] == "z":
                        z = d
                    elif cline[2] == "x":
                        x = d
                    else:
                        print("Interpreter Error: Invalid MOV Destination.")
                        sys.exit
                    d = 0
                elif cline[1] == "e":
                    if cline[2] == "a":
                        a = e
                    elif cline[2] == "b":
                        b = e
                    elif cline[2] == "c":
                        c = e
                    elif cline[2] == "d":
                        d = e
                    elif cline[2] == "e":
                        e = e
                    elif cline[2] == "f":
                        f = e
                    elif cline[2] == "z":
                        z = e
                    elif cline[2] == "x":
                        x = e
                    else:
                        print("Interpreter Error: Invalid MOV Destination.")
                        sys.exit
                    e = 0
                elif cline[1] == "f":
                    if cline[2] == "a":
                        a = f
                    elif cline[2] == "b":
                        b = f
                    elif cline[2] == "c":
                        c = f
                    elif cline[2] == "d":
                        d = f
                    elif cline[2] == "e":
                        e = f
                    elif cline[2] == "f":
                        f = f
                    elif cline[2] == "z":
                        z = f
                    elif cline[2] == "x":
                        x = f
                    else:
                        print("Interpreter Error: Invalid MOV Destination.")
                        sys.exit
                    f = 0
                elif cline[1] == "z":
                    if cline[2] == "a":
                        a = z
                    elif cline[2] == "b":
                        b = z
                    elif cline[2] == "c":
                        c = z
                    elif cline[2] == "d":
                        d = z
                    elif cline[2] == "e":
                        e = z
                    elif cline[2] == "f":
                        f = z
                    elif cline[2] == "z":
                        z = z
                    elif cline[2] == "x":
                        x = z
                    else:
                        print("Interpreter Error: Invalid MOV Destination.")
                        sys.exit
                    z = 0
                elif cline[1] == "x":
                    if cline[2] == "a":
                        a = x
                    elif cline[2] == "b":
                        b = x
                    elif cline[2] == "c":
                        c = x
                    elif cline[2] == "d":
                        d = x
                    elif cline[2] == "e":
                        e = x
                    elif cline[2] == "f":
                        f = x
                    elif cline[2] == "z":
                        z = x
                    elif cline[2] == "x":
                        x = x
                    else:
                        print("Interpreter Error: Invalid MOV Destination.")
                        sys.exit
                    x = 0
                elif cline[1] == "m":
                    if cline[2] == "a":
                        a = m
                    elif cline[2] == "b":
                        b = m
                    elif cline[2] == "c":
                        c = m
                    elif cline[2] == "d":
                        d = m
                    elif cline[2] == "e":
                        e = m
                    elif cline[2] == "f":
                        f = m
                    elif cline[2] == "z":
                        z = m
                    elif cline[2] == "x":
                        x = m
                    else:
                        print("Interpreter Error: Invalid MOV Destination.")
                        sys.exit
                    m = 0

init()
interpret()