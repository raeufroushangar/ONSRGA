
import random

reads= []
def addingErrorsFunc(seqRead, percentError):
    """
    -Input: 
        1: seqRead: nucleic acid string, type: string
        2: percentError: error rate, type: integer
    -Functionality: multiple the desired error (percentError) by read size to estimate the number
                    of  errors to add to the read. Loop through the nucleotides in the read and add 
                    the estimated errors using indexing.
    -Output: 
        1: newSeqRead: same input nucleic acid string but with errors, type: string
    """
    errorNum = round(len(seqRead)*(percentError/100))
    alphabetNoA = ['T', 'C', 'G']
    alphabetNoT = ['A', 'C', 'G']
    alphabetNoC = ['A', 'G', 'T']
    alphabetNoG = ['A', 'C', 'T']

    fragments= list (seqRead)
    # generate unique (without replacement) random numbers with sample size equal to errorNum 
    # (e.g. 10% of the length of the input fragment). The generated random numbers are within 
    # the range 0 and the length of the input fragment.
    cps = random.sample(range(0, len(seqRead)), errorNum)
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
    newSeqRead= "".join(fragments)
    return newSeqRead
#-------------------------
def fragmentsGeneratorFunc(genome, readLenMin, readLenMax, errorStatus, errorRate):
    """ 
    -Input:
         1: genome: refernce genome string, type: string
         2: readLenMin: smallest read size, type: integer
         3: readLenMax: largest read size, type: integer
         5: errorRate: error rate, type: integer
    -Functionality: Generate a list of reads with/without errors from an input nucleic acid string.
    -Output: 
          1: list of reads, type: list
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