import sys

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# RUN python name.py "Blessing Claire" - HELLO, MY NAME IS BLESSING
# python - program name, name.py - 0 index, Blessing - 1 index

# ALTERNATIVELY

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)

# SLICING: have many args but give me argument 1 to the end

#elif len(sys.argv) > 2:
    #sys.exit("Too many arguments")

# print("Hello, my name is", sys.argv[1])