import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import numpy as np
import dataframe_image as dfi


##### CONFIG #####
RYZEN = "./results/ryzen/"
GTX1650 = "./results/gtx1650/"
GTX1070 = "./results/gtx1070/"
GRAPHS_FOLDER = "./results/graphs/"
TABLES_FOLDER = "./results/tables/"
##### CONFIG END #####

times = {"ryzen": [], "gtx1650": [], "gtx1070": []}
scores = {"ryzen": [], "gtx1650": [], "gtx1070": []}

def create_paths():
    Path(GRAPHS_FOLDER).mkdir(parents=True, exist_ok=True)
    Path(TABLES_FOLDER).mkdir(parents=True, exist_ok=True)


def read_data(path, file):
    scores = []
    times = []

    with open(path + file, "r") as f:
        for line in f:
            score, time = line.split()
            scores.append(int(score))
            times.append(int(time))

    return scores, times


def generate_graphs():
    labels = ["Ryzen 5 3600", "GTX 1650 Max-Q", "GTX 1070"]

    for i in range(1, 11):
        filename = f"mk0{i}" if i < 10 else f"mk{i}"

        for folder, processor in zip([RYZEN, GTX1650, GTX1070], ["ryzen", "gtx1650", "gtx1070"]):
            score, time = read_data(folder, filename)
            scores[processor].append(score)
            times[processor].append(time)

        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.title(f"Scores, {filename}.fjs")
        plt.ylabel("Score")
        plt.boxplot(
            [scores["ryzen"][-1], scores["gtx1650"][-1], scores["gtx1070"][-1]],
            labels=labels,
            showmeans=True
        )

        plt.subplot(1, 2, 2)
        plt.title(f"Runtimes, {filename}.fjs")
        plt.ylabel("μs")
        plt.boxplot(
            [times["ryzen"][-1], times["gtx1650"][-1], times["gtx1070"][-1]],
            labels=labels,
            showmeans=True
        )

        plt.savefig(f"{GRAPHS_FOLDER}{filename}.png", bbox_inches="tight", dpi=300)


def generate_tables():
    columns = ["mk01", "mk02", "mk03", "mk04", "mk05", "mk06", "mk07", "mk08", "mk09", "mk10"]

    ##### mean and median scores #####

    index = [
        "Ryzen",
        "GTX 1650",
        "GTX 1070",
        # "Ryzen (median)",
        # "GTX 1650 (median)",
        # "GTX 1070 (median)",
    ]

    data = [
        [round(np.mean(x)) for x in scores["ryzen"]],
        [round(np.mean(x)) for x in scores["gtx1070"]],
        [round(np.mean(x)) for x in scores["gtx1650"]],
        # [round(np.median(x)) for x in scores["ryzen"]],
        # [round(np.median(x)) for x in scores["gtx1070"]],
        # [round(np.median(x)) for x in scores["gtx1650"]],
    ]
        
    df = pd.DataFrame(data, index=index, columns=columns, dtype=object)
    dfi.export(df, f"{TABLES_FOLDER}scores.png", table_conversion="matplotlib", dpi=300)


    ##### mean runtimes #####

    index = [
        "Ryzen",
        "GTX 1650",
        "GTX 1070",
        # "Ryzen (median)",
        # "GTX 1650 (median)",
        # "GTX 1070 (median)",
    ]

    data = [
        [round(np.mean(x)) for x in times["ryzen"]],
        [round(np.mean(x)) for x in times["gtx1070"]],
        [round(np.mean(x)) for x in times["gtx1650"]],
        # [round(np.median(x)) for x in times["ryzen"]],
        # [round(np.median(x)) for x in times["gtx1070"]],
        # [round(np.median(x)) for x in times["gtx1650"]],
    ]
        
    df = pd.DataFrame(data, index=index, columns=columns, dtype=object)
    dfi.export(df, f"{TABLES_FOLDER}runtimes.png", table_conversion="matplotlib", dpi=300)

    ##### xPU speed advantage over yPU #####

    index = [
        "Ryzen / GTX 1650",
        "Ryzen / GTX 1070",
        "GTX 1650 / GTX 1070",
    ]

    data = [
        [round(np.mean(cpu) / np.mean(gpu), 2) for cpu, gpu in zip(times["ryzen"], times["gtx1650"])],
        [round(np.mean(cpu) / np.mean(gpu), 2) for cpu, gpu in zip(times["ryzen"], times["gtx1070"])],
        [round(np.mean(cpu) / np.mean(gpu), 2) for cpu, gpu in zip(times["gtx1650"], times["gtx1070"])],
    ]
        
    df = pd.DataFrame(data, index=index, columns=columns, dtype=object)
    dfi.export(df, f"{TABLES_FOLDER}speed_advantage.png", table_conversion="matplotlib", dpi=300)



def main():
    create_paths()
    generate_graphs()
    generate_tables()


main()
