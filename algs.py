from libs import project_score
from brute_force import generate_allocations
from parsing import parse_file

def calcolate_best(filename):
    data = parse_file(filename)
    