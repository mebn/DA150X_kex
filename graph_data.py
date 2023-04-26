import matplotlib.pyplot as plt
from pathlib import Path


##### CONFIG #####
RYZEN = "./results/ryzen/"
GTX1650 = "./results/gtx1650/"
GTX1070 = "./results/gtx1070/"
GRAPHS_FOLDER = "./results/graphs/"
TABLES_FOLDER = "./results/tables/"
##### CONFIG END #####


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
    scores = {"ryzen": [], "gtx1650": [], "gtx1070": []}
    times = {"ryzen": [], "gtx1650": [], "gtx1070": []}

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

        # plt.show()
        plt.savefig(f"{GRAPHS_FOLDER}{filename}.png", bbox_inches="tight", dpi=300)


def generate_tables():
    # COLS: mk01.fjs - mk10.fjs
    # ROWS: (mean, median for each CPU/GPU) score and runtime, x times GPU 1 and 2 faster then CPU, x times GPU 1 faster then GPU 2, best score, best runtime
    pass


def main():
    create_paths()
    generate_graphs()
    generate_tables()


main()