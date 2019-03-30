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
# Import modules

import sys
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.patches as mpatches
import numpy as np

# End of Import modules
#==============================================================================


#==============================================================================
# ImageHandle class definition. 

class ImageHandle():
        
    #==========================================================================
    # Function definitions
    def update_result_text_plot(self, ax_result, icebergs, iceberg_no):
        """
        Update the resultant plot area appropriately with the text obtained
        from Iceberg object
        
        Arguments required:
            ax_result - subplot area of the resultant text (no default)
            icebergs - list of Iceberg objects (no default)
            iceberg_no - the number of the Iceberg object (no default)
            
        Returns:
            No return
        """
        # clear resultant subplot area before showing the text
        ax_result.clear()
        
        # title for the result plot area
        text_result = 'Results of image analysis of berg'
        text_result += '\nHover over the icebergs to view characteristics'
        
        # show the result title text
        ax_result.text(0, 115, text_result, 
                       bbox={'facecolor': 'white', 'pad': 5})
        
        # show the result text returned from iceberg object on the plot area
        ax_result.text(0, 285, str(icebergs[iceberg_no-1]), 
                       bbox={'facecolor': 'white', 'pad': 5})
        
        # turn off the resultant subplot area borders to keep only text
        ax_result.axis('off')
        
        # refresh plot area to view changes
        ax_result.figure.canvas.draw_idle()
    
    def on_hover(self, event, icebergs, iceberg_data, ax_result, 
                 iceberg_quantity):
        """
        Identify the mouse location over analysed image plot area and
        call update method of the resultant plot area appropriately
        
        The following code is altered from the source 
        https://stackoverflow.com/questions/7908636/possible-to-make-labels-
        appear-when-hovering-over-a-point-in-matplotlib
        
        Arguments:
            event - event handling information
            icebergs - list of Iceberg objects (no default)
            iceberg_data - numpy array of identified bergs data (no default)
            ax_result - subplot area of the resultant text (no default)
            iceberg_quantity - the quantity of the Iceberg objects (no default)
            
        Returns:
            No return
        """
        # Check if event occured on subplot areas
        if event.inaxes is not None:
            # Check if event occured on subplot area Analysed Icebergs
            if event.inaxes.title.get_text() == 'Analysed Icebergs':
                # Identify suggested iceberg number
                iceberg_no = iceberg_data[int(round(event.ydata))] \
                                         [int(round(event.xdata))]
                # Update the result text if value belongs to any iceberg
                if iceberg_no in range (1, iceberg_quantity+1):
                    self.update_result_text_plot(ax_result, icebergs, 
                                                 iceberg_no)
                    
        
        
    def draw_result_multiple(self, 
                             iceberg_data, icebergs,
                             radar_data_texture, 
                             lidar_data_height):
        """
        Draw input images and result of analysis (both image and text) in the 
        canvas and activate hovering fucntion to view the resultant text of the 
        specific berg
        
        Arguments:
            iceberg_data - numpy array of identified bergs data (no default)
            icebergs - list of Iceberg objects (no default)
            radar_data_texture - numpy array contains texture of the objects 
                                 (no default)
            lidar_data_height - numpy array contains height of the objects 
                                (no default)
            
        Results:
            No result
        """
                        
        #!!!!! The following resources were used in the creation of the method 
        # https://stackoverflow.com/questions/25482876/how-to-add-legend-to-
        # imshow-in-matplotlib
        # https://stackoverflow.com/questions/9707676/defining-a-discrete-
        # colormap-for-imshow-in-matplotlib/9708079
        
        # Classification of icebergs into pullable and not. Assign values 1 
        # and 2. 1 means that the berg is pullable and 2 is not pullable. 
        # Calculation of unique values of iceberg_data_pullable.  
        # Value_desciption is used for the legend
        iceberg_data_pullable, \
        values_unique, \
        value_description = self.icebergs_pullable_classification(
                                                            icebergs, 
                                                            iceberg_data
                                                            )
    
        # Create 4 plot areas, first pair at the top for input images 
        # visualisation and the second pair for analysed image and the result 
        # text
        fig, ax = plt.subplots(2, 2, figsize=(8,8), sharey=True)
        
        # Visualisation of input images
        #======================================================================
        ax[0, 0].imshow(radar_data_texture)
        ax[0, 0].set_title('Input Radar Image')
        ax[0, 1].imshow(lidar_data_height)
        ax[0, 1].set_title('Input Lidar Image')
        
        # Visualisation of analysed images
        #======================================================================
        # Make a color map of fixed colors, blue for the sea (0), green (1) for 
        # the pullable bergs and red (2) for berg which cannot be pulled 
        cmap = colors.ListedColormap(['blue', 'green', 'red'])
        bounds=[0,0.5,1,1.5,2]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        
        # Plot image with predefined colors
        im = ax[1, 0].imshow(
                iceberg_data_pullable, 
                interpolation='none', 
                cmap=cmap, norm=norm)
        
        # Identify the colors from the plot. In this case it is blue, gren and 
        # red
        colors_image = [im.cmap(im.norm(value)) for value in values_unique]
        
        # Create a patch for every color 
        patches = [mpatches.Patch(color=colors_image[i], 
                   label="{}".format(value_description[i])) 
                   for i in range(len(values_unique))]
        
        # Put those patched as legend-handles into the legend
        ax[1, 0].legend(handles=patches, bbox_to_anchor=(1.05, 1), 
                        loc=2, borderaxespad=0.)
        
        ax[1, 0].set_title('Analysed Icebergs')
        
        # Anotate the bergs on the analysed image
        #======================================================================
        iceberg_quantity = len(icebergs)
        for berg in icebergs:
            ice_ind = np.where(iceberg_data == berg.iceberg_no)
            ax[1, 0].annotate(
                    str(berg.iceberg_no), 
                    xy=(ice_ind[1][0], 
                    ice_ind[0][0]-10
                    ), 
                    bbox=dict(
                            boxstyle="round, pad=0.1", 
                            fc="w"
                            )
                    )
            
        # Visualisation of the result text
        #======================================================================
        self.update_result_text_plot(ax[1, 1], icebergs, 1)
        
        # Activation of hovering function to view result text of analysed bergs
        #======================================================================
        fig.canvas.mpl_connect(
                'motion_notify_event', 
                lambda event: self.on_hover(event, icebergs, iceberg_data, 
                                       ax[1, 1], iceberg_quantity))
        
        plt.show()
        
    def read_file(self, file_name):    
        """ Read input file and convert to numpy array dataset """
        
        # Try to read the input files
        # Note: assigning new value to environment variable make it local,
        # so return function was used
        try:
            image_data = np.loadtxt(file_name, delimiter = (','))
            return image_data     
        except IOError as err:
            print(err)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            
    def write_file(self, file_name, icebergs):    
        """ Write result of analysis into output file """
        
        # Try to write the result to the output file
        # Result is the list of the icebergs with calculated parameters
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
            
    def icebergs_pullable_classification(self, icebergs, iceberg_data):
        """
        Classify the available iceberg data into pullable and not
        
        Arguments:
            icebergs - list of Iceberg objects (no default)
            iceberg_data - numpy array of identified bergs data (no default)  
        
        Returns:
            iceberg_data_pullable_local - numpy array contains integer value  
                                          0, 1 or 2. 
                                          0 - Sea level; 
                                          1 - Pullable Berg;
                                          2 - Not Pullable Berg
            values - unique values of obtained dataset 
                     iceberg_data_pullable_local
            value_descr - dictionary of unique values to display on legend
        """
        
        # Create a copy of iceberg_data to modify it and assign values 1 and 2.
        # 1 means that the berg is pullable and 2 is not pullable
        iceberg_data_pullable_local = np.copy(iceberg_data)
        
        # Take subset of iceberg_data dataset and assign 1 or 2 based on the 
        # condition to the new dataset iceberg_data_pullable_local
        for berg in icebergs:
            iceberg_data_slice_temp = np.where(iceberg_data == berg.iceberg_no)
            if berg.berg_pullable:
                iceberg_data_pullable_local[iceberg_data_slice_temp] = 1
            else:
                iceberg_data_pullable_local[iceberg_data_slice_temp] = 2
                
        # Get the unique values from data. In this case it will be 0, 1 nad 2.
        # 0 refer to the sea level, 1 to the pullable iceberg and 2 to the  
        # iceberg which cannot be pulled
        values = np.unique(iceberg_data_pullable_local.ravel())
        
        # Create the dictionary of unique values to display on legend    
        value_descr = {0: 'Sea level', 1: 'Iceberg pullable', \
                             2: 'Iceberg not pullable',}
        return iceberg_data_pullable_local, values, value_descr
    
            
    def iceberg_identification(self, radar_data_texture):
        """
        Identify the mupltiple icebergs and quantity from the radar image
        
        Arguments:
            radar_data_texture - numpy array of radar image 
        
        Returns:
            iceberg_data - numpy array contains unique integer value for each 
                           iceberg and 0 is for sea level. 
            iceberg_quantity - quantity of the identified icebergs
        """
       
        # Create the variable with 0 and -1. 0 refer to the sea level, -1 to 
        # the iceberg
        iceberg_data = -(radar_data_texture >= 100).astype(np.int)
        
        # Initiate the varible
        iceberg_quantity = 0
        
        # Get dimensions of the iceberg_data dataset. In this case y_len and 
        # x_len are both equal to 300
        y_len, x_len = iceberg_data.shape
        
        # Identify icebergs. Algorithm goes through all values once and assign
        # values to the adjacent cells with the values -1. If any new 
        # disconnected -1 value found then iceberg_quantity increased by 1 and  
        # assigned to the cell
        for y in range(y_len):
            for x in range(x_len):
                if iceberg_data[y][x] < 0:
                    # Prevent array index to be out of bounds
                    y1 = (y - 1) if ((y - 1) >= 0) else 0
                    y2 = (y + 2) if ((y + 2) < y_len) else y_len
                    x1 = (x - 1) if ((x - 1) >= 0) else 0
                    x2 = (x + 2) if ((x + 2) < x_len) else x_len
                    
                    # Select adjacent cells of the x,y of the iceberg
                    iceberg_data_slice = iceberg_data[y1:y2, x1:x2]
                    
                    # Select cells with already identified iceberg values (>0)
                    iceberg_data_slice_pos = np.where(iceberg_data_slice > 0)
                    
                    # Increase iceberg_quantity by 1 and assign the new value 
                    # to the adjacent cells with -1 values of the temporary 
                    # array
                    if len(iceberg_data_slice[iceberg_data_slice_pos]) == 0:
                        iceberg_quantity +=1
                        iceberg_quantity_temp = iceberg_quantity
                    # Assign the value of the cell which already was identified 
                    # to the adjacent cells with -1 values of the temporary 
                    # array
                    else:
                        iceberg_quantity_temp = np.max(iceberg_data_slice
                                                      [iceberg_data_slice_pos])
                    
                    # Alter the iceberg_data with the new identified cell 
                    # values    
                    iceberg_data_slice_neg = np.where(iceberg_data_slice < 0)
                    iceberg_data_slice[iceberg_data_slice_neg] = \
                                                          iceberg_quantity_temp
                    
        return iceberg_data, iceberg_quantity                
        
    
    # End of Function definitions
    #==========================================================================

# End of ImageHandle class definition
#==============================================================================
