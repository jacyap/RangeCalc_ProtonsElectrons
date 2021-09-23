## Simple python scripts to calculate the range of electrons and protons in different media.

These are based on values from the NIST PSTAR & ESTAR database, to save manual calculation from the look up tables. \
The different media were chosen based on relevance in particle therapy applications. \
Note: The code interpolates (linearly) between values for the energy/range values not explicitly listed. \
Run with Python 3.8.3 \
Written by J Yap, 2021

![Terminal](https://github.com/jacyap/RangeCalc_ProtonsElectrons/blob/main/RangeCalc.png)

### Main files

CSDARangeCalc.py (CSDA range: Protons & Electrons) \
ProjRangeCalc.py (Projected range: Protons only)

### Data files
Densities.txt \
Electrons/Electrons_*Medium*_ NIST i.e. Electrons_Air_NIST.txt \
Protons/Protons_*Medium*_NIST i.e. Protons_Air_NIST.txt 

#### Bonus
To add more materials: \
-> In .py script, create while loops to call the Medium in function WhichMedia() \
-> Create Media.txt file from NIST \
-> Add info to Densities.txt


#### NIST sources

PSTAR: https://physics.nist.gov/PhysRefData/Star/Text/PSTAR.html \
ESTAR: https://physics.nist.gov/PhysRefData/Star/Text/ESTAR.html \
Material compositions: https://physics.nist.gov/cgi-bin/Star/compos.pl?ap \
Definitions: https://physics.nist.gov/PhysRefData/Star/Text/appendix.html
