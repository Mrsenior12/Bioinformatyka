from ast import Mod
from pickletools import optimize

from torch import randint
import DNAMatrix as DNAMatrix
import DNAReadWrite as ReadWrite
import projetk as Modi

from random import randint

def main():
    ReadWrite.createFile()
    issue_list = ['positive','negative','both']

    """
        tutaj wstawić wywołanie fnkcji z błedami
    """

    #spectrum = ReadWrite.readFromFile("dna.txt")
    spectrum = ['aaaa','abcd','asdd','wead','adqa','aaaa','abcd','asdd','wead','adqa','aaaa','abcd','asdd','wead','adqa']
    return_creeated = DNAMatrix.optimize_graph(spectrum)

    spectrum = return_creeated[0]
    graph = return_creeated[1]
    population_List = Modi.Population(spectrum)

    best_dna = 99999999

    for iteration in range(10):
        population_List = Modi.mutation(population_List,mutationStrenght=15)

        for cross_count in range(randint(10,len(spectrum))):
            first_ind = randint(0,len(spectrum)-1)
            second_ind = randint(0,len(spectrum)-1)
            while first_ind == second_ind:
                second_ind = randint(0,len(spectrum)-1)

            new_population = Modi.crossover(population_List[first_ind],population_List[second_ind])

            population_List.append(new_population[0])
            population_List.append(new_population[1])
        
       # if iteration%4 == 0 and iteration != 0:
       #     population_List = Modi.tournament(population_List,graph)



main()