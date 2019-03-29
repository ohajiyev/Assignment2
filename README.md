# Assignment 2
The purpose of the repo is to fulfill the requirements of the Assignment 2 of the Module GEOG5991M 

## Instructions of ice_v2.py script

Date Last Updated: 
    Mar 29, 2019

Author: 
    Orkhan Hajiyev (gy17oh)

Title: 
    Assignment 2. Module GEOG5991M
    White Star Line Project

Version: 
    2.0

Purpose: 
    To implement the requirements of the Assignment 2 of the Module GEOG5991M.
    The version was built to analyse MULTIPLE iceberg images.
    
    White Star Line was selected as the project to satisfy the assignment's
    description. The link to the project's problem definition:
    https://www.geog.leeds.ac.uk/courses/computing/
    study/core-python-odl/assessment2/ice.html
    
    Briefly, the goal is to analyse two raster files of the size 300 by 300 of 
    the radar and lidar images of the sea and identify the multiple bergs. 
    
License: 
    Copyright (c) 2019 Orkhan Hajiyev
    Lisence under MIT License
    License link: 
        https://github.com/ohajiyev/Assignment2/blob/master/LICENSE.md
       
Github Repo Link: 
    https://github.com/ohajiyev/Assignment2
    
Code Folder Link:
    https://github.com/ohajiyev/Assignment2/tree/master/python/src/unpackaged/
    ice/Version2

Zip file link:
    https://github.com/ohajiyev/Assignment2/tree/master/python/src/unpackaged/
    ice/Version2/assignment2.zip

Instructions to run:
    Download 'assignment2.zip' file and extract.
    The extracted folder should contain the following files and folders, as 
    minimum:
        'ice_v2.py' - main code to run from command prompt
        'icebergstructure.py' - Iceberg class definiton
        'ice2_notebook.ipynb' - Jupyter Notebook file
        'input' - folder which contains input images 'white2.lidar' and 
                  'white2.radar'
        'input/white2.lidar' - lidar image (300x300) of an area of sea with 
                               the multiple bergs. Values (0-255) contain 
                               height data of the objects
        'input/white2.radar' - radar image (300x300) of an area of sea with 
                               the multiple bergs. Values (0-255) contain 
                               information to idenitify the bergs (>=100)
        'output' - folder which is output folder for the result text file 
                   ('result.txt)
    Software requirements:
        Anaconda3 (64bit):
            Python 3.7
            Spyder 3.3.2
            Jupiter Notebook
            Anaconda prompt
        
    The code can be run in Anaconda command line, Spyder and Jupyter notebook.
        Anaconda cmd: 
            1. 'python ice_v2.py'
        Spyder: 
            1. Open 'ice_v2.py
            2. Ensure that IPython console is activated
            3. Run '#%matplotlib qt5' command in IPython console to interact
               with interface.
            4. Press 'F5' button or 'Run' from the  menu to run the code
        Jupyter Notebook:
            1. Open 'ice2_notebook.ipynb' in browser
            2. Run first line '%matplotlib notebook' to enable interaction
               with the output
            3. Press 'Run all' from Run menu
        
Limitations:
    The code only was tested and developed with/for available two sets of the 
    inputs provided by the University. It is assumed that the bergs data should 
    be continuous and without any gaps in the files. Any gaps in input data
    may wrongly identify the bergs. This is artificial files and in the reality
    no image can come ideally without any gaps or distortions. For real images
    the algorithms which is used to bergs identification hardly can be applied.
    For the real case object classification method of machine learning should
    be applied.
    
Evident improvements:
    Code can be improved by separation of visualisation part into instance
    class and be enhanced by using real GUI not relying only on matplotlib
    capability. Machine learning techniques can be implemented to improve
    identification of bergs.
    
Python version: 
    3.7 (Python 3.7.1 64-bit | Qt 5.9.6 | PyQt5 5.9.2 | Windows 10)

Coding Tool:
    Spyder Version 3.3.2

!!! Important note: some part of the code may be copied and modified from 
!!! different sources which are explitely shown in the comments below

Please see Readme.md file in repo for the same instructions:
    https://github.com/ohajiyev/Assignment2/blob/master/README.md
