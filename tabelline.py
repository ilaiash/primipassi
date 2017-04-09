import sys

for i in range(1,11):
    for j in range(1,11):
        sys.stdout.write("%2d "%(i*j))
    sys.stdout.write("\n")

