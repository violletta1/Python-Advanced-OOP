from typing import List


from project import Worker
from project.animal import Animal


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"



    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)

        return f"{worker_name} fired successfully"
        # if worker_name in self.workers:
        #     self.workers.remove(worker_name)
        #     return f"{worker_name} fired successfully"
        # return "There is no {worker_name} in the zoo"


    def pay_workers(self):
        salaries = sum(w.salary for w in self.workers)
        if salaries < self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"



    def tend_animals(self):
        animals_care = sum(a.money_for_care for a in self.animals)
        if animals_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animals_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"



    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:",
        ]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(str(x) for x in result)
        # lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        # tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        # cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]
        #
        # total_animals_count = len(self.animals)
        # amount_of_lions = len(lions)
        # amount_of_tigers = len(tigers)
        # amount_of_cheetahs = len(cheetahs)
        # lion_str = "\n".join([f"{lion}" for lion in lions])
        # tiger_str = "\n".join([f"{tiger}" for tiger in tigers])
        # cheetah_str = "\n".join([f"{cheetah}" for cheetah in cheetahs])
        # return f"You have {total_animals_count} animals" \
        #        f"----- {amount_of_lions} Lions:" \
        #        f"{lion_str}" \
        #        f"----- {amount_of_tigers} Tigers:" \
        #        f"{tiger_str}" \
        #        f"----- {amount_of_cheetahs} Cheetahs:" \
        #        f"{cheetah_str}"


    def workers_status(self):
        info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info['Keeper'],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info['Caretaker'],
            f"----- {len(info['Vet'])} Vets:",
            *info['Vet'],
        ]

        return "\n".join(result)

        # keepers = [w for w in self.workers if isinstance(worker, Keeper)]
        # caretakers = [c for c in self.workers if isinstance(worker, Caretaker)]
        # vets = [v for v in self.workers if isinstance(worker, Vet)]
        #
        # total_workers_count = len(self.workers)
        # amount_of_keepers = len(keepers)
        # amount_of_caretakers = len(caretakers)
        # amount_of_vets = len(vets)
        #
        # keepers_str = "\n".join([f"{keeper}" for keeper in keepers])
        # caretakers_str = "\n".join([f"{caretaker}" for caretaker in caretakers])
        # vets_str = "\n".join([f"{vet}" for vet in vets])
        # return f"You have {total_workers_count} workers"\
        #        f"----- {amount_of_keepers} Keepers:"\
        #        f"{keepers_str}"\
        #        f"----- {amount_of_caretakers} Caretakers:" \
        #        f"{caretakers_str}" \
        #        f"----- {amount_of_vets} Vets:" \
        #        f"{vets_str}"








