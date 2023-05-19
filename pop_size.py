import subprocess
from pathlib import Path
import os


##### CONFIG #####
RUNS = 10
RESULTS_FOLDER = f"./results/pop_size/ryzen/"
# RESULTS_FOLDER = f"./results/pop_size/gtx1650/"
# RESULTS_FOLDER = f"./results/pop_size/gtx1070/"
##### CONFIG END #####

def run_files():
    for pop_size in ["pop100", "pop500", "pop1000", "pop2000", "pop4000"]:
        print("running pop_size:", pop_size)

        for file in ["mk01", "mk05", "mk08"]:
            print(f"running: {file}.fjs")
            outputs = []

            # run RUNS times
            for run in range(RUNS):
                print(f"run: {run+1}/{RUNS}")
                output = subprocess.Popen([f"{os.getcwd()}/exes/{pop_size}.exe", f"./data/{file}.fjs"], stdout=subprocess.PIPE, shell=True, cwd=os.getcwd()).communicate()[0]
                print(str(output, "utf-8"))
                outputs.append(str(output, "utf-8"))

            # write to file
            Path(RESULTS_FOLDER).mkdir(parents=True, exist_ok=True)
            with open(RESULTS_FOLDER + file + pop_size, "w") as f:
                for output in outputs:
                    f.write(output.strip() + "\n")


def main():
    run_files()


main()