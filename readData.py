def readData(inputFile):
    file = open("data/{}".format(inputFile))
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    return(list(map(int, contents_split)))

if __name__ == "__main__": 
    setA = readData("datasetA.txt")
    setB = readData("datasetB.txt")
    setC = readData("datasetC.txt")