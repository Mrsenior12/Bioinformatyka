from random import randint
import random
import string

mutationStrenght = 20
MUTATIONP_ROB = 5
DNA_PROB = 30

def createFile():
    l = ['A', 'C', 'G', 'T']
    with open('dna.txt', 'w') as f:
        for i in range(randint(100,400)):
            for j in range(10):
                f.write(l[randint(0,3)])
            f.write("\n")

def readFromFile(file):
    lista =''
    with open(file) as f:
        lista = f.read().splitlines()
    
    return lista

def firstPopulation(lista):
    tmpList = lista.copy()
    tmpList.sort()
    for i in range(5):
        lista[i] = tmpList[i]
    for i in range(6, len(lista)-1):
        lista[i] = tmpList[randint(5, len(lista))]
    return lista


def mutation(lista):
    for ind in range(len(lista)):
        dna = lista[ind]
        if randint(0,100) <= 30:
            for oglinukleotyd in range(mutationStrenght):
                dna_ind = randint(1,len(dna)-1)
                dna_ind2 = randint(1,len(dna)-1)
                tmp = dna[dna_ind2]
                dna[dna_ind2] = dna[dna_ind]
                dna[dna_ind] = tmp

    print(lista)
    #return lista


#startFile = createFile()
dna = readFromFile('dna.txt')
population = firstPopulation(dna)
mutation([population])