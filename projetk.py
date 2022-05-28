from importlib_metadata import Pair
from numpy.random import rand
from random import randint, random
import numpy

MUTATION_PROB = 100
DNA_PROB = 100

def Population(lista):
    population_list = []
    for i in range(20):
        tmpList = lista[:]
        tmpList.sort()
        dna = []
        dna.append(tmpList[0])
        for i in range(1, len(lista)-1):
            random_oli = randint(1, len(tmpList)-1)
            dna.append(tmpList[random_oli])
            print(tmpList[random_oli])
            tmpList.remove(tmpList[random_oli])
        print("stwrzylem nic")
        population_list.append(dna)
    return population_list

def mutation(dnaList,mutationStrenght):
    for ind in range(len(dnaList)):
        dna = dnaList[ind]
        if randint(1,100) <= MUTATION_PROB:
            if randint(0,100) <= DNA_PROB:
                for oglinukleotyd in range(mutationStrenght):
                    dna_ind = randint(1,len(dna)-1)
                    dna_ind2 = randint(1,len(dna)-1)
                    tmp = dna[dna_ind2]
                    dna[dna_ind2] = dna[dna_ind]
                    dna[dna_ind] = tmp

    return dnaList

def count_path(graph,dna):
    path_distance = 0
    starting = dna[0][0]

    for oli in range(len(dna)-1):
        path_distance += graph[starting][dna[oli+1][0]]
        starting = dna[oli+1][0]
    
    return path_distance

def tournament(dnaList,graph,tournamentSize = 2):
    result = []
    participantList = [ind for ind in range(len(dnaList))]

    best_lenght = 999999
    best_participant = []
    for turn in range(len(dnaList)//tournamentSize):
        tournament_result = []
        #Create list of participant
        for participant in range(tournamentSize):
            participant_ind = participantList[randint(0,len(participantList)-1)]
            tournament_result.append([participant_ind ,count_path(graph,dnaList[participant_ind])])
            participantList.remove(participant_ind)

        tournament_result_sorted = sorted(tournament_result,key=lambda x:x[1])
        result.append(dnaList[tournament_result_sorted[0][0]])
        if tournament_result_sorted[0][1] < best_lenght:
            best_lenght = tournament_result_sorted[0][1]
            best_participant = dnaList[tournament_result_sorted[0][0]]

    # Add to result list DNA strings which didn't take part in tournament
    if len(participantList)%tournamentSize != 0: 
        for rest in participantList:
            result.append(dnaList[rest])

    return (result, best_lenght, best_participant)

def crossover(p1, p2, r_cross=0.75):
    c1, c2 = p1[:], p2[:]
    if random() < r_cross:
        # select crossover point that is not on the end of the string
        pt = randint(1, len(p1)-2)
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]



#print(crossover([1,2,3],[3,4,5],0.9))
#startFile = createFile()
#dna = readFromFile('dna.txt')
#population = firstPopulation(dna)
#mutation([population])
