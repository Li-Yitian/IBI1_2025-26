#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import os
#define the SIR_vaccination model
def SIR_vaccination_model(vaccine_fraction):
    N=10000 #total population
    I=1 #initial infected
    R=0 #initial recovered
    V=int(N * vaccine_fraction) #initial vaccinated
    S=max(0, N-I-R-V) #initial susceptible
    beta=0.3 #infection rate
    gamma=0.05 #recovery rate
    timestep=1000
    I_list=[I]#list to store infected population
    for i in range(timestep):
        p_infect=beta*I/N #probability of infection
        new_infections=np.random.binomial(S, p_infect) #new infections
        new_recoveries=np.random.binomial(I, gamma) #new recoveries
        S=S-new_infections
        I=I+new_infections-new_recoveries
        R=R+new_recoveries
        I_list.append(I)#record the number of infected individuals at each time step
    return I_list
#for loop to run the model for different vaccine fractions
vaccine_fraction = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
labels = [f"{int(v*100)}% Vaccinated" for v in vaccine_fraction]
plt.figure(figsize=(9,5),dpi=150)#plot the results
for v, label in zip(vaccine_fraction, labels):
    curve = SIR_vaccination_model(v)
    plt.plot(curve, label=label)
plt.xlabel("Time")
plt.ylabel("Infected individuals")
plt.title("SIR model with vaccination")
plt.legend()
save_folder = os.path.join("Practical9", "Practical9_SIR_vaccination_Results")
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
i = 1
while os.path.exists(os.path.join(save_folder, f"SIR_vaccination_{i}.png")):
    i += 1
filename = os.path.join(save_folder, f"SIR_vaccination_{i}.png")
plt.savefig(filename)
plt.show()
#save different results in this folder

