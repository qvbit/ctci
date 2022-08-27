import random
from typing import Tuple


def run_n_families(n: int) -> float:
    boys = 0
    girls = 0
    for i in range(n):
        genders = run_one_family()
        boys += genders[0]
        girls += genders[1]
    
    return girls / (boys + girls)  # return the probability of a girl
    

def run_one_family() -> Tuple[int, int]:
    boys = 0
    girls = 0
    while girls == 0:
        if random.choice([True, False]):  # If girl
            girls += 1
        else:  # Else boy
            boys += 1
    
    return (boys, girls)


if __name__ == "__main__":
    print(run_n_families(10000))  # Should be close to 0.5
