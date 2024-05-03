#!/usr/bin/python3
""" rain """

def rain(walls):
    if not walls:
        return 0

    size = len(walls)
    result = 0

    for i in range(1, size - 1):
        left_max = max(walls[:i])
        right_max = max(walls[i + 1:])

        water_level = min(left_max, right_max)
        trapped_water = max(0, water_level - walls[i])

        result += trapped_water
    return result
