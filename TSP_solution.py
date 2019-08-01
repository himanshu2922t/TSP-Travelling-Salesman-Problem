# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:59:48 2019

@author: Himanshu Rathore
"""

# importing libraries
import random
import numpy as np
import matplotlib.pyplot as plt

# input for total cities
total_cities = int(input("Enter total number of cities: "))

#input for distance/cost etc. and creating cost matrix (can be used in case of asymmetric problem)
"""
rows_list = list()
for i in range(total_cities):
    row = input("Enter distance between(or cost) city {} and other cities in space separated form: ".format(i+1)).split()
    row = list(map(int, row))
    row.insert(i, 0) 
    rows_list.append(row)

cost_matrix = np.array(rows_list)
"""

###############################################
#######  Creating Cost/Distance Matrix  #######

# For simplification Generating coordinates of cities randomly
cities_cord = [random.sample(range(100), 2) for x in range(total_cities)]
print("City Coordinates:",cities_cord)

cost_matrix = list()

# Calculating distances btw each city
for city1 in cities_cord:
    row = map(lambda city2: round(((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) ** 0.5, 2) , cities_cord)
    cost_matrix.append(list(row))

# converting distance list into array
cost_matrix = np.array(cost_matrix)

# Now filling diagonal values as infinity
np.fill_diagonal(cost_matrix, float('inf'))
print("Cost Matrix:\n",cost_matrix)

###############################################
#######         Solution for TSP        #######

def TSP(cost_matrix, start=None):
    """ Solution by more simplifying and optimizing 
        to going to nearest unvisited city (Heuristic Algorithm) """
    #Making start point as First City
    if start is None:
        start = 0   #first city index is 0 in array
        
    dist = 0.0
    must_visit = list(range(total_cities))  #to maintain list of unvisited cities
    path = [start+1]    # Adding city 1 in path as starting point
    
    while len(must_visit)>1:
        dist += np.amin(cost_matrix[start, 1:])     # Gives nearest unvisited city distance
        start = np.argmin(cost_matrix[start, 1:])+1 # Gives City Number 
        path.append(start+1)    # Adding visited city in path
        cost_matrix[:, [start]] = float('inf')  #Making visited city column's values as infinity
                                                #so that no longer taking part in minnimum
        
        must_visit.remove(start)    # Removing visited city from unvisited list
        
    dist += cost_matrix[start,0]    # Adding distance of last city from start city
    path.append(1)      # Adding start city in path to complete cycle
    
    return dist, path

shortest_dist, best_path = TSP(cost_matrix)
print("Optimized Distance/Cost:",shortest_dist)
print("Best Route:",best_path)

###############################################
#######       PLoting Best Route        #######

plt.plot([cities_cord[ best_path[i]-1 ][0] for i in range(total_cities+1)], \
          [cities_cord[ best_path[i]-1 ][1] for i in range(total_cities+1)], 'xb-')
