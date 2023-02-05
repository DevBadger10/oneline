import sys

try:
    if sys.argv[1].endswith(".ol"):
        path = sys.argv[1]
    else:
        print("Interpreter Error: Incorrect Extension.")
        sys.exit()
except:
    print("Interpreter Error: No code path supplied.")
    sys.exit()

def init():
    codefile = open(path)
    code = codefile.read()
    print(code)

init()