# Search Algorithms (Binary Search)

## Overview

This Python project implements two search algorithms: Naive Search and Binary Search. These algorithms are designed to find the index of a target element in a given list. Naive Search performs a linear search, while Binary Search is a more efficient algorithm that works on sorted lists.

## Functions

### `naive_search(l, target)`

Performs a linear search on the given list `l` to find the index of the target element. Returns the index if found, otherwise returns -1.

### `binary_search(l, target, low=None, high=None)`

Performs a binary search on the given list `l` to find the index of the target element. The list is assumed to be sorted. Returns the index if found, otherwise returns -1.

## Usage

1. Run the script:

   ```bash
   python your_script_name.py

   Modify the l list and target variable with your desired values.

Uncomment the search algorithm you want to use (navive_search or binary_search) by removing the '#' in front of the respective line.

Run the script to see the result of the search algorithm.

Notes
navive_search performs a linear search, iterating through the list one element at a time.
binary_search is a more efficient algorithm for sorted lists, using a divide-and-conquer approach.
Customization
You can modify the l list and target variable for different test cases.
Experiment with different lists and target values to observe the behavior of each search algorithm.
Credits
[Harsh Chainani]
