
import random

reads= []
def addingErrorsFunc(seqFragment, percentError):
    """
    -Input: 
        1: seqFragment: sequence fragment, type: string
        2: percentError: error rate, type: integer
    -Functionality: multiple user input error by length of read fragment to generate number of 
                    errors (errorNum) to use. Generate a list of individual nucleotides from
                    fragment. Loop through the nucleotides and add errors by replacing them 
                    using their index.
    -Output: 
        1: seqFragmentNew: same input genome fragment but with errors, type: string
    """
    errorNum = round(len(seqFragment)*(percentError/100))
    alphabetNoA = ['T', 'C', 'G']
    alphabetNoT = ['A', 'C', 'G']
    alphabetNoC = ['A', 'G', 'T']
    alphabetNoG = ['A', 'C', 'T']

    fragments= list (seqFragment)
    # generate unique (without replacement) random numbers with sample size equal to errorNum 
    # (e.g. 10% of the length of the input fragment). The generated random numbers are within 
    # the range 0 and the length of the input fragment.
    cps = random.sample(range(0, len(seqFragment)), errorNum)
    for i  in cps:
        randomACGT= random.randint(0, 3)
        if randomACGT == 3:
            fragments[i] = ''
        else:
            if fragments[i] == 'A':
                fragments[i] = alphabetNoA[randomACGT]
            elif fragments[i] == 'T':
                fragments[i] = alphabetNoT[randomACGT]
            elif fragments[i] == 'C':
                fragments[i] = alphabetNoC[randomACGT]
            else:
                fragments[i] = alphabetNoG[randomACGT]
    seqFragmentNew= "".join(fragments)
    return seqFragmentNew
#-------------------------
def fragmentsGeneratorFunc(genome, readLenMin, readLenMax, errorStatus, errorRate):
    """ 
    -Input: 
        1: genome: refernce genome string, type: string
        2: readLenMin: smallest read length size, type: integer
        3: readLenMax: largest read length size, type: integer
        4: errorStatus: fragment with or without error, string
        5: errorRate: error rate, type: integer
    -Functionality: generate read fragments with/without errors from a refernce genome
    -Output: 
        1: list of read fragments type: list
    """
    
    readLen = random.randint(readLenMin, readLenMax)
    startPos = random.randint(0,len(genome)-readLen)
    read1, read2, read3 = (genome[:startPos],
                           genome[startPos:startPos+readLen],
                           genome[startPos+readLen:])
    if len(read2) !=0 and len(read2) >=readLenMin:
        if errorStatus == 'YES':
            read2WithError = addingErrorsFunc(read2, errorRate)
            reads.append(read2WithError)
        else:
            reads.append(read2)
    for read in [read1, read3]:
        if len(read) !=0 and len(read) >=readLenMin:
            if len(read) > readLenMax:
                fragmentsGeneratorFunc(read, readLenMin, readLenMax, errorRate, errorStatus)
            else:
                if errorStatus == 'YES':
                    readWithError = addingErrorsFunc(read, errorRate)
                    reads.append(readWithError)
                else:
                    reads.append(read)
    return reads
#-------------------------

result= fragmentsGeneratorFunc(genome='CAAGACCATGCAGCCTCTCTGCTTTCATGGAGTGCTGCTAAGCCAGGGATCCTTCATATTTCCTAACAGACTTT', readLenMin= 5, readLenMax= 10, errorStatus='YES', errorRate= 20)
print(result) 