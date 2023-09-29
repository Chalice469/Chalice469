#!/usr/bin/env py
import pyautogui as pg

def move(coordinates, time, rest, comment):
    """ this function take composes a line of the program's code
    pair = 100, 100
    >>> move(pair, ".5", "1", "line 1 is for declaring the funtion name)
    moveTo(100,100, duration =.5); sleep(1) #line 1 is for declaring the funtion name:
    """
    x, y = coordinates
    return "moveTo({}, {}, duration ={}); sleep({}) #{};".format(x, y, time, rest, comment)


