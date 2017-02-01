#!/usr/bin/env python
import numpy as np

def load_data():    
    # Load the data from a source. In this case hard-coded. Dataset corresponds to soccer players' position and height.
    positions = ['GK', 'M', 'A', 'D', 'M', 'D', 'M', 'M', 'M', 'A', 'M', 'M', 'A', 'A', 'A', 'M', 'D', 'A', 'D', 'M', 'GK', 'D', 'D', 'M', 'M', 'M', 'M', 'D', 'M', 'GK', 'D', 'GK', 'D', 'D', 'M', 'A', 'M', 'D', 'M', 'GK', 'M', 'GK', 'A', 'D', 'GK', 'A', 'GK', 'GK', 'GK', 'GK', 'A', 'D', 'A', 'D', 'D', 'M', 'D', 'M', 'D', 'D', 'GK', 'GK', 'D', 'M', 'M', 'GK', 'M', 'D', 'M', 'M', 'D', 'D', 'M', 'M', 'D', 'A', 'A', 'M', 'M', 'M', 'A', 'D', 'D', 'A', 'A', 'M', 'M', 'M', 'D', 'D', 'A', 'A', 'D', 'M', 'M', 'M', 'D', 'M', 'M', 'D', 'M', 'A', 'M', 'M', 'GK', 'M', 'D', 'M', 'M', 'D', 'M', 'M', 'A', 'GK', 'D', 'M', 'GK', 'M', 'M', 'M', 'M', 'D', 'D', 'M', 'D', 'M', 'D', 'M', 'M', 'A', 'M', 'GK', 'A', 'M', 'D', 'M', 'D', 'GK', 'D', 'D', 'M', 'A', 'GK', 'M', 'D', 'A', 'D', 'A', 'A', 'M', 'D', 'M', 'A', 'GK', 'D', 'M', 'GK', 'A', 'D', 'D', 'D', 'GK', 'GK', 'M', 'D', 'GK', 'D', 'M', 'GK', 'A', 'D', 'GK', 'GK', 'D', 'M', 'GK', 'D', 'D', 'D', 'M', 'D', 'M', 'D', 'D', 'A', 'D', 'D', 'D', 'M', 'M', 'A', 'D', 'M', 'M', 'D', 'M', 'A', 'A', 'D', 'A', 'GK', 'M', 'A', 'A', 'D', 'D', 'A', 'D', 'GK', 'D', 'M', 'D', 'D', 'M', 'M', 'GK', 'D', 'M', 'GK', 'GK', 'D', 'M', 'D', 'D', 'M', 'A', 'D', 'D', 'M', 'A', 'A', 'A']

    heights = [191, 184, 185, 180, 181, 187, 170, 179, 183, 186, 185, 170, 187, 183, 173, 188, 183, 180, 188, 175, 193, 180, 185, 170, 183, 173, 185, 185, 168, 190, 178, 185, 185, 193, 183, 184, 178, 180, 177, 188, 177, 187, 186, 183, 189, 179, 196, 190, 189, 188, 188, 188, 182, 185, 184, 178, 185, 193, 188, 179, 189, 188, 180, 178, 186, 188, 180, 185, 172, 179, 180, 174, 183, 178, 187, 178, 193, 181, 180, 187, 179, 173, 175, 188, 187, 175, 171, 179, 180, 188, 185, 196, 183, 184, 186, 178, 188, 168, 176, 178, 178, 192, 172, 170, 190, 175, 174, 179, 177, 187, 184, 185, 175, 193, 185, 191, 181, 183, 176, 176, 182, 192, 187, 170, 189, 171, 181, 183, 178, 182, 186, 191, 175, 179, 180, 181, 178, 193, 179, 181, 186, 190, 190, 192, 185, 178, 182, 171, 182, 173, 192, 175, 183, 183, 184, 176, 183, 186, 178, 185, 188, 193, 193, 170, 188, 196, 175, 180, 184, 173, 180, 190, 186, 182, 183, 195, 188, 187, 190, 180, 194, 182, 182, 183, 178, 183, 171, 185, 177, 180, 195, 173, 185, 186, 187, 178, 185, 174, 175, 176, 191, 170, 183, 180, 174, 191, 179, 178, 187, 191, 183, 180, 184, 183, 180, 185, 184, 181, 186, 185, 182, 175, 173, 175, 176, 174, 184, 177, 185, 162, 180, 171]
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
