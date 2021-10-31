import sys
from utils import Flags
from models.Plants import Plant
from logger import Logger
from container import Container
from algorithms import MergeSort
import time

INPUT_FILE = ""
OUTPUT_FILE = ""
RANDOM_PLANTS = list()

def generate_plants(amount: int) -> str:
    for i in range(amount):
        RANDOM_PLANTS.append(Plant.generate_plant())

def set_input_file(input_file: str):
    global INPUT_FILE
    INPUT_FILE = input_file

def set_output_file(output_file: str):
    global OUTPUT_FILE
    OUTPUT_FILE = output_file


RANDOM_INPUT_FLAG = Flags.Flag(representation='r', activator=generate_plants)
INPUT_FLAG = Flags.Flag(representation='i', activator=set_input_file)
OUTPUT_FLAG = Flags.Flag(representation='o', activator=set_output_file)

def write_result(output_file: str, container: 'Container.Container', metric: str):
    container.write_file(output_file)
    Logger.log_file(f"{metric} seconds left.", output_file, Logger.LogType.INFO)

def write_to_file(output_file: str, plants: 'typing.List[Plants]'):
    with open(output_file, 'w') as f:
        f.write(str(len(plants))+'\n')
        for plant in plants:
            f.write(plant.get_file_representation()+'\n')

def main(args):
    flags_handler = Flags.FlagHandler([RANDOM_INPUT_FLAG, INPUT_FLAG, OUTPUT_FLAG])
    flags_handler.from_args(args)
    for flag in flags_handler.known_flags:
        print(flag.__repr__())
    flags_handler.handle_all()

    if not INPUT_FLAG.state:
        Logger.log("No input file in parameters!", Logger.LogType.WARNING)
        return

    if not OUTPUT_FLAG.state:
        Logger.log("No output file in parameters!", Logger.LogType.WARNING)
        return

    if RANDOM_INPUT_FLAG.state:
        Logger.log("Random mode ON.", Logger.LogType.INFO)
        write_to_file(INPUT_FILE, RANDOM_PLANTS)

    container = Container.Container.from_file(INPUT_FILE)
    print("Input:")
    for c in range(container.length()):
        print(container[c])
    start_time = time.perf_counter()
    container = Container.Container.from_list(MergeSort.straight_merge(container.c))
    seconds_left = f"{(time.perf_counter() - start_time):0.6f}"
    write_result(OUTPUT_FILE, container, seconds_left)
    print("\nResult:")
    for elem in container:
        print(elem)
    Logger.log(f"{seconds_left} seconds left.", Logger.LogType.INFO)

if __name__=="__main__":
    main(sys.argv)