# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:36:01 2019

@author: hao2d9
"""

#==============================================================================
# Iceberg class definition. 

class Iceberg():    
    def __init__ (self, ice_data, lidar_data_height, ice_no):
        self._total_mass = 0 # kg
        self._total_mass_above_sea = 0 # kg
        self._total_volume = 0 # m3
        self._total_volume_above_sea = 0 # m3
        self._total_area = 0 # m2
        self._total_area_above_sea = 0 # m2
        #self._total_height = 0 # m
        #self._total_height_above_sea = 0 # m
        self.ice_data = ice_data
        self.lidar_data_height = lidar_data_height
        self._ice_no = ice_no
        self._pullable_threshold = 36000000 # kg
        self._berg_pullable = False
        
        self.calc_iceberg_params()
        
    # Set the property of the private variables to use Incapsulation
    ###########################################################################

    @property
    def ice_no(self):
        """Get the 'ice_no' property."""
        return self._ice_no

    @ice_no.setter
    def ice_no(self, value):
        """Set the 'ice_no' property."""
        self._ice_no = round(value, 1)

    @ice_no.deleter
    def ice_no(self):
        """Delete the 'ice_no' property."""
        del self._ice_no    
    
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
        y_len, x_len = self.lidar_data_height.shape
        
        cell_area = 1 # define default cell area = 1 sq.m.
        
        for y in range(y_len):
            for x in range(x_len):
                if self.ice_data[y][x] == self._ice_no:
                    self._total_area += 1
                    self._total_volume += self.lidar_data_height[y][x] / 10 \
                                            * cell_area
                    
                    if self.lidar_data_height[y][x] > 0:
                        self._total_area_above_sea += 1
                        self._total_volume_above_sea += \
                                            self.lidar_data_height[y][x] / 10
                                            
        if (self._total_area_above_sea / self._total_area) * 100 >= 10:
            self._total_mass = 900 * self._total_volume 
        self._total_mass_above_sea = 900 * self._total_volume_above_sea
        
        if self._total_mass < self._pullable_threshold:
            self._berg_pullable = True
        
    def __str__(self):
        return 'Iceberg no: {0}\
                \nTotal area: {1} sq.m.\
                \nTotal area above sea: {2} sq.m.\
                \nTotal volume: {3} m3\
                \nTotal volume above sea: {4} m3\
                \nTotal mass: {5} kg\
                \nTotal mass above sea: {6} kg\
                \nTug {7} pull the berg'\
                .format(self._ice_no, \
                        round(self._total_area,1), \
                        round(self._total_area_above_sea,1),\
                        round(self._total_volume,1), \
                        round(self._total_volume_above_sea,1),\
                        round(self._total_mass,1), \
                        round(self._total_mass_above_sea,1), \
                        ('can' if self._berg_pullable else 'cannot'))
        
# End of Iceberg class definition
#==============================================================================
