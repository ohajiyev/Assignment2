# -*- coding: utf-8 -*-
"""

Title: Assignment 2. Module GEOG5991M
       White Star Line Project

Version: 2.0
The version was built to analyse MULTIPLE iceberg images 
       
Link to Github: https://github.com/ohajiyev/Assignment2
    
Last updated on Mar 27, 2019

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
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.patches as mpatches
import numpy as np
import icebergstructure
#%matplotlib qt

# End of Import modules
#==============================================================================


#==============================================================================
# Function definitions

def on_hover(event, icebergs, ice_data, ax_result, ice_count):
    if event.inaxes is not None:
        if event.inaxes.title.get_text() == 'Analysed Icebergs':
            ice_data_value = ice_data[int(round(event.ydata))][
                    int(round(event.xdata))]
            if ice_data_value in range (1, ice_count+1):
                ax_result.clear()
                text_result = 'Results of image analysis of berg'
                text_result += '\nHover over the icebergs to view characteristics'
                ax_result.text(0, 115, text_result, 
                             bbox={'facecolor': 'white', 'pad': 5})
                ax_result.text(0, 285, str(icebergs[ice_data_value-1]), 
                             bbox={'facecolor': 'white', 'pad': 5})
                ax_result.axis('off')
                plt.gcf().canvas.draw_idle()
    
def draw_result_multiple(ice_data, icebergs, \
                         radar_data_texture, lidar_data_height):
                    
    #!!!!!!!! The following resources were used in the creation of the method 
    # https://stackoverflow.com/questions/25482876/how-to-add-legend-to-imshow-
    # in-matplotlib
    # https://stackoverflow.com/questions/9707676/defining-a-discrete-colormap-
    # for-imshow-in-matplotlib/9708079
    
    # Create a copy of ice_data to modify it and assign values 1 and 2.
    # 1 means that the berg is pullable and 2 is not pullable
    ice_data_pullable = np.copy(ice_data)
    
    # Create the variable with 0, 1 and 2. 0 refer to the sea level, 1 to 
    # the pullable iceberg and 2 to the iceberg which cannot be pulled
    for berg in icebergs:
        ice_data_slice_temp = np.where(ice_data == berg.ice_no)
        if berg.berg_pullable:
            ice_data_pullable[ice_data_slice_temp] = 1
        else:
            ice_data_pullable[ice_data_slice_temp] = 2
            
    # Get the unique values from data. In this case it will be 0, 1 nad 2
    values = np.unique(ice_data_pullable.ravel())
    
    # Create the dictionary of unique values           
    value_description = {0: 'Sea level', 1: 'Iceberg pullable', \
                         2: 'Iceberg not pullable',}
    
    # Create two plot area, one for image visualisation and the second will
    # be used for showing the result text
    fig, ax = plt.subplots(2, 2, figsize=(8,8), sharey=True)
    
    ax[0, 0].imshow(radar_data_texture)
    ax[0, 0].set_title('Input Radar Image')
    ax[0, 1].imshow(lidar_data_height)
    ax[0, 1].set_title('Input Lidar Image')
        
    # Make a color map of fixed colors, blue for the sea and grey for 
    # the iceberg
    cmap = colors.ListedColormap(['blue', 'green', 'red'])
    bounds=[0,0.5,1,1.5,2]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    # Plot image with predefined colors
    im = ax[1, 0].imshow(ice_data_pullable, interpolation='none', cmap=cmap, \
           norm=norm)
    
    # Identify the colors from the plot. In this case it is blue, gren and red
    colors_image = [ im.cmap(im.norm(value)) for value in values]
    
    # Create a patch for every color 
    patches = [mpatches.Patch(color=colors_image[i], label="{}".
                    format(value_description[i]) ) for i in range(len(values))]
    
    # Put those patched as legend-handles into the legend
    ax[1, 0].legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, 
      borderaxespad=0.)
    
    ax[1, 0].set_title('Analysed Icebergs')
    
    text_result = 'Results of image analysis of berg'
    text_result += '\nHover over the icebergs to view characteristics'
    
    ax[1, 1].text(0, 115, text_result, bbox={'facecolor': 'white', 'pad': 5})
    
    ax[1, 1].text(0, 285, str(icebergs[0]), bbox={'facecolor': 'white', 
      'pad': 5})
    
    ax[1, 1].axis('off')
    
    ice_count = len(icebergs)
    
    plt.show()
    
    cid = fig.canvas.mpl_connect('motion_notify_event', lambda event: 
        on_hover(event, icebergs, ice_data, ax[1, 1], ice_count))
    
    plt.show()
    
def read_file(file_name):    
    # Try to read the input files
    # Note: assigning new value to environment variable make it local,
    # so return function was used
    try:
        environment = np.loadtxt(file_name, delimiter = (','))
        return environment     
    except IOError as err:
        print(err)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        
def write_file(file_name, icebergs):    
    # Try to write the result to the output file
    try:
        with open(file_name, 'w') as file_object:
            file_object.write('Results of analysis\n\n') 
            for berg in icebergs:
                file_object.write(str(berg))   
                file_object.write('\n\n')
    except IOError as err:
        print(err)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        
def iceberg_identification(radar_data_texture):

    # The below resource was used to apply numpy.where function result to the 
    # array
    # https://stackoverflow.com/questions/42492342/apply-function-to-result-of-
    # numpy-where

   
    # Create the variable with 0 and 1. 0 refer to the sea level, 1 to 
    # the iceberg
    ice_data = -(radar_data_texture >= 100).astype(np.int)
    
    iceberg_number = 0
    
    y_len, x_len = ice_data.shape
    
    for y in range(y_len):
        for x in range(x_len):
            if ice_data[y][x] < 0:
                
                y1 = (y - 1) if ((y - 1) >= 0) else 0
                y2 = (y + 2) if ((y + 2) < y_len) else y_len
                x1 = (x - 1) if ((x - 1) >= 0) else 0
                x2 = (x + 2) if ((x + 2) < x_len) else x_len
                
                ice_data_slice = ice_data[y1:y2, x1:x2]
                
                ice_data_slice_pos = np.where(ice_data_slice > 0)
                if len(ice_data_slice[ice_data_slice_pos]) == 0:
                    iceberg_number +=1
                    iceberg_number_temp = iceberg_number
                else:
                    iceberg_number_temp = np.max(ice_data_slice[\
                                                           ice_data_slice_pos])
                    
                ice_data_slice_neg = np.where(ice_data_slice < 0)
                ice_data_slice[ice_data_slice_neg] = iceberg_number_temp
                
    return ice_data, iceberg_number                
    

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
#lidar_data_file_path = 'input/white1.lidar'
#radar_data_file_path = 'input/white1.radar'

# Define input file paths for multiple bergs
lidar_data_file_path = 'input/white2.lidar'
radar_data_file_path = 'input/white2.radar'

# Define output file path
output_file_path = 'output/results.txt'

# End of Create variables
#==============================================================================


# Main part of the code
#==============================================================================

# Read input files and assign texture and height info to the variables
lidar_data_height = read_file(lidar_data_file_path)
radar_data_texture = read_file(radar_data_file_path)

# Identify the mupltiple icebergs from the radar image
ice_data, ice_count = iceberg_identification(radar_data_texture)

# Create the Iceberg object from the input  image files
for ice_no in range(1, ice_count + 1):
    icebergs.append(icebergstructure.Iceberg(ice_data, lidar_data_height, \
                                             ice_no))

# Draw result in the canvas
draw_result_multiple(ice_data, icebergs, radar_data_texture, lidar_data_height)

# Write the results of the analysis to text file
write_file(output_file_path, icebergs)

# End of Main part of the code
#==============================================================================