Simple scripts to calculate the range of electrons and protons in different media \

These are based on values from the NIST PSTAR & ESTAR database \
The different media were chosen based on relevance in particle therapy applications \
Written by J Yap, 2021

### Main files

CSDARangeCalc.py (CSDA range: Protons & Electrons) \
ProjRangeCalc.py (Projected range: Protons only)

### Data files
Densities.txt \
Electrons/Electrons_*Media*_ NIST i.e. Electrons_Air_NIST.txt \
Protons/Protons_*Media*_NIST i.e. Protons_Air_NIST.txt 

#### Note
To add more materials: \
-> In .py script, create while loops in function WhichMedia() \
-> Create Media.txt file from NIST \
-> Add info to Densities.txt


#### NIST sources

PSTAR: https://physics.nist.gov/PhysRefData/Star/Text/PSTAR.html \
ESTAR: https://physics.nist.gov/PhysRefData/Star/Text/ESTAR.html \
Material compositions: https://physics.nist.gov/cgi-bin/Star/compos.pl?ap \
Definitions: https://physics.nist.gov/PhysRefData/Star/Text/appendix.html
