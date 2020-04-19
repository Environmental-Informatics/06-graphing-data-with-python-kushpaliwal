"""
Created on April 19, 2020
by Kush Paliwal

Script to read in a data file and generate summary figures for that file.
"""

import numpy as np
import matplotlib.pyplot as plt

# Input Files

input=["Tippecanoe_River_at_Ora.Annual_Metrics.txt","Wildcat_Creek_at_Lafayette.Annual_Metrics.txt"]

# Output Files

output=["Tippecanoe_River_at_Ora.Annual_Metrics.pdf","Wildcat_Creek_at_Lafayette.Annual_Metrics.pdf"]

# store data file

for i in range(len(input)):

# read and store the original data as data

    data=np.genfromtxt(input[i],dtype=["int","float","float","float","float","float","float"],delimiter='\t',names=True)

    # size of the figure
    
    plt.figure(figsize=(10,10))

    # space between plots
    
    plt.subplots_adjust(hspace=0.3)
    
    # Plot 1

    plt.subplot(311)
    plt.plot(data['Year'],data['Mean'], 'k',
             data['Year'],data['Max'], 'r',
             data['Year'],data['Min'], 'b')
    plt.legend(["Mean","Max","Min"], loc='best',edgecolor='k')
    plt.xlabel("Year")
    plt.ylabel("Streamflow (cfs)")

    # Plot 2

    plt.subplot(312)
    plt.plot(data['Year'],data['Tqmean']*100, 'g^')
    plt.xlabel("Year")
    plt.ylabel("Tqmean (%)")

    # Plot 3

    plt.subplot(313)
    plt.bar(data['Year'],data['RBindex'])
    plt.xlabel("Year")
    plt.ylabel("R-B Index (ratio)")

    # save figure as pdf

    plt.savefig(output[i])
    
    plt.close()