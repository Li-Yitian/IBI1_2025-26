#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#initialize a 100x100 grid where all cells=0 (susceptible)
population = np.zeros((100,100))
#randomly infect 1 cell
outbreak = np . random . choice ( range (100) ,2)
population [ outbreak [ 0 ] , outbreak [ 1 ] ] = 1
#initialize variables
beta=0.3 #infection rate
gamma=0.05 #recovery rate