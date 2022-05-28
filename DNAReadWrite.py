from random import randint

def createFile():
    l = ['A', 'C', 'G', 'T']
    with open('dna.txt', 'w') as f:
        for i in range(randint(100,400)):
            for j in range(4):
                f.write(l[randint(0,3)])
            f.write("\n")

def readFromFile(file):
    oligoList = ''
    with open(file) as f:
        oligoList = f.read().splitlines()
    
    return oligoList

def negative_error(spectrum,count_oligonucleotides = 10):
    for i in range(count_oligonucleotides):
        index_to_delete = randint(0,len(spectrum)-1)
        spectrum.pop(index_to_delete)

    return spectrum

def positive_error(spectrum,count_oligonucleotides = 10):
    lenght_of_oli = len(spectrum[0])
    possible_amino = ['A', 'C', 'G', 'T']
    for oli in range(count_oligonucleotides):
        oligonucleotide = ''
        for element in range(lenght_of_oli):
            oligonucleotide += possible_amino[randint(0,3)]
        spectrum.append(oligonucleotide)
    return(spectrum)
