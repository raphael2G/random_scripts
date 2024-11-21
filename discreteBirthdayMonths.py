import random



def generateRandomBirthMonth(): 
    return random.randint(1, 12)

def howManyUniqueBirthMonths(n: int):
    birthmonths = []
    for i in range(n): 
        birthmonths.append(generateRandomBirthMonth())

    repeats = []
    for i in range(n):
        repeats.append(len(list(filter(lambda x: x == i, birthmonths))))

    return len(list(filter(lambda x: x == 1, repeats)))

TRIALS = 1000

for i in range(50, 51): 
    cumulative = 0
    for trial in range(TRIALS): 
        cumulative += howManyUniqueBirthMonths(i)

    print("Distinct Birthmonths with", i, " people: ", cumulative/TRIALS)

