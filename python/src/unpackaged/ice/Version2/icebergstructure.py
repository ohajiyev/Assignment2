# -*- coding: utf-8 -*-
"""
Date Last Updated: Mar 29, 2019

Author: Orkhan Hajiyev (gy17oh)

Title: Iceberg class

Purpose: 
    Iceberg class contains iceberg characteristics which are calculated
    during the initialisation of the objects
    
License: 
    Copyright (c) 2019 Orkhan Hajiyev
    Lisence under MIT License
    License link: 
        https://github.com/ohajiyev/Assignment2/blob/master/LICENSE.md
       
Python version: 3.7
"""

#==============================================================================
# Iceberg class definition. 

class Iceberg():    
    def __init__ (self, iceberg_data, lidar_data_height, iceberg_no):
        """ Initalize the class """
        self._total_mass = 0 # kg
        self._total_mass_above_sea = 0 # kg
        self._total_volume = 0 # m3
        self._total_volume_above_sea = 0 # m3
        self._total_area = 0 # m2
        self._total_area_above_sea = 0 # m2
        self.iceberg_data = iceberg_data
        self.lidar_data_height = lidar_data_height
        self._iceberg_no = iceberg_no
        self._pullable_threshold = 36000000 # kg
        self._berg_pullable = False
        
        self.calc_iceberg_params()
        
    # Set the property of the private variables to use Incapsulation
    ###########################################################################

    @property
    def berg_pullable(self):
        """Get the 'berg_pullable' property."""
        return self._berg_pullable

    @berg_pullable.setter
    def berg_pullable(self, value):
        """Set the 'berg_pullable' property."""
        self._berg_pullable = round(value, 1)

    @berg_pullable.deleter
    def berg_pullable(self):
        """Delete the 'berg_pullable' property."""
        del self._berg_pullable    
        
    @property
    def iceberg_no(self):
        """Get the 'iceberg_no' property."""
        return self._iceberg_no

    @iceberg_no.setter
    def iceberg_no(self, value):
        """Set the 'iceberg_no' property."""
        self._iceberg_no = round(value, 1)

    @iceberg_no.deleter
    def iceberg_no(self):
        """Delete the 'iceberg_no' property."""
        del self._iceberg_no    
    
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
        Calculate iceberg total area, total volume and total mass both for the 
        whole image area and for the identified above sea
    
        """
        # Get dimensions of the image dataset. In this case y_len and 
        # x_len are both equal to 300
        y_len, x_len = self.lidar_data_height.shape
        
        cell_area = 1 # define default cell area = 1 sq.m.
        
        for y in range(y_len):
            for x in range(x_len):
                # Calculate area and volume only for the current iceberg object 
                if self.iceberg_data[y][x] == self._iceberg_no:
                    self._total_area += 1
                    self._total_volume += self.lidar_data_height[y][x] / 10 \
                                            * cell_area
                    # Calculate above sea area and volume for the current 
                    # iceberg object by checking lidar data > 0
                    if self.lidar_data_height[y][x] > 0:
                        self._total_area_above_sea += 1
                        self._total_volume_above_sea += \
                                  self.lidar_data_height[y][x] / 10 * cell_area
        # Calculate the total mass of the iceberg if 10% of its mass is above
        # sea                                    
        if (self._total_area_above_sea / self._total_area) * 100 >= 10:
            self._total_mass = 900 * self._total_volume 
        # Calculate the total mass of the iceberg above sea
        self._total_mass_above_sea = 900 * self._total_volume_above_sea
        
        # Identify if iceberg pullable or not 
        if self._total_mass < self._pullable_threshold:
            self._berg_pullable = True
        
    def __str__(self):
        """ Overwrite the method to create the string to convert to text """
        return 'Iceberg no: {0}\
                \nTotal area: {1} sq.m.\
                \nTotal area above sea: {2} sq.m.\
                \nTotal volume: {3} m3\
                \nTotal volume above sea: {4} m3\
                \nTotal mass: {5} kg\
                \nTotal mass above sea: {6} kg\
                \nTug {7} pull the berg'\
                .format(self._iceberg_no, \
                        round(self._total_area,1), \
                        round(self._total_area_above_sea,1),\
                        round(self._total_volume,1), \
                        round(self._total_volume_above_sea,1),\
                        round(self._total_mass,1), \
                        round(self._total_mass_above_sea,1), \
                        ('can' if self._berg_pullable else 'cannot'))
        
# End of Iceberg class definition
#==============================================================================
