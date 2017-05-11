#!/usr/bin/env python

import numpy as np

def load_data():    
    # Goalkeeper, defender, midfielder, attacker
    possible_positions = ['GK', 'D', 'M', 'A']
    N = 100
    positions = []
    heights = []
    for i in range(0,N):
        positions.append(possible_positions[np.random.randint(len(possible_positions))])
        heights.append(np.random.normal(loc=180.0,scale=5.0))
    return positions, heights

positions, heights = load_data()

np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers.
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players.
print("Median height of other players: " + str(np.median(other_heights)))

if(np.median(gk_heights) > np.median(other_heights)):
    print("The median goalkeepers height is bigger than that of the other players")
else:
    print("The median goalkeepers height is not bigger than that of the other players")
