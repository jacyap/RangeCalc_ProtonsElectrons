# Script to calculate approximate range in media for protons only (PSTAR)
# Simple calculations to avoid manual searching & computation from NIST look up tables
# Selection of media chosen based on relevance in particle therapy applications
# Uses values from NIST database for density, projected range according to energies (0.001-1000 MeV)
# J YAP, July 2021. jacinta.yap@unimelb.edu.au

import numpy as np

E_i = []
SP_i = []
ProjR_i = []
Energies = []
Mat = []
Rho = []
density_index = []
Medium = ''
particle = "Protons"

# Materials and density
d = open("Densities.txt","r")
lines = d.readlines()
for x in lines:
        Mat.append(x.split(' ')[0])
for x in lines:
        Rho.append(x.split(' ')[1])
        rho = [float(i) for i in Rho]

Materials_list = Mat.copy()
Materials_list.sort() # Sort Media alphabetically
# List all media types
def WhichMedia(): 
    
    medium = input("What medium? "+ str(Mat)+ ". \n" + "Please input using exact case. \n") 
            
    while medium == 'Air':
        Medium = "Air"
        return Medium

    while medium == 'WaterLiquid':
        Medium = "WaterLiquid"       
        return Medium
    
    while medium == 'Si02':
        Medium = "Si02"         
        return Medium
    
    while medium == 'PyrexGlass':
        Medium = "PyrexGlass"         
        return Medium    
    
    while medium == 'Silicon':
        Medium = "Silicon"         
        return Medium

    while medium == 'Tungsten':
        Medium = "Tungsten"       
        return Medium    
     
    while medium == 'Copper':
        Medium = "Copper"         
        return Medium   

    while medium == 'Lead':
        Medium = "Lead"       
        return Medium
    
    while medium == 'Aluminium':
        Medium = "Aluminium"        
        return Medium  

    while medium == 'Bone':
        Medium = "Bone"         
        return Medium 
    
    while medium == 'PMMA':
        Medium = "PMMA"       
        return Medium    

    while medium == 'MuscleSkeletal':
        Medium = "MuscleSkeletal"         
        return Medium        

    while medium == 'AdiposeTissue':
        Medium = "AdiposeTissue"    
        return Medium   

    while medium == 'Mylar':
        Medium = "Mylar"    
        return Medium    
    
    while medium == 'Beryllium':
        Medium = "Beryllium"    
        return Medium   

    while medium == 'Graphite':
        Medium = "Graphite"    
        return Medium   

    while medium == 'Kapton':
        Medium = "Kapton"    
        return Medium   

    while medium == 'Carbon':
        Medium = "Carbon"    
        return Medium   

    while medium == 'Molybdenum':
        Medium = "Molybdenum"    
        return Medium  

    while medium == 'Titanium':
        Medium = "Titanium"    
        return Medium   
    
    while medium == 'TissueEquivPlastic':
        Medium = "TissueEquivPlastic"    
        return Medium   
    
    while medium == 'Iron':
        Medium = "Iron"    
        return Medium   

    while medium == 'Gold':
        Medium = "Gold"    
        return Medium   

    while medium == 'Silver':
        Medium = "Silver"    
        return Medium   
    
    while medium == 'SodiumIodide':
        Medium = "SodiumIodide"    
        return Medium 

    else: 
     print("Please choose a media")
     Medium = WhichMedia()
     return Medium
  
# Find nearest energy values
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    nearestEnergy = E_i[idx]
    if Energy > nearestEnergy:
        return E_i[idx], E_i[idx+1]
    else: 
        return E_i[idx-1], E_i[idx]

# Make sure NIST media files are saved with values tab separated
def TableCalc(): 
    #Check if exact energy is listed in NIST table
   
    f = open(particle+"/"+particle+"_"+Medium+"_NIST.txt","r")
    for line in f.readlines():            
        currentline = line.split("\t")
        E = float(currentline[0])
        Range = float(currentline[5])  
        E_i.append(E)
        ProjR_i.append(Range)
            
    if Energy in E_i:
       indexE = E_i.index(Energy)
       ProjR = ProjR_i[indexE]

       return ProjR
       
    else:
        nearestE = find_nearest(E_i,Energy)
        Elow = nearestE[0]
        Ehigh = nearestE[1]
        indexProjRlow = E_i.index(Elow)
        indexProjRhigh = E_i.index(Ehigh)
        ProjRlow = ProjR_i[indexProjRlow]
        ProjRhigh = ProjR_i[indexProjRhigh]
        
        # Interpolate between tabulated values
        if Energy < Elow:
            denominator = Ehigh - Energy
            baseline = ProjRhigh
            
        if Energy > Elow:
            denominator = Energy - Elow
            baseline = ProjRlow
            
        graduation = (ProjRhigh-ProjRlow)/(Ehigh-Elow)
        interpolatedRange = (denominator)*graduation + baseline
        
        return interpolatedRange
    
             
## START ##
        
print("To calculate to approximate the range of protons in different media. First choose the medium.")

Medium = WhichMedia()

density_index = Mat.index(Medium)
density = float(Rho[density_index])
print(str(Medium) +" has a density of " + str(density) + " g/cm^3")
        
Energy = float(input("What is the mean kinetic beam energy? [MeV] \n"))
print(str(Energy)+ " MeV")    

ProjR=TableCalc()
range = float(ProjR)
Range = range/density

# Unit conversion display: cm (default), m, mm, um
if 1 < Range < 100:
    print("The range of " +  str(Energy) + " MeV " + str(particle) +" in " + str(Medium) + " is " + str(round(Range,4))+" cm")  

if Range >= 100:
    print("The range of " +  str(Energy) + " MeV " + str(particle) +" in " + str(Medium) + " is " + str(round(Range/100,4))+" m")  

if 0.01 <= Range <= 1: 
    print("The range of " +  str(Energy) + " MeV " + str(particle) +" in " + str(Medium) + " is " + str(round(Range*10,4))+" mm")  

if Range < 0.01: 
    print("The range of " +  str(Energy) + " MeV " + str(particle) +" in " + str(Medium) + " is " + str(round(Range*10000,4))+" \u03bcm")  
