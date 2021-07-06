# J YAP July 2021
# Script to calculate approximate range in media for protons
# Selection of media chosen based on relevance in particle therapy applications
# Uses values from NIST database for density, projected range according to energies

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

#Materials and density
d = open("Densities.txt","r")
lines = d.readlines()
for x in lines:
        Mat.append(x.split(' ')[0])
for x in lines:
        Rho.append(x.split(' ')[1])
        rho = [float(i) for i in Rho]

#List all media types
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

    else: 
     print("Please choose a media")
     WhichMedia()
  
# find nearest energy values
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return E_i[idx], E_i[idx+1]


#Make sure NIST media files are saved with values tab separated
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
        
        #Interpolate between tabulated values
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
        
print("To calculate to approximate the range of protons in different media. First choose the mediumR.")

Medium = WhichMedia()

density_index = Mat.index(Medium)
density = np.float(Rho[density_index])
print(str(Medium) +" has a density of " + str(density) + " g/cm^3")
        
Energy = float(input("What is the mean kinetic beam energy? [MeV] \n"))
print(str(Energy)+ " MeV")    

ProjR=TableCalc()
range = np.float(ProjR)
Range = range/density

print("The range of " +  str(Energy) + " MeV " + str(particle) +" in " + str(Medium) + " is " + str(round(Range,4))+" cm")  