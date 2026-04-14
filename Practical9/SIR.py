#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import os
#define the SIR model
def SIR_model():
    N=10000 #total population
    I=1 #initial infected
    R=0 #initial recovered
    S=N-I-R #initial susceptible
    beta=0.3 #infection rate
    gamma=0.05 #recovery rate
    timestep=1000
    S_list=[S]#list to store susceptible population
    I_list=[I]#list to store infected population
    R_list=[R]#list to store recovered population
    for i in range(timestep):
        p_infect=beta*I/N #probability of infection
        new_infections=np.random.binomial(S, p_infect) #new infections
        new_recoveries=np.random.binomial(I, gamma) #new recoveries
        S=S-new_infections
        I=I+new_infections-new_recoveries
        R=R+new_recoveries
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
    return S_list, I_list, R_list
S_list, I_list, R_list = SIR_model()
#plot the results
plt.figure(figsize=(8,4),dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('SIR Model Simulation')
plt.legend()
save_folder = os.path.join("Practical9", "Practical9_SIR_Results")
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
i = 1
while os.path.exists(os.path.join(save_folder, f"SIR_{i}.png")):
    i += 1
filename = os.path.join(save_folder, f"SIR_{i}.png")
plt.savefig(filename)
plt.show()
#save different results in this folder

