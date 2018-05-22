import primerSetFinder



def largeFileReader():
    largeFile = 'nonRedundant.fasta'
    lineCount = 0
    coliPoint = 0
    coliSeq = ''
    file = open(largeFile,'r')
    for line in file:
        if '>' in line:
            if coliPoint == 1:
                primerSetFinder.fwdPrimerFinder(coliSeq,0,0)
                file.close()
                break
            if 'Escherichia coli' in line:
                coliPoint = 1
        elif coliPoint == 1:
            coliSeq = coliSeq + line
            lineCount += 1 