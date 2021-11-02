from readData import readData 

def computeProbMLE_1(dataset):
    freq, probAll = {}, {} # Probabilities of 1,2,3,4,5,6

    for d in dataset:
        if d not in freq:
            freq[d]  = 1
        else:
            freq[d]  += 1

    for key in freq:
        prob = round(freq[key]/len(dataset) * 100, 1)
        probAll[key] = prob
        
    return probAll

def computeProbBayes_2(dataset, datasetName):
    probSix = {} # Probabilities of 6 only

    for i in range(1, 10):  # Test with ⊖ ranging from 0.1 to 0.9
        # Since any p(⊖) is uniform, p(D) is impossible to know, and
        # p(⊖|D) (what we want to compute) is proportional to p(D|⊖)
        # we will compute p(D|⊖). Call p(D|⊖) 'prob'
        t = i/10
        prob = 1

        for d in dataset:
            if d == 6:
                prob *= t
            else:
                prob *= (1-t)
        
        # prob is really small and hard to see the difference
        # so we multiply it by a constant to compare easily
        scaledProb = prob
        if datasetName == "A":
            scaledProb *= 10**8
        elif datasetName == "B":
            scaledProb *= 10**70
        else:
            scaledProb *= 10**300
        probSix[t] = scaledProb

    return probSix

def computeProbBayes_34(dataset, tProbList, datasetName):
    probSix = {} # Probabilities of 6 only

    for t in tProbList:  # Test with input ⊖ 
        # Since p(D) is impossible to know, and
        # p(⊖|D) is proportional to p(D|⊖) * p(⊖),
        # we will compute p(D|⊖) * p(⊖) Call p(D|⊖) * p(⊖) 'prob'
        tProb = tProbList[t]
        # theta = eval(t)
        # numOfSix = 0

        for d in dataset:
            if d == 6:
                prob *= eval(t)
            else:
                prob *= (1-eval(t))

        # for d in dataset:
        #     if d == 6:
        #         numOfSix += 1

        # if datasetName == "A":
        #     scaledProb = (10**8)*((theta)**(numOfSix))*(10**8)*((1 - theta)**(len(dataset) - numOfSix))*tProb
        # elif datasetName == "B":
        #     scaledProb = (10**70)*((theta)**(numOfSix))*(10**70)*((1 - theta)**(len(dataset) - numOfSix))*tProb
        # else:
        #     scaledProb = (10**300)*((theta)**(numOfSix))*(10**300)*((1 - theta)**(len(dataset) - numOfSix))*tProb
        # probSix[t] = scaledProb
        
        # prob is really small and hard to see the difference
        # so we multiply it by a constant to compare easily
        scaledProb = prob * tProb
        if datasetName == "A":
            scaledProb *= 10**8
        elif datasetName == "B":
            scaledProb *= 10**70
        else:
            scaledProb *= 10**300
        probSix[t] = scaledProb

    return probSix

def displayResults(method, scenario, probSetA, probSetB, probsetC, tProbList = None):
    probSets = {"A": probSetA, "B": probSetB, "C": probsetC}

    print()
    print("***** SCENARIO {} *****".format(scenario))

    for probSetKey in probSets:    
        currentSet = probSets[probSetKey]
        print("Dataset {} - Size {} - {}".format(probSetKey, "20" if probSetKey == "A" else "200" if probSetKey == "B" else "2000", "MLE" if method == "M" else "Bayesian"))
        if method == "M":
            for val in currentSet:
                print("Probability of {}: {}%".format(str(val), str(currentSet[val])))
        elif method == "B":
            print("Probability of 6")
            for theta in currentSet:
                tProb = "is uniform" if scenario == "2" else "= " + str(int(tProbList[theta]*100)) + "%"
                print("⊖={} | p(⊖) {}: {}".format(str(theta), tProb, str(currentSet[theta])))
        print()

    print("-----------------------------------")

def main():
    # Scenario 1: Don't know if die is loaded with fixed distribution, so won't use prior probability (use MLE)
    # Scenario 2: Unsure if die is fair, so any theta has equal probability (use Bayesian, test with thetas from 0.1 to 0.9)
    # Scenario 3: Think that die favors 6: p(theta=0.5) = 45%, p(theta=0.6) = 35%, p(theta=1/6) = 20% (use Bayesian, test with 3 thetas)
    # Scenario 4: Think that die favors 6: p(theta=0.5) = 52%, p(theta=0.6) = 28%, p(theta=1/6) = 20% (use Bayesian, test with 3 thetas)

    # theta probability lists for scenario 3 & 4
    l3 = {"0.5": 0.45, "0.6": 0.35, "1/6": 0.20}
    l4 = {"0.5": 0.52, "0.6": 0.28, "1/6": 0.20}

    # Read data from text files
    datasetA = readData("datasetA.txt")
    datasetB = readData("datasetB.txt")
    datasetC = readData("datasetC.txt")

    displayResults("M", "1",  computeProbMLE_1(datasetA), computeProbMLE_1(datasetB), computeProbMLE_1(datasetC))
    displayResults("B", "2",  computeProbBayes_2(datasetA, "A"), computeProbBayes_2(datasetB,"B"), computeProbBayes_2(datasetC,"C"))
    displayResults("B", "3",  computeProbBayes_34(datasetA,l3,"A"), computeProbBayes_34(datasetB, l3,"B"), computeProbBayes_34(datasetC,l3,"C"), l3)
    displayResults("B", "4",  computeProbBayes_34(datasetA,l4,"A"), computeProbBayes_34(datasetB, l4,"B"), computeProbBayes_34(datasetC,l4,"C"), l4)

if __name__ == "__main__":
    main()
