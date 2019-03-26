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
#%matplotlib qt

# End of Import modules
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

# End of Function definitions
#==============================================================================

#==============================================================================
# Iceberg class definition. 

class Iceberg():    
    def __init__ (self, radar_data_texture, lidar_data_height):
        self._total_mass = 0
        self._total_mass_above_sea = 0
        self._total_volume = 0
        self._total_volume_above_sea = 0
        self._total_area = 0
        self._total_area_above_sea = 0
        self._total_height = 0
        self._total_height_above_sea = 0
        self.radar_data_texture = radar_data_texture
        self.lidar_data_height = lidar_data_height
        
        self.calc_ice()
        
    # Set the proprty of the private variables to use Incapsulation
    @property
    def total_mass(self):
        """Get the 'total_mass' property."""
        return self._total_mass

    @total_mass.setter
    def total_mass(self, value):
        """Set the 'total_mass' property."""
        self._total_mass = value

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
        self._total_mass_above_sea = value

    @total_mass_above_sea.deleter
    def total_mass_above_sea(self):
        """Delete the 'total_mass_above_sea' property."""
        del self._total_mass_above_sea 
        
    @property
    def total_volume(self):
        """Get the 'total_volume' property."""
        return self._total_volume

    @total_mass_above_sea.setter
    def total_volume(self, value):
        """Set the 'total_volume' property."""
        self._total_volume = value

    @total_mass_above_sea.deleter
    def total_volume(self):
        """Delete the 'total_volume' property."""
        del self._total_volume 
        
        
    def calc_ice(self):
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
        
    def __str__(self):
        return 'Total area: {0} sq.m.\
                \nTotal area above sea: {1} sq.m.\
                \nTotal volume: {2} m3\
                \nTotal volume above sea: {3} m3\
                \nTotal mass: {4} kg\
                \nTotal mass above sea: {5} kg'\
                .format(self._total_area, \
                        self._total_area_above_sea,\
                        self._total_volume, \
                        self._total_volume_above_sea,\
                        self._total_mass, \
                        self._total_mass_above_sea)
        
# End of Iceberg class definition
#==============================================================================


#==============================================================================
# Create variables. 

radar_data_texture = [] # empty list of data which contains texture of objects
                         # read from radar file   
lidar_data_height = [] # empty list of data which contains height of objects
                        # read from lidar file 
icebergs = [] # empty list of Iceberg objects

# Define input file paths for single bergs
lidar_data_file_name = 'input/white1.lidar'
radar_data_file_name = 'input/white1.radar'

# Define input file paths for multiple bergs
#lidar_data_file_name = 'input/white2.lidar'
#radar_data_file_name = 'input/white2.radar'

# End of Create variables
#==============================================================================

read_file(lidar_data_file_name, lidar_data_height)
read_file(radar_data_file_name, radar_data_texture)
    
draw_environment(radar_data_texture)
draw_environment(lidar_data_height)

icebergs.append(Iceberg(radar_data_texture, lidar_data_height))

print(icebergs[0])
#calc_ice(radar_data_texture, lidar_data_height)