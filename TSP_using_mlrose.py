# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:36:26 2019

@author: Himanshu Rathore
"""
# importing libraries
import mlrose
import random
import matplotlib.pyplot as plt

# input for total cities
total_cities = int(input("Enter total number of cities: "))

# Generating Random coordinates for cities
cities_cord = [random.sample(range(100), 2) for x in range(total_cities)]



""" TSP Solution Using mlrose (library for randomized optimization) """

fitness_coords = mlrose.TravellingSales(coords = cities_cord)
problem_fit = mlrose.TSPOpt(length = total_cities, fitness_fn = fitness_coords, maximize=False)
best_path, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2, max_attempts = 100, random_state = 2)

print("Optimized Route:", best_path) 
print("Least Cost/Distance:",round(best_fitness,2))
					      
# Plotting Route
plt.plot([cities_cord[best_path[i % total_cities]][0] for i in range(total_cities+1)], \
          [cities_cord[best_path[i % total_cities]][1] for i in range(total_cities+1)], 'xb-')





""" TSP Solution using Graph Theory Concepts """

def distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) ** 0.5

def travelling_salesman(cities_cord, start=None):
    if start is None:
        start = cities_cord[0]
    must_visit = list(cities_cord)
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path

def total_distance(points):
        return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])


print(travelling_salesman(cities_cord))
print(total_distance(travelling_salesman(cities_cord)))   
