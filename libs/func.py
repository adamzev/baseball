import json
import sys
import os
import re
import glob
from colorama import init, Fore, Back, Style
init()

def is_float(the_string):
    try:
        x = float(the_string)
        return True
    except ValueError:
        return False

def is_int(the_string):
    try:
        x = int(the_string)
        return True
    except ValueError:
        return False

def between_floats(target, lower_bound, upper_bound, precision=3):
    ''' checks if a float is equal to or between two floats
        using rounding to avoid floating point errors
        for example, 8.00000000005 is considered to be between 8.0 and 8.0
        "precision" is how many digits to round all numbers to
    '''
    if round(lower_bound, precision) <= round(target, precision) <= round(upper_bound, precision):
        return True
    return False

def convert_to_numeric_dict(dict_,
    use_float=True,
    non_numeric_zeroes=[""],
    remove=["zipcode", "id"]):
    ''' Changes dict so that all values are floats or ints
        removes text fields from data and converts numeric strings to numbers
        "dict_" is a dict with a mix of numeric and text values
            or numbers listed as strings
        "use_float" is a bool. Uses int if false
        "zero_values" a list of non-numeric zeros. For example, by default, an
            empty string is treated as 0. Something like "-.--" could also be set
            to count as 0
        "remove" are fields to remove (even if they are numeric).
            Typically used to remove labels like ids because it does
            not make sense to do math on labels
    '''
    results = {}
    for key, value in dict_.items():
        # ignore numeric values that are used as labels, not values
        if key in remove:
            continue
        elif use_float and is_float(value):
            results[key] = float(value)
        elif not use_float and is_int(value):
            results[key] = int(value)
        elif value in non_numeric_zeroes:
            if use_float:
                results[key] = 0.0
            else:
                results[key] = 0
    return results

def remove_non_alphanumeric(your_string):
    return re.sub(r'\W+', '', your_string)

def stopPrinting(my_loud_function):
    sys.stdout = open(os.devnull, "w")
    my_loud_function()
    sys.stdout = sys.__stdout__

def printTable(table_data, cols):
    maxWidth = 170
    maxCellWidth = maxWidth / cols
    for row in table_data:
        rowString = "{: >"+str(maxCellWidth)+"}"
        rowString = rowString * len(row)
        print(rowString.format(*row))

def getNextKey(my_dict):
    ''' returns a key from my dict. Use this function to manually loop through a dict or to access the key of a one key dict'''
    return next(iter(my_dict))

def pretty_json(parsed_json):
    print(json.dumps(parsed_json, indent=4, sort_keys=True))

def current(myArray):
    return myArray[-1]


def prev(myArray):
    ''' Gets the previous value if it exists, otherwise returns the current value

    '''
    try:
        return myArray[-2]
    except IndexError:
        return myArray[-1]

def get_value(myArray, when="current"):
    if when == "current":
        return current(myArray)
    else:
        return prev(myArray)


def real_quadradric(a, b, c):
    ''' returns the x values for given a, b, c where ax^2 + bx + c =0
    Only handles quads with real results
    '''
    disc = b**2 - 4 * a * c
    assert disc >= 0

    x1 = (-b + disc**0.5)/(2.0*a)
    x2 = (-b - disc**0.5)/(2.0*a)
    return x1, x2


def break_point():
    ''' Inserts a breakpoint '''
    import pdb; pdb.set_trace()

def almost_equal(x, y, threshold=0.0001):
    ''' returns boolean regarding whether abs(x-y) is within a given threshold '''
    return abs(x-y) < threshold

def weighted_average(values, amounts):
    ''' return the weighted average given values and the frequencies (amounts) of the values '''
    return sum(x * y for x, y in zip(values, amounts)) / sum(amounts)

def linear_estimate(current_time, times, values):
    ''' convert stepwise data into a linear estimate '''
    current_time = round(current_time, 5)
    if len(times) != len(values):
        raise ValueError
    i = 0
    for time in times:
        if current_time <= time:
            break
        i += 1
    else:
        raise ValueError("Current time is greater than last time")
    closest_times = (times[i-1], times[i])
    closest_values = (values[i-1], values[i])
    time_range = closest_times[1] - closest_times[0]
    time_past_prior = current_time - closest_times[0]

    progress = time_past_prior / time_range
    print(time_range, time_past_prior, progress)
    weights = [1 - progress, progress]
    return weighted_average(closest_values, weights)

def less_than_or_almost_equals(a, b, decimal_precision = 5):
    ''' compare floating point values withing a given precision '''
    return round(a, decimal_precision) <= round(b, decimal_precision)
