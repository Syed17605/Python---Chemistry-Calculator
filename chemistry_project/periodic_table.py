import csv
import re
from element import Element

class PeriodicTable:
    def __init__(self, csv_file_path: str): # Constructor, loads the CSV file
        self.elements = {}
        self.load_elements(csv_file_path)

    def load_elements(self, file_path: str) -> None: # Extracts csv File data
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # Skip the header
            for row in reader:
                symbol = row[2].strip() # Extract the symbol (3rd column)
                atomic_mass = float(row[3].strip()) # Atomic mass (4th column)
                self.elements[symbol] = Element(symbol, atomic_mass)
    
    def get_molar_mass(self, formula: str) -> float: # Copy of this is made in ChemistryCalculator class; optimize later
        pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
        molar_mass = 0.0

        for match in pattern.finditer(formula):
            element_symbol = match.group(1)
            count_str = match.group(2)
            count = int(count_str) if count_str else 1 # Count the number of times a specific element appears

            element = self.elements.get(element_symbol)
            if element is None:
                raise ValueError(f"Element with symbol '{element_symbol}' not found.")
            molar_mass += element.get_atomic_mass() * count

        return molar_mass
    
    def get_moles_to_mass(self, formula: str, moles: float) -> float: # Copy of this is made in ChemistryCalculator class; optimize later
        molar_mass = self.get_molar_mass(formula)
        return (moles * molar_mass)
    
    def get_mass_to_moles(self,formula: str, mass: float) -> float: # Copy of this is made in ChemistryCalculator class; optimize later
        molar_mass = self.get_molar_mass(formula)
        return (mass / molar_mass)