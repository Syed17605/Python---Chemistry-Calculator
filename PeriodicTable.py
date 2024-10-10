import csv
import re
from Element import Element

class PeriodicTable:
    def __init__(self, csvFilePath: str): # Constructor, loads the CSV file
        self.elements = {}
        self.loadElements(csvFilePath)

    def loadElements(self, filePath: str) -> None: # Extracts csv File data
        with open(filePath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # Skip the header
            for row in reader:
                symbol = row[2].strip() # Extract the symbol (3rd column)
                atomicMass = float(row[3].strip()) # Atomic mass (4th column)
                self.elements[symbol] = Element(symbol, atomicMass)
    
    def getMolarMass(self, formula: str) -> float: # Copy of this is made in ChemistryCalculator class; optimize later
        pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
        molarMass = 0.0

        for match in pattern.finditer(formula):
            elementSymbol = match.group(1)
            countStr = match.group(2)
            count = int(countStr) if countStr else 1 # Count the number of times a specific element appears

            element = self.elements.get(elementSymbol)
            if element is None:
                raise ValueError(f"Element with symbol '{elementSymbol}' not found.")
            molarMass += element.getAtomicMass() * count

        return molarMass
    
    def getMolesToMass(self, formula: str, moles: float) -> float: # Copy of this is made in ChemistryCalculator class; optimize later
        molarMass = self.getMolarMass(formula)
        return (moles * molarMass)
    
    def getMassToMoles(self,formula: str, mass: float) -> float: # Copy of this is made in ChemistryCalculator class; optimize later
        molarMass = self.getMolarMass(formula)
        return (mass / molarMass)