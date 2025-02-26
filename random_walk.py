import random

import matplotlib.pyplot as plt

plt.switch_backend('TkAgg')
import numpy as np

import pandas as pd


def get_coordinates_data(dims, steps):
    return [[0] * (steps + 1) for _ in range(0, dims)]


def random_walk(coordinates_data):
    for step in range(1, len(coordinates_data[0])):
        for dim in range(len(coordinates_data)):
            coordinates_data[dim][step] = coordinates_data[dim][step - 1]
        current_dim = random.randint(0, len(coordinates_data) - 1)
        current_step = random.choice([1, -1])
        coordinates_data[current_dim][step] += current_step


def display_walk_data(coordinates_data):
    if len(coordinates_data) == 1:
        plt.plot(coordinates_data[0])
    if len(coordinates_data) == 2:
        plt.plot(coordinates_data[0], coordinates_data[1])
    if len(coordinates_data) == 3:
        x = plt.axes(projection="3d")
        x.plot([coordinates_data[0]], [coordinates_data[1]], [coordinates_data[2]])
    elif len(coordinates_data) >= 4:
        data = {f' dimensions {i + 1}': coordinates_data[i] for i in range(len(coordinates_data))
                }
        df = pd.DataFrame(data)
        print(df)
    plt.show()


while True:
    try:
        dims_input = input(str("input a integer number for dimensions to walk "))
        assert dims_input.isdigit() and int(dims_input) > 0
        dims = int(dims_input)
        break
    except AssertionError:
        print("invalid input, please enter a positive integer.")
        print()
        continue

while True:
    try:
        steps_input = input(str("input a integer number for steps to walk "))
        assert steps_input.isdigit() and int(steps_input) > 0
        steps = int(steps_input)
        break
    except AssertionError:
        print("invalid input, please enter a positive integer.")
        print()
        continue

coordinates_data = get_coordinates_data(dims, steps)
random_walk(coordinates_data)
display_walk_data(coordinates_data)
