from audioop import cross
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

    population_List = Modi.Population(spectrum)


    best_dna_string = []
    best_dna_lenght = 999999999

    mutationStrenght = 15
    without_change = 0
    for iteration in range(1,500):
        population_List = Modi.mutation(population_List,mutationStrenght)
        if (iteration%500 == 0 and mutationStrenght > 0): mutationStrenght -= 1
        # Poprawić pętle z crossem
        
        prticipant_ind = [i for i in range(len(population_List))]
        end_point = (len(population_List)-(len(population_List)%4))//4
        for cross_count in range(randint(0,end_point)):
            participant_list = []

            for i in range(4):
                dna_ind = prticipant_ind[randint(0,len(prticipant_ind)-1)]
                participant_list.append(population_List[dna_ind])
                prticipant_ind.remove(dna_ind)

            new_population = Modi.crossover(graph,participant_list)

            for elem in new_population:
                population_List.append(elem)
            
        if(iteration%10==0):
            #print("zaczynam turniej {}".format(len(population_List)))
            tournament_result = Modi.tournament(population_List,graph)
            population_List = tournament_result[0]
            print("koncze turniej {}".format(len(population_List)))
            if tournament_result[1] == best_dna_lenght:
                without_change += 1
            elif tournament_result[1] < best_dna_lenght:
                print("zmieniam z {} na {}".format(best_dna_lenght,tournament_result[1]))
                best_dna_lenght = tournament_result[1]
                best_dna_string = tournament_result[2]
                without_change = 0
        if without_change == 10:
            break
  
    print("dna reconstruction with lowest shift lenght: {} {}".format(best_dna_lenght,best_dna_string))
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
