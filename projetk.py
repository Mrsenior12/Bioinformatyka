from numpy.random import rand

import DNAMatrix as DNAMatrix
import DNAReadWrite as ReadWrite

from random import randint
import numpy
import ga

mutationStrenght = 20
MUTATIONP_ROB = 5
DNA_PROB = 30

def firstPopulation(lista):
    tmpList = lista.copy()
    tmpList.sort()
    for i in range(5):
        lista[i] = tmpList[i]
    for i in range(6, len(lista)-1):
        lista[i] = tmpList[randint(5, len(lista))]
    return lista

def mutation(dnaList):
    for ind in range(len(dnaList)):
        dna = dnaList[ind]

        if randint(0,100) <= 30:
            for oglinukleotyd in range(mutationStrenght):
                dna_ind = randint(1,len(dna)-1)
                dna_ind2 = randint(1,len(dna)-1)
                tmp = dna[dna_ind2]
                dna[dna_ind2] = dna[dna_ind]
                dna[dna_ind] = tmp

    return dnaList

def tournament(dnaList,tournamentSize = 2):
    result = []
    for turn in range(len(dnaList)//tournamentSize):
        
        #Create list of participant
        participantList = []
        for participant in range(tournamentSize):
            participant = dnaList[randint(0,len(dnaList)-1)]
            while participant in participantList:
                participant = dnaList[randint(0,len(dnaList)-1)]
            participantList.append(participant)
        
        #Sort Participant of tournament by their's sum
        participantList.sort(key=lambda participantList:sum(participantList))
        result.append(participantList[-1])

        for part in participantList:
            dnaList.remove(part)

    # Add to result list DNA strings which didn't take part in tournament
    if len(dnaList)%tournamentSize != 0: 
        for rest in dnaList:
            result.append(rest)

    return result


def crossover(p1, p2, r_cross):
    c1, c2 = p1.copy(), p2.copy()
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
        pt = randint(1, len(p1)-2)
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]

print(tournament([[1,2,3],[2,2,2],[3,3,3],[0,8,7,3],[9,9,9,9,9]]))

print(crossover([1,2,3],[3,4,5],0.9))
#startFile = createFile()
#dna = readFromFile('dna.txt')
#population = firstPopulation(dna)
#mutation([population])
