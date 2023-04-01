from typing import List
from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    @property
    def available_capacity(self):
        return self.capacity - self.capacity_used

    @property
    def available_memory(self):
        return self.memory - self.memory_used

    @property
    def capacity_used(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def memory_used(self):
        return sum([s.memory_consumption for s in self.software_components])


    def install(self, software:Software):
        if software.memory_consumption <= self.available_memory and software.capacity_consumption <= self.available_capacity:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)



