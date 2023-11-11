import random
import numpy as np
import pandas as pd

from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = os.path.join(BASE_DIR, 'genetic_algorithm/data/dataset.csv')


def load_dataset():
    df = pd.read_csv(DATA_PATH)
    return df


def fitness_function(individual, dataset):
    return np.sum((dataset['Y'] - individual) ** 2)


def initialize_population(population_size, dataset_size):
    return [np.random.uniform(0, 10, dataset_size) for _ in range(population_size)]


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = np.concatenate(
        (parent1[:crossover_point], parent2[crossover_point:]))
    return child


def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] += random.uniform(-0.5, 0.5)
    return individual
