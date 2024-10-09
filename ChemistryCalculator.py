from PeriodicTable import PeriodicTable # Importing the PeriodicTable class

class ChemistryCalculator:
    periodicTable = PeriodicTable("Periodic Table of Elements.csv")

    def getMolarMass(self, formula: str) -> float:
        molarMass = self.periodicTable.getMolarMass(formula)
        print(f"Molar Mass of {formula}: {molarMass} g/mol")
        return molarMass
    
    def getMolesToMass(self, formula: str, moles: float) -> float:
        mass = self.periodicTable.getMolesToMass(formula, moles)
        print(f"Mass of {moles} moles of {formula}: {mass} g")
        return mass
    
    def getMassToMoles(self, formula: str, mass: float) -> float:
        moles = self.periodicTable.getMolesToMass(formula, moles)
        print(f"Moles in {mass} grams of {formula}: {moles} mol")
        return moles