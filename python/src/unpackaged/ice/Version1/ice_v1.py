# -*- coding: utf-8 -*-
"""

Title: Assignment 2. Module GEOG5991M
       White Star Line Project

Version: 1.0
The version was built to analysis SINGLE iceberg images 
       
Link to Github: https://github.com/ohajiyev/Assignment2
    
Last updated on Mar 26, 2019

@author: Orkhan Hajiyev (gy17oh)

Python version: 3.7 (Python 3.7.1 64-bit | Qt 5.9.6 | PyQt5 5.9.2 | Windows 10)

The code is written in Spyder Version 3.3.2

!!! Important note: some part of the code may be copied and modified from 
!!! https://docs.python.org/3/ as a reference

The purpuse of the script is to implement the requirements of the 
Assignment 2 of the Module GEOG5991M.

White Star Line was selected as the project to satisfy the assignment's
description. The link to the project's problem definition:
    https://www.geog.leeds.ac.uk/courses/computing/
    study/core-python-odl/assessment2/ice.html
    
Copyright (c) 2019 Orkhan Hajiyev
Lisence under MIT License
License link: https://github.com/ohajiyev/Assignment2/blob/master/LICENSE.md

"""

#==============================================================================
# Import modules

import sys
import operator
import matplotlib.pyplot
import matplotlib.animation
import csv
#%matplotlib qt

# End of Import modules
#==============================================================================


#==============================================================================
# Iceberg class definition. 

class Iceberg():    
    def __init__ (self, radar_data_texture, lidar_data_height):
        self._total_mass = 0 # kg
        self._total_mass_above_sea = 0 # kg
        self._total_volume = 0 # m3
        self._total_volume_above_sea = 0 # m3
        self._total_area = 0 # m2
        self._total_area_above_sea = 0 # m2
#        self._total_height = 0 # m
#        self._total_height_above_sea = 0 # m
        self.radar_data_texture = radar_data_texture
        self.lidar_data_height = lidar_data_height
        self._pullable_threshold = 36000000 # kg
        self._berg_pullable = False
        
        self.calc_iceberg_params()
        
    # Set the property of the private variables to use Incapsulation
    ###########################################################################
    
    @property
    def total_mass(self):
        """Get the 'total_mass' property."""
        return self._total_mass

    @total_mass.setter
    def total_mass(self, value):
        """Set the 'total_mass' property."""
        self._total_mass = round(value, 1)

    @total_mass.deleter
    def total_mass(self):
        """Delete the 'total_mass' property."""
        del self._total_mass    

    @property
    def total_mass_above_sea(self):
        """Get the 'total_mass_above_sea' property."""
        return self._total_mass_above_sea

    @total_mass_above_sea.setter
    def total_mass_above_sea(self, value):
        """Set the 'total_mass_above_sea' property."""
        self._total_mass_above_sea = round(value, 1)

    @total_mass_above_sea.deleter
    def total_mass_above_sea(self):
        """Delete the 'total_mass_above_sea' property."""
        del self._total_mass_above_sea 
        
    @property
    def total_volume(self):
        """Get the 'total_volume' property."""
        return self._total_volume

    @total_volume.setter
    def total_volume(self, value):
        """Set the 'total_volume' property."""
        self._total_volume = round(value, 1)

    @total_volume.deleter
    def total_volume(self):
        """Delete the 'total_volume' property."""
        del self._total_volume 
        
    @property
    def total_volume_above_sea(self):
        """Get the 'total_volume_above_sea' property."""
        return self._total_volume_above_sea

    @total_volume.setter
    def total_volume_above_sea(self, value):
        """Set the 'total_volume_above_sea' property."""
        self._total_volume_above_sea = round(value, 1)

    @total_volume.deleter
    def total_volume_above_sea(self):
        """Delete the 'total_volume_above_sea' property."""
        del self._total_volume_above_sea 
 
    @property
    def total_area(self):
        """Get the 'total_area' property."""
        return self._total_area

    @total_area.setter
    def total_area(self, value):
        """Set the 'total_area' property."""
        self._total_area = round(value, 1)

    @total_area.deleter
    def total_area(self):
        """Delete the 'total_area' property."""
        del self._total_area 
        
    @property
    def total_area_above_sea(self):
        """Get the 'total_area_above_sea' property."""
        return self._total_area_above_sea

    @total_area.setter
    def total_area_above_sea(self, value):
        """Set the 'total_area_above_sea' property."""
        self._total_area_above_sea = round(value, 1)

    @total_area.deleter
    def total_area_above_sea(self):
        """Delete the 'total_area_above_sea' property."""
        del self._total_area_above_sea
    
    # End of property
    ###########################################################################
        
    def calc_iceberg_params(self):
        """
        Calculate the total mass above sea, tha volume of the iceberg
    
        """
        cell_area = 1 # 
        for y in range(299):
            for x in range(299):
                if self.radar_data_texture[x][y] >= 100:
                    self._total_area += 1
                    self._total_volume += self.lidar_data_height[x][y] / 10 \
                                            * cell_area
                    
                    if self.lidar_data_height[x][y] > 0:
                        self._total_area_above_sea += 1
                        self._total_volume_above_sea += \
                                            self.lidar_data_height[x][y] / 10
                                            
        if (self._total_area_above_sea / self._total_area) * 100 >= 10:
            self._total_mass = 900 * self._total_volume 
        self._total_mass_above_sea = 900 * self._total_volume_above_sea
        
        if self._total_mass < self._pullable_threshold:
            self._berg_pullable = True
        
    def __str__(self):
        return 'Total area: {0} sq.m.\
                \nTotal area above sea: {1} sq.m.\
                \nTotal volume: {2} m3\
                \nTotal volume above sea: {3} m3\
                \nTotal mass: {4} kg\
                \nTotal mass above sea: {5} kg\
                \nTug {6} pull the berg'\
                .format(round(self._total_area,1), \
                        round(self._total_area_above_sea,1),\
                        round(self._total_volume,1), \
                        round(self._total_volume_above_sea,1),\
                        round(self._total_mass,1), \
                        round(self._total_mass_above_sea,1), \
                        ('can' if self._berg_pullable else 'cannot'))
        
# End of Iceberg class definition
#==============================================================================


#==============================================================================
# Function definitions

def draw_environment(environment):
    """
    Draw environment

    Arguments:
    environment -- list variable contains the data of iceberg environment
                   (no default)

    Returns:
    Plot of environment variable.
    """
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.show()
    

    
def read_file(file_name, environment):    
    # Check, try and read the input files
    try:
        with open(file_name, 'r') as file_object:
            # Read input file values and assign into environment variable
            for data_row in file_object:
                row_list = []
                for single_value in data_row.split(","):
                    row_list.append(int(single_value))
                environment.append(row_list)       
    except IOError as err:
        print(err)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        
def write_file(file_name, result_text):    
    # Check, try and write result to the output file
    try:
        with open(file_name, 'w') as file_object:
            file_object.write(result_text)      
    except IOError as err:
        print(err)
    except:
        print("Unexpected error:", sys.exc_info()[0])

# End of Function definitions
#==============================================================================


#==============================================================================
# Create variables. 

radar_data_texture = [] # empty list of data which contains texture of objects
                         # read from radar file   
lidar_data_height = [] # empty list of data which contains height of objects
                        # read from lidar file 
icebergs = [] # empty list of Iceberg objects

# Define input file paths for single bergs
lidar_data_file_path = 'input/white1.lidar'
radar_data_file_path = 'input/white1.radar'

# Define input file paths for multiple bergs
#lidar_data_file_path = 'input/white2.lidar'
#radar_data_file_path = 'input/white2.radar'

# Define output file path
output_file_path = 'output/results.txt'

# End of Create variables
#==============================================================================

read_file(lidar_data_file_path, lidar_data_height)
read_file(radar_data_file_path, radar_data_texture)
    
draw_environment(radar_data_texture)
draw_environment(lidar_data_height)

icebergs.append(Iceberg(radar_data_texture, lidar_data_height))

print(icebergs[0])

write_file(output_file_path, str(icebergs[0]))

#calc_ice(radar_data_texture, lidar_data_height)