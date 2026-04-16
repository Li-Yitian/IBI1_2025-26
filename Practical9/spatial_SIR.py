#import necessary libraries
import os
import numpy as np
import matplotlib.pyplot as plt
#initialize a 100x100 grid where all cells=0 (susceptible)
population = np.zeros((100,100))
#randomly infect 1 cell
outbreak = np . random . choice ( range (100) ,2)
population [ outbreak [ 0 ] , outbreak [ 1 ] ] = 1
base_dir = "Practical9"
os.makedirs(base_dir, exist_ok=True)

run_num = 1
while os.path.exists(os.path.join(base_dir, f"spatial_run{run_num}")):
    run_num += 1

save_folder = os.path.join(base_dir, f"spatial_run{run_num}")
os.makedirs(save_folder)

#plot of the initial state of the population
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Spatial SIR - Step 0")
plt.savefig(os.path.join(save_folder, "step_0.png"), bbox_inches='tight')
plt.close()

#initialize variables
beta=0.3 #infection rate
gamma=0.05 #recovery rate
step=100
#start the simulation
for step in range(1, step + 1):
    new_pop = population.copy()
    infected_x, infected_y = np.where(population == 1)#find the coordinates of the infected cells
    for x, y in zip(infected_x, infected_y):#define the 8 neighboring cells
        neighbors = [
            (x-1, y-1), (x-1, y), (x-1, y+1),
            (x, y-1),            (x, y+1),
            (x+1, y-1), (x+1, y), (x+1, y+1)
        ]

        for nx, ny in neighbors:
            if 0 <= nx < 100 and 0 <= ny < 100:#make sure the neighbor is within the grid
                if population[nx, ny] == 0:
                    if np.random.rand() < beta:
                        new_pop[nx, ny] = 1
    for x, y in zip(infected_x, infected_y):
        if np.random.rand() < gamma:
            new_pop[x, y] = 2

    population = new_pop
    if step in [10, 50, 100]:
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Spatial SIR - Step {step}")
        plt.savefig(os.path.join(save_folder, f"step_{step}.png"), bbox_inches='tight')
        plt.close()
