from xml.dom import WrongDocumentErr
import DNAMatrix as DNAMatrix
import DNAReadWrite as ReadWrite
import projetk as Modi

from random import randint
from sys import argv

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ToLittleArgumentsAsInput(Error):
    pass

class WrongTypeOfError(Error):
    pass


def main(error_type):

    spectrum = ReadWrite.readFromFile("dna.txt")
    #spectrum = ['aaaa','abcd','asdd','wead','adqa','aaaa','abcd','asdd','wead','adqa','aaaa','abcd','asdd','wead','adqa']
    
    #spectrum = ['ACGTAA','AGGTCC']
    if error_type == 'POSITIVE':
        spectrum = ReadWrite.positive_error(spectrum)
    elif error_type == 'NEGATIVE':
        spectrum = ReadWrite.negative_error(spectrum)
    else:
        spectrum = ReadWrite.negative_error(spectrum)
        spectrum = ReadWrite.positive_error(spectrum)
    
    spectrum.sort()
    return_creeated = DNAMatrix.optimize_graph(spectrum)

    spectrum = return_creeated[0]
    graph = return_creeated[1]
    max_superposition = return_creeated[2]

    population_List = Modi.Population(spectrum)


    best_dna_string = []
    best_dna_lenght = 999999999

    mutationStrenght = 15
    without_change1 = 0
    without_change2 = 0
    for iteration in range(1,3):
        print(iteration)
        population_List = Modi.mutation(population_List,mutationStrenght)
        if (iteration%10 == 0 and mutationStrenght > 0):
            mutationStrenght -= 1
        for cross_count in range(randint(10,len(spectrum))):
            first_ind = randint(0,len(population_List)-1)
            second_ind = randint(0,len(population_List)-1)
            while first_ind == second_ind:
                second_ind = randint(0,len(population_List)-1)

            new_population = Modi.crossover(population_List[first_ind],population_List[second_ind])

            population_List.append(new_population[0])
            population_List.append(new_population[1])

            superposition = DNAMatrix.calcSuperposition(population_List)
            if (superposition > max_superposition):
                 max_superposition = superposition
                 without_change2 = 0
            else:
                 without_change2 += 1

        if(iteration%2==0):
            print("zaczynam turniej {}".format(len(population_List)))
            tournament_result = Modi.tournament(population_List,graph)
            population_List = tournament_result[0]
            print("koncze turniej {}".format(len(population_List)))
            if tournament_result[1] >= best_dna_lenght:
                without_change1 += 1
            elif tournament_result[1] < best_dna_lenght:
                #print("zmieniam z {} na {}".format(best_dna_lenght,tournament_result[1]))
                best_dna_lenght = tournament_result[1]
                best_dna_string = tournament_result[2]
                without_change1 = 0
        if without_change1 >= 10 and without_change2 >= 10:
            break
    
    #for i in graph:
    #    print(i)
    print("dna reconstruction with lowest shift lenght: {} {}".format(best_dna_lenght,best_dna_string))
    print("\n number of perfect impositions: ", max_superposition)
    print(Modi.count_occurances(best_dna_string))
if __name__ == "__main__":
    try:
        if len(argv)-1 == 1:
            if argv[1].upper() not in ['POSITIVE','NEGATIVE','BOTH']:
                raise WrongTypeOfError    
            else:
                main(argv[1].upper())
        else:
            raise ToLittleArgumentsAsInput
            
    except ToLittleArgumentsAsInput:
        print("Please specify error type")
    
    except WrongTypeOfError:
        print("Specified incorrect error type. Available: 'POSITIVE','NEGATIVE','BOTH'")
