from tqdm import tqdm
import matplotlib.pyplot as plt
from random import randint
from enum import Enum


class PrizeType(Enum):
    Car = 1
    Goat = 2



class MontyHallProblem:
    def __init__(self):
        self.door_prize = {}

    def reset(self):
        self.selected_idx = None
        self.opened_idx = None
        self.car_idx = randint(0, 2)
        self.door_prize = {k: PrizeType.Goat for k in range(3)}
        self.door_prize[self.car_idx] = PrizeType.Car

    def select_first(self, idx):
        self.selected_idx = idx

    def open_goat_door(self):
        for k, v in self.door_prize.items():
            if v == PrizeType.Car:
                continue

            if not k == self.selected_idx:
                self.opened_idx = k
                break

    def change_candidate(self):
        self.selected_idx = [i for i in range(3) if not i in (self.selected_idx, self.opened_idx)][0]

    def is_correct(self) -> bool:
        return self.selected_idx == self.car_idx




problem = MontyHallProblem()
result = {"changed": [], "not_changed": []}
iterations = [10**i for i in range(1, 8)]

for iteration in tqdm(iterations):
    result["changed"].append(0)
    result["not_changed"].append(0)
    
    for i in tqdm(range(iteration), leave=False):
        problem.reset()
        problem.select_first(0)
        problem.open_goat_door()
        result["not_changed"][-1] += int(problem.is_correct()) / iteration
    
    
    for i in tqdm(range(iteration), leave=False):
        problem.reset()
        problem.select_first(0)
        problem.open_goat_door()
        problem.change_candidate()
        result["changed"][-1] += int(problem.is_correct()) / iteration
    

plt.plot(result["changed"], color="b", label="changed")
plt.plot(result["not_changed"], color="r", label="not_changed")
plt.show()
