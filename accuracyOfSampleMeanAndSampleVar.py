import random
import math
from functools import reduce


def generate_exp(rate): 
    """
    Generates random value from Exponential with rate rate.
    """
    u = random.uniform(0, 1)
    return - math.log(1-u) / rate

def generate_hyper_exp(rate1, rate2, p):
    """
    Generates random value from Exp rate 1 with probability p, and 
    random value from Exp rate 2 with probability 1-p
    """
    assert (0 <= p and p <= 1)
    u = random.uniform(0, 1)
    if u < p: 
        return generate_exp(rate1)
    else: 
        return generate_exp(rate2)
    
def calculate_sample_mean(data: list[int]) -> int: 
    assert(len(data) > 0)
    return sum(data) / len(data)

def caluculate_sample_variance(data: list[int], known_mean=None) -> int: 
    mean_to_use = known_mean if known_mean else calculate_sample_mean(data)
    return reduce( lambda x, y: x + y, map(lambda x: (x - mean_to_use) ** 2, data) ) / len(data)

if __name__=="__main__":

    exp1_data, exp2_data, hyperexp_data = [], [], []
    for i in range(30): 
        exp1_data.append(generate_exp(1))
        exp2_data.append(generate_exp(.01))
        hyperexp_data.append(generate_hyper_exp(1, .01, .99))

    print("------ COMPUTING WITH 30 SAMPLES -----")
    print(f"Exp 1 - Sample Mean: {calculate_sample_mean(exp1_data)} - Sample Var (known mean): {caluculate_sample_variance(exp1_data, 1)} - Sample Var (unknown mean): {caluculate_sample_variance(exp1_data)}")
    print(f"Exp 1 - Sample Mean: {calculate_sample_mean(exp2_data)} - Sample Var (known mean): {caluculate_sample_variance(exp2_data, 100)} - Sample Var (unknown mean): {caluculate_sample_variance(exp1_data)}")
    print(f"Exp 1 - Sample Mean: {calculate_sample_mean(hyperexp_data)} - Sample Var (known mean): {caluculate_sample_variance(hyperexp_data, 1.99)} - Sample Var (unknown mean): {caluculate_sample_variance(hyperexp_data)}")

    exp1_data, exp2_data, hyperexp_data = [], [], []
    for i in range(100): 
        exp1_data.append(generate_exp(1))
        exp2_data.append(generate_exp(.01))
        hyperexp_data.append(generate_hyper_exp(1, .01, .99))

    print("------ COMPUTING WITH 100 SAMPLES -----")
    print(f"Exp 1 - Sample Mean: {calculate_sample_mean(exp1_data)} - Sample Var (known mean): {caluculate_sample_variance(exp1_data, 1)} - Sample Var (unknown mean): {caluculate_sample_variance(exp1_data)}")
    print(f"Exp 1 - Sample Mean: {calculate_sample_mean(exp2_data)} - Sample Var (known mean): {caluculate_sample_variance(exp2_data, 100)} - Sample Var (unknown mean): {caluculate_sample_variance(exp1_data)}")
    print(f"Exp 1 - Sample Mean: {calculate_sample_mean(hyperexp_data)} - Sample Var (known mean): {caluculate_sample_variance(hyperexp_data, 1.99)} - Sample Var (unknown mean): {caluculate_sample_variance(hyperexp_data)}")





