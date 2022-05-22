from random import randint

def createFile():
    l = ['A', 'C', 'G', 'T']
    with open('dna.txt', 'w') as f:
        for i in range(randint(100,400)):
            for j in range(10):
                f.write(l[randint(0,3)])
            f.write("\n")

def readFromFile(file):
    oligoList = ''
    with open(file) as f:
        oligoList = f.read().splitlines()
    
    return oligoList

