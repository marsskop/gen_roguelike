import numpy as np


"""
Default map arrays.
"""

def empty(shape):
    grid = np.zeros(shape)

    return grid


def square(shape, sqside):
    grid = np.zeros(shape)
    height = shape[0]
    width = shape[1]
    
    topcrn = (int(height/2 - sqside/2), int(width/2 - sqside/2))
    botcrn = (int(height/2 + sqside/2), int(width/2 + sqside/2))

    for i in range(sqside + 1):
        for j in range(sqside + 1):
            grid[topcrn[0]+j, topcrn[1]+i] = 1

    return grid