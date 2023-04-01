from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        return System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        return System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:  #if there is no hardware the list will stay empty and the [0] index will be invalid
            hardware = [h for h in System._hardware if h.name == hardware_name][0] #create list of h.Check if the h in the list _hardware is with same name
            software = ExpressSoftware(name, capacity_consumption, memory_consumption) #create object of class ExpressSoftware
            hardware.install(software) #after finding hardware with given name we create software of class Express and installed on this hardware
            System._software.append(software)
        except IndexError: #if we don't find any hardware with the given name the created list will be empty and we cant get the el of index 0
            return "Hardware not exist"
        except Exception as ex: #if the capacity and memory of the software is bigger then avaible in the hardware
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0] #[0] to get the element from the list NOT the full list
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError: #if we dont find h with given name and the list is empty
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n"\
               f"Hardware Components: {len(System._hardware)}\n"\
               f"Software Components: {len(System._software)}\n"\
               f"Total Operational Memory: {sum([h.memory_used for h in System._hardware])} / {sum([h.memory for h in System._hardware])}\n"\
               f"Total Capacity Taken: {sum([h.capacity_used for h in System._hardware])} / {sum([h.capacity for h in System._hardware])}"

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            names = ', '.join([s.name for s in h.software_components])
            result += f"Hardware Component - {h.name}\n"\
                      f"Express Software Components: {len([s for s in h.software_components if s.__class__.__name__ == 'ExpressSoftware'])}\n"\
                      f"Light Software Components: {len([s for s in h.software_components if s.__class__.__name__ == 'LightSoftware'])}\n"\
                      f"Memory Usage: {h.memory_used} / {h.memory}\n"\
                      f"Capacity Usage: {h.capacity_used} / {h.capacity}\n"\
                      f"Type: {h.hardware_type}\n"\
                      f"Software Components: {names if names else None}\n"
        return result