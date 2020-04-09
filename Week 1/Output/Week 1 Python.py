# -*- coding: utf-8 -*-
"""
Created on Thu Apr 9 14:15:10 2020

Week 1

Remember to check sizes of variables if you're having trouble with doing some-
thing that you found online

@author: John Stout
"""

#------------------------------------------------------------------------------
#                 Extracting & Visualizing Position Data
#------------------------------------------------------------------------------

# libraries for opening matlab files
import scipy.io as sio
import os

# define a variable representing the session directory
sessions_folder = 'X:/03. Lab Procedures and Protocols/Matlab Practice'
session = '/Session X'
os.chdir(sessions_folder+session) # cd equivalent

# load Int and TimeVariables dictionaries
TimeVariables = sio.loadmat('VT1.mat')
IntVars       = sio.loadmat('Int_file.mat')

# If you want to isolate an element from the dictionary
ExtractedX = TimeVariables["ExtractedX"]
ExtractedY = TimeVariables["ExtractedY"]
TimeStamps = TimeVariables["TimeStamps"]
Int        = IntVars["Int"]

# convert data
import numpy as np                             # import numPy
numSamples = np.size(ExtractedX)               # how many samples total?
X_data = np.resize(ExtractedX,(numSamples,))   # reformat
Y_data = np.resize(ExtractedY,(numSamples,))

# load in matplotlib library
import matplotlib.pyplot as plt # a plotting library
sampleX = X_data[:50]
sampleY = Y_data[:50]

# plot data
plt.title("Rat Position Data")
plt.xlabel("X-position (in pixels)")
plt.ylabel("Y-position (in pixels)")
plt.plot(X_data,Y_data)
plt.show()

# plot data on a trial-by-trial basis
for i in range(0,np.size(clusters)):







