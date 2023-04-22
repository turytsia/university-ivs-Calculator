import random
import sys

assert(int(sys.argv[1]) > 1)
for i in range(0, int(sys.argv[1])):
    print(random.randint(1, 100000), end=" ")
