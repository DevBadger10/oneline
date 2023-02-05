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

init()
print(line)
print(line[2].split())