# J YAP July 2021
# Script to calculate approximate range in media for electrons and protons
# Selection of media chosen based on relevance in particle therapy applications
# Uses values from NIST database for density, CSDA range according to energies (0.001-1000 MeV)

import numpy as np

E_i = []
SP_i = []
CSDA_i = []
Energies = []
Mat = []
Rho = []
density_index = []
Medium = ''

# Materials and density
d = open("Densities.txt","r")
lines = d.readlines()
for x in lines:
        Mat.append(x.split(' ')[0])
for x in lines:
        Rho.append(x.split(' ')[1])
        rho = [float(i) for i in Rho]


def WhichParticle():
    particleType = input("1=electrons or 2=protons?\n")

    if particleType == '1':
        
        particle = str(input('electrons'))        
        particle = "Electrons"
                
    if particleType == '2':
            
        particle = str(input('protons'))
        particle = "Protons"

    return particle
 
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

    while medium == 'Concrete': # only electrons
        Medium = "Concrete"    
        return Medium    

    else: 
     print("Please choose a media")
     Medium = WhichMedia()
     return Medium
  
# Find nearest energy values
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return E_i[idx], E_i[idx+1]


# Make sure NIST media files are saved with values tab separated
# If no such file, the data does not exist for that particle in the specific medium (i.e. protons in Concrete)
def TableCalc(): 
    #Check if exact energy is listed in NIST table
   
    f = open(particle+"/"+particle+"_"+Medium+"_NIST.txt","r")
    
    for line in f.readlines():            
        currentline = line.split("\t")
        E = float(currentline[0])
        Range = float(currentline[4])  
        E_i.append(E)
        CSDA_i.append(Range)
              
    if Energy in E_i:
       indexE = E_i.index(Energy)
       CSDA = CSDA_i[indexE]
       
       return CSDA
       
    else:
        nearestE = find_nearest(E_i,Energy)
        Elow = nearestE[0]
        Ehigh = nearestE[1]
        indexCSDAlow = E_i.index(Elow)
        indexCSDAhigh = E_i.index(Ehigh)
        CSDAlow = CSDA_i[indexCSDAlow]
        CSDAhigh = CSDA_i[indexCSDAhigh]
        
        # Interpolate between tabulated values
        if Energy < Elow:
            denominator = Ehigh - Energy
            baseline = CSDAhigh
            
        if Energy > Elow:
            denominator = Energy - Elow
            baseline = CSDAlow
            
        graduation = (CSDAhigh-CSDAlow)/(Ehigh-Elow)
        interpolatedRange = (denominator)*graduation + baseline
        
        return interpolatedRange
    
             
## START ##
        
print("To calculate to approximate the range of electrons or protons in different media. First choose a particle type.")

particle = WhichParticle()
Medium = WhichMedia()

density_index = Mat.index(Medium)
density = np.float(Rho[density_index])
print(str(Medium) +" has a density of " + str(density) + " g/cm^3")
        
Energy = float(input("What is the mean kinetic beam energy? [MeV] \n"))
print(str(Energy)+ " MeV")    

CSDA=TableCalc()
range = np.float(CSDA)
Range = range/density

# Unit conversion display: cm (default), m, mm, um
if 1 < Range < 100:
    print("The range of " +  str(Energy) + " MeV " + str(particle) +" in " + str(Medium) + " is " + str(round(Range,4))+" cm")  

if Range >= 100:
    print("The range of " +  str(Energy) + " MeV " + str(particle) +" in " + str(Medium) + " is " + str(round(Range/100,4))+" m")  

if 0.001 <= Range <= 1: 
    print("The range of " +  str(Energy) + " MeV " + str(particle) +" in " + str(Medium) + " is " + str(round(Range*10,4))+" mm")  

if Range < 0.001: 
    print("The range of " +  str(Energy) + " MeV " + str(particle) +" in " + str(Medium) + " is " + str(round(Range*10000,4))+" \u03bcm")  
