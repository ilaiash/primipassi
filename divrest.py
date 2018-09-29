import sys


dividendo = 0
divisore = 0

if len(sys.argv) != 3:
    print "errore devi inserire divisore e dividendo"
    exit(179)
else:
    dividendo = int(sys.argv[1])
    divisore = int(sys.argv[2])

quoziente = int( dividendo / divisore )
resto = dividendo - (quoziente * divisore)

print "quoziente : ", quoziente , " resto : ", resto

