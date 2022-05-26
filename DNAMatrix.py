
MAX_SHIFT = 3

#Create N*N matrix with 0
def create_matrix(length_of_spectrum):
    return [[0]*length_of_spectrum for row in range(length_of_spectrum)]

#check if last n-1 elements of first oligonucleotide 
#match first n-1 ements of secound oligonucleotide
def perfect_match(left_oli, right_oli):
    r = len(right_oli)
    return True if(left_oli[1:] == right_oli[:r-1]) else False

#check if last element of first oligonucleotide 
#match first element of second oligonucleotide
def index_matches(left_list,right_list):
    return True if(left_list[-1] == right_list[0]) else False

#find shift value of oligonucleotide
"""
def find_shift(first,second):
    if(perfect_match(first,second)):
        return 1
    else:
        for shift in range(2,len(first)-1):
            if(first[shift:] == second[:len(second)-shift]):
                return shift
    return 0
"""

#fill created matrix with values of shifts
def fill_matrix(matrix,spectrum,length_of_spectrum):
    for row in range(length_of_spectrum):
        for column in range(length_of_spectrum):
            if(row == column):
                continue
            else:
                matrix[row][column] = calcDifference(spectrum[row],spectrum[column])#find_shift(spectrum[row],spectrum[column])

    return matrix

#combine oligonucleotides if its possible
def find_match(oligonucleotide):
    for row in range(len(oligonucleotide)):
        for column in range(row,len(oligonucleotide)):
            if(index_matches(oligonucleotide[row],oligonucleotide[column])):
                left_oli = oligonucleotide[row]
                right_oli = oligonucleotide[column]
                oligonucleotide.pop(column)
                oligonucleotide.pop(row)
                oligonucleotide.insert(0,left_oli[:-1]+right_oli)
                return oligonucleotide
    return []

#find pairs of oligonucleotide with one entrance
def find_oligonucleotide_with_one_entrance(matrix,length_of_spectrum):
    columns_to_eliminate = []
    matching_oligonucleotide =[]
    for row in range(length_of_spectrum):
        if(sum(matrix[row]) == 1):
            tmp_sum = tmp_ind = -1
            for element_in_row in matrix[row]:
                if(element_in_row == 1):
                    tmp_ind = matrix[row].index(element_in_row)
                    break

            if(tmp_ind in columns_to_eliminate):
                break

            #Check if there's only 1 connection to oligonucleotide
            else:
                for column in range(length_of_spectrum):
                    tmp_sum += matrix[column][tmp_ind]
                if(tmp_sum == 0):
                    matching_oligonucleotide.append([row,tmp_ind])
                else:
                    columns_to_eliminate.append(tmp_ind)

    return matching_oligonucleotide

#Convert matrix to dictionary
def matrix_to_list(matrix):
    return {key: matrix[key] for key in range(0,len(matrix))}
    #return [matrix[oli] for oli in range(0,len(matrix))]

def optimize_matrix(oligonucleotide_pair,spectrum,length_of_spectrum):
    optimized_matrix = []
    while(True):
        current_oligonucleotide = find_match(oligonucleotide_pair)
        if(current_oligonucleotide):
            optimized_matrix = oligonucleotide_pair
        else:
            break

    oligonucleotides_without_pair = []
    for row in range(length_of_spectrum):
        if(not(any(row in pair for pair in oligonucleotide_pair))):
            oligonucleotides_without_pair.append(row)

    for element in oligonucleotides_without_pair:
        oligonucleotide_pair.append([element])

    seqs = []
    for pairs in oligonucleotide_pair:
        seq = spectrum[pairs[0]]
        ### Dodać łączenie oligonukleotyd
        for row in range(1,len(pairs)):
            seq += spectrum[pairs[row]][-1]
        seqs.append(seq)

    optimized_matrix = matrix_to_list(seqs)
    #zwracać liste [[klucz, element],... ]
    return [i for i in optimized_matrix.values()]

def optimize_graph(spectrum):
    matrix = create_matrix(len(spectrum))
    filled_matrix=fill_matrix(matrix,spectrum,len(spectrum))
    print(filled_matrix)

    dst_matches = find_oligonucleotide_with_one_entrance(filled_matrix,len(spectrum))
    oligonucleotids = optimize_matrix(dst_matches,spectrum,len(spectrum))
    return (oligonucleotids,fill_matrix(matrix,oligonucleotids,len(oligonucleotids)))

def calcDifference(stringA, stringB, difference=0):
    if stringA[difference:] == stringB[:len(stringB) - difference]:
        return difference
    return calcDifference(stringA, stringB, difference + 1)

