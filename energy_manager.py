#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 23:23:02 2023

@author: takayuki
"""

import pandas as pd
import datetime

print("Libraries import done.")


class CleanEnergyProducer:
    def __init__(self, clean_name, yield_power):
        self.name = clean_name
        self.yield_power = yield_power
    
    def yield_power():
        yield_power = df["pv_yield_power"]


class Consumer:
    def __init__(self, consumer_name, demand):
        self.name = consumer_name
        self.demand = demand
        
    def demand():
        demand = df["household_consumption"]
        


class Storage:
    def __init__(self, storage_name, capacity):
        self.name = storage_name
        self.capacity = capacity
        
class LegacyEnergyProducer:
    def __init__(self, legacy_name, yield_power):
        self.name = legacy_name
        self.yield_power = yield_power

class ConfiguredSystem():
    # def __init__(self, clean_energy_producers, consumer, storage):
        
    def decide_component():
        
        # When the supply of clean energy is larger than demand, always use clean energy.
        if CleanEnergyProducer.yield_power > Consumer.demand:
            chosen_component = CleanEnergyProducer
            
        # When there is still power left in storage, use storage. It always keeps a little amount in case for emergency.
        elif storage.power > 5000.0:
            chosen_component = Storage
        
        else:
            chosen_component = LegacyEnergyProducer
        
        return chosen_component
    pass

# Create CleanEnergyProducer instances
solar_power = CleanEnergyProducer("Solar power", 1000)
wind_power = CleanEnergyProducer("Wind power", 700)
geothermal_power = CleanEnergyProducer("Geothermal power", 500)

# Create Consumer instances
house_hold = Consumer("House hold", 1000)
office = Consumer("Office", 2000)
factory = Consumer("Factory", 3000)

# Create Storage instances
battery = Storage("Battery", 3000)
hydrogen_tank = Storage("Hydrogen tank", 5000)

# Create LegacyEnergyProducer instances
grid = LegacyEnergyProducer("grid", 800)

# Example of a configured system
example_system = ConfiguredSystem(solar_power, house_hold, battery, grid)


clean_energy_producers = [solar_power, wind_power, geothermal_power]
consumers = [house_hold, office, factory]
storage = [battery, hydrogen_tank]


def choose_component(clean_energy_producers, consumers, storages):
    """
        Let an user to choose a combination of components from the options provided.


    Parameters
    ----------
    clean_energy_producers : LIST

    consumers : LIST

    storage : LIST

    Returns
    -------
    None.

    """

    # Choose clean energy component
    clean_energy_input = ""
    input_message = f"Choose an option for the clean energy producer:\n"

    for index, item in enumerate(clean_energy_producers):
        input_message += f'{index+1}) {item.name}\n'
        
    input_message += f"Your choice for the clean energy producer:"

    while clean_energy_input not in map(str, range(1, len(clean_energy_producers) + 1)):
        clean_energy_input = input(input_message)

    # print('You picked: ' + option_list[int(user_input) - 1])

    # Choose consumer component
    consumer_input = ""
    input_message = f"Choose an option for the consumer:\n"

    for index, item in enumerate(consumers):
        input_message += f'{index+1}) {item.name}\n'

    input_message += f"Your choice for the consumer:"

    while consumer_input not in map(str, range(1, len(consumers) + 1)):
        consumer_input = input(input_message)

    # Choose storage component
    storage_input = ""
    input_message = f"Choose an option for the storage:\n"

    for index, item in enumerate(storages):
        input_message += f'{index+1}) {item.name}\n'

    input_message += f"Your choice for the storages:"

    while storage_input not in map(str, range(1, len(storages) + 1)):
        storage_input = input(input_message)
        
    print(
        f"Your energy components are: {clean_energy_producers[int(clean_energy_input) - 1].name}, {consumers[int(consumer_input) - 1].name}, {storages[int(storage_input) - 1].name}")

    return clean_energy_input, consumer_input, storage_input


# load dummy dataset
df = pd.read_csv("profiles_dataset_updated.csv")

# Current implementation is loading dummy dataset at once and provide decision for time stamps which is already provided.
# Future plan: Deploy on AWS lambda and set schedule ot run it every 5 min so that the decison is up to date.

def decide_component():
    
    for ind in df.index:
        
        print(df['timestamp'][ind])
        
        
        # When the supply of clean energy is larger than demand, always use clean energy.
        if df["pv_yield_power"][ind] > df["household_consumption"][ind]:
            
            df["log"][ind] = "clean energy"
            chosen_component = CleanEnergyProducer
                     
            
        # When there is still power left in storage, use storage. It always keeps a little amount in case for emergency.
        elif df["battery_power"][ind] > 5000.0:
            
            df["log"][ind] = "battery"
            chosen_component = Storage
        
        else:
            df["log"][ind] = "grid"
            chosen_component = LegacyEnergyProducer
        
        return chosen_component




def main():
    print("I'm an energy manager!\n Choose a component of clean energy producers, consumers, storages.")

    choose_component(clean_energy_producers, consumers, storage)



if __name__ == "__main__":
    main()
