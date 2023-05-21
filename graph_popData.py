import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import numpy as np
#behövs ej här.
#import dataframe_image as dfi


##### CONFIG #####
#Behöver justera dessa.
RYZEN = "./results/pop_size/ryzen/"
GTX1070 = "./results/pop_size/gtx1070/"
POPANDTIME_FOLDER = "./results/graphs/popANDtime/"
POPANDSCORE_FOLDER = "./results/graphs/popANDscore/"
##### CONFIG END #####

#här uppp
times = {"ryzen": [], "gtx1070": []}
scores = {"ryzen": [],  "gtx1070": []}

#använder nestade listor istället. 
cpuTimes = []
gpuTimes = []


def create_paths():
    Path(POPANDTIME_FOLDER).mkdir(parents=True, exist_ok=True)
    Path(POPANDSCORE_FOLDER).mkdir(parents=True, exist_ok=True)


def read_data(path, file):
    scores = []
    times = []

    with open(path + file, "r") as f:
        for line in f:
            score, time = line.split()
            scores.append(int(score))
            times.append(int(time))

    return scores, times


# ska läsa in rätt data för varje 
def prod_data():
    

    # ska läsa in alla pop. 

    for i in [1, 5, 8]:
      for j in [100, 500, 1000, 2000, 4000]:
        filename = f"mk0{i}pop{j}" if i < 10 else f"mk{i}pop{j}"
        #test
      #  print(filename)

        #först medelvärde för score. Sedan för scores innehåller nu alla värden. 

        for folder, processor in zip([RYZEN, GTX1070], ["ryzen","gtx1070"]):
            score, time = read_data(folder, filename)
            scores[processor].append(score)
            times[processor].append(time)

        
      
    averageCPU = []
    averageGPU = []
    gpuOverCPU = []

    avScoreCPU = []
    avScoreGPU = []


    for i in range(0,15):
        averageCPU.append((sum(times["ryzen"][i]) / 10))
        averageGPU.append((sum(times["gtx1070"][i]) / 10))
        gpuOverCPU.append(averageCPU[i] / averageGPU[i])

        avScoreCPU.append((sum(scores["ryzen"][i]) / 10))
        avScoreGPU.append((sum(scores["gtx1070"][i]) / 10))

    x_values = [100, 500, 1000, 2000, 4000]

    

    part1, part2, part3 = split_list(gpuOverCPU)

    plt.plot(x_values, part1[:5], label='mk01')
    plt.plot(x_values, part2[:5], label='mk05')
    plt.plot(x_values, part3[:5], label='mk08')

    plt.xlabel('Population')
    plt.ylabel('Execution time for the GPU divided by the execution time for the CPU.')
    plt.title('Comparison of execution time at different population sizes.')
    plt.legend()
  #  plt.show()
    plt.savefig(f"{POPANDTIME_FOLDER}popANDtime.png", bbox_inches="tight")

    
    plt.clf() 

    part1GPU, part2GPU, part3GPU = split_list(avScoreGPU)
    part1CPU, part2CPU, part3CPU = split_list(avScoreCPU)


    plt.plot(x_values, part1GPU[:5], label='GPU')
    plt.plot(x_values, part1CPU[:5], label='CPU')
  

    plt.xlabel('Score and population with mk01')
    plt.ylabel('Score.')
    plt.title('Population.')
    plt.legend()
    plt.savefig(f"{POPANDSCORE_FOLDER}mk01score.png", bbox_inches="tight")

    plt.clf() 


    plt.plot(x_values, part2GPU[:5], label='GPU')
    plt.plot(x_values, part2CPU[:5], label='CPU')
  

    plt.xlabel('Score and population with mk05')
    plt.ylabel('Score.')
    plt.title('Population.')
    plt.legend()
    plt.savefig(f"{POPANDSCORE_FOLDER}mk05score.png", bbox_inches="tight")


    plt.clf() 

    
    plt.plot(x_values, part3GPU[:5], label='GPU')
    plt.plot(x_values, part3CPU[:5], label='CPU')
  

    plt.xlabel('Score and population with mk08')
    plt.ylabel('Score.')
    plt.title('Population.')
    plt.legend()
    plt.savefig(f"{POPANDSCORE_FOLDER}mk08score.png", bbox_inches="tight")


    # ska nu skapa en graf. 




def split_list(a_list):
    third = len(a_list) // 3
    return a_list[:third], a_list[third:2*third], a_list[2*third:]



"""

För skall man skapa en graf där man för varje population size för mk01, mk05, mk08 se hur förhållandet de olika tiderna påverkas 
av population.  
Sedan skall man skapa en graf där man för varje 

"""


def main():


    create_paths()

    prod_data()
# kan börja med att få fram rätt data

   ## generate_graphs()


main()
