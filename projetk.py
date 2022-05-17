from random import randint
mutationStrenght = 20
MUTATIONP_ROB = 5
DNA_PROB = 30

def readFromFile():
    lista =''
    with open('dna.txt') as f:
        lista = f.read().splitlines()
    
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



dna = readFromFile()
mutation([dna])