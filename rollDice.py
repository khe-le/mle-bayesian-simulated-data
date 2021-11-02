import numpy as np

# Dice has a 10% chance of showing 1, 10% of 2, 10% of 3, 10% of 4, 10% of 5, and 50% of 6

def rollLoadedDice(size):
    data = []
    for i in range(size):
        diceVal = np.random.choice([1,2,3,4,5,6], p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.5])
        data.append(diceVal)
    return data

def saveData(outputFile, dataset):
    with open("data/{}.txt".format(outputFile), 'w') as f:
        for val in dataset:
            f.writelines("{}\n".format(str(val))) 

# Generate datasets from rolling the dice 20, 200, 2000 times
if __name__ == "__main__":
    # dataA = rollLoadedDice(20)
    # saveData('datasetA', dataA)

    # dataB = rollLoadedDice(200)
    # saveData('datasetB', dataB)

    # dataC = rollLoadedDice(2000)
    # saveData('datasetC', dataC)
    print()