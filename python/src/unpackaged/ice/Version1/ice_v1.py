# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:37:13 2019

@author: Orkhan Hajiyev (gy17oh)

!!! Important note: some part of the code may be copied and modified from 
!!! https://docs.python.org/3/ as a reference

The purpuse of the script is to implement the requirements of the 
Assignment 2 of the Module GEOG5991M.

White Star Line was selected as the project to satisfy the assignment's
description. The link to the project's problem definition:
    https://www.geog.leeds.ac.uk/courses/computing/
    study/core-python-odl/assessment2/ice.html

"""

#==============================================================================
# Import modules

import sys
import operator
import matplotlib.pyplot
import matplotlib.animation
import csv

# End of Import modules
#==============================================================================


#==============================================================================
# Function definitions

# Function to 
def draw_environment(environment):
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment)
#    for i in range(num_of_agents):
#        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.show()
    
    
# Check, try and read the input files
try:
    with open(lidar_data_file_name, 'r') as lidar_file:
        # Read input file values and assign into environment variable
        for data_row in lidar_file:
            row_list = []
            for single_value in data_row.split(","):
                row_list.append(int(single_value))
            environment_texture.append(row_list)
except IOError as err:
    print(err)
except:
    print("Unexpected error:", sys.exc_info()[0])

# End of Function definitions
#==============================================================================


#==============================================================================
# Create variables

environment_texture = [] # empty list of data which contains texture of objects
environment_height = [] # empty list of data which contains height of objects 
icebergs = [] # empty list of Iceberg objects

# Define input file paths for single bergs
lidar_data_file_name = 'input/white1.lidar'
radar_data_file_name = 'input/white1.radar'

# Define input file paths for multiple bergs
#lidar_data_file_name = 'input/white2.lidar'
#radar_data_file_name = 'input/white2.radar'

# End of Create variables
#==============================================================================


# Check, try and read the input files
try:
    with open(lidar_data_file_name, 'r') as lidar_file:
        # Read input file values and assign into environment variable
        for data_row in lidar_file:
            row_list = []
            for single_value in data_row.split(","):
                row_list.append(int(single_value))
            environment_texture.append(row_list)
except IOError as err:
    print(err)
except:
    print("Unexpected error:", sys.exc_info()[0])
    
try:
    with open(radar_data_file_name, 'r') as radar_file:
        # Read input file values and assign into environment variable
        for data_row in radar_file:
            row_list = []
            for single_value in data_row.split(","):
                row_list.append(int(single_value))
            environment_height.append(row_list)
except IOError as err:
    print(err)
except:
    print("Unexpected error:", sys.exc_info()[0])
    
draw_environment(environment_texture)
draw_environment(environment_height)