import random

'''
We are given a line segment, [0, 1]. Two darts are each independently
thrown uniformly at random within the line segment. What is the probability
that the value of one dart is at least three times the value of the other?
'''

def simulateThrowing2Darts(trials: int): 
    successes = 0
    for trial in range(trials): 
        dart1, dart2 = random.uniform(0, 1), random.uniform(0, 1)
        if (dart1 >= 3 * dart2 or dart2 >= 3 * dart1): 
            successes += 1

    print(f"After {trials} trials, probability is {successes/trials * 100}")


'''
A dart is thrown uniformly at random at the unit interval [0, 1]. The dart
splits the interval into two segments, one to its right and one to its left.
What is the expected length of the smaller segment?
'''
def dartsSplitSegments(trials: int): 
    cumulativeValues = 0
    for trial in range(trials): 
        dart1 = random.uniform(0, 1)
        cumulativeValues += min(dart1, 1 - dart1)

    print(f"The expected value of the smaller segment determined by a dart's throw is {cumulativeValues/trials} over {trials} trials")



# simulateThrowing2Darts(1000000)
dartsSplitSegments(1000000)
    
