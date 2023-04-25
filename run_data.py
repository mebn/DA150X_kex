import subprocess
from pathlib import Path


##### CONFIG #####
#PROCESSING_UNIT = "cpu"
PROCESSING_UNIT = "gpu"
RUNS = 10
#RESULTS_FOLDER = f"./results/ryzen/"
RESULTS_FOLDER = f"./results/gtx1650/"
#RESULTS_FOLDER = f"./results/gtx1070/"
##### CONFIG END #####


def make():
    subprocess.Popen(["make", PROCESSING_UNIT], stdout=subprocess.PIPE, shell=True).communicate()


def run_files():
    for num in range(1, 11):
        file = f"mk0{num}" if num != 10 else f"mk{num}"
        print(f"running: {file}.fjs")
        outputs = []

        # run RUNS times
        for run in range(RUNS):
            print(f"run: {run+1}/{RUNS}")
            output = subprocess.Popen(["a.exe", f"./data/{file}.fjs"], stdout=subprocess.PIPE, shell=True).communicate()[0]
            print(str(output, "utf-8"))
            outputs.append(str(output, "utf-8"))

        # write to file
        Path(RESULTS_FOLDER).mkdir(parents=True, exist_ok=True)
        with open(RESULTS_FOLDER + file, "w") as f:
            for output in outputs:
                f.write(output.strip() + "\n")


def main():
    make()
    run_files()


main()