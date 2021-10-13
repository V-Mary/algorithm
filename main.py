import math
from selection_sort import *

sum_hours = 0


def check_speed(array, possible_speed, time, sum_hours):

    for i in array:
        hours_for_pile = math.ceil(i / possible_speed)
        sum_hours = sum_hours + hours_for_pile

    if sum_hours == time:
        return print("Speed = ",possible_speed)
    elif sum_hours > time:
        while sum_hours > time:
            possible_speed = possible_speed + 1
            sum_hours = 0
            for i in array:
                hours_for_pile = math.ceil(i / possible_speed)
                sum_hours = sum_hours + hours_for_pile
        return print("Speed = ",possible_speed)
    else:
        while sum_hours > time:
            possible_speed = possible_speed - 1
            sum_hours = 0
            for i in array:
                hours_for_pile = math.ceil(i / possible_speed)
                sum_hours = sum_hours + hours_for_pile
        return print("Speed = ",possible_speed)


def find_speed(array, time):

    array = selection_sort(array)

    diference = time - len(array)

    if diference == 0:
        speed = array[-1]
        return print(speed)

    elif diference < 0:
        return print("Not enough time!")

    else:
        if (-1 - diference) <= - len(array):
            possible_speed = array[0]
        else:
            possible_speed = array[-1 - diference]

        check_speed(array,possible_speed,time, 0)


piles = [30,11,23,4,20]

find_speed(piles, 6)

