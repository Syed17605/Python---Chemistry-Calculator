from periodic_table import PeriodicTable # Importing the PeriodicTable class

class ChemistryCalculator:
    periodic_table = PeriodicTable("Periodic Table of Elements.csv")

    def get_molar_mass(self, formula: str) -> float:
        molar_mass = self.periodic_table.get_molar_mass(formula)
        print(f"Molar Mass of {formula}: {molar_mass} g/mol")
        return molar_mass
    
    def get_moles_to_mass(self, formula: str, moles: float) -> float:
        mass = self.periodic_table.get_moles_to_mass(formula, moles)
        print(f"Mass of {moles} moles of {formula}: {mass} g")
        return mass
    
    def get_mass_to_moles(self, formula: str, mass: float) -> float:
        moles = self.periodic_table.get_mass_to_moles(formula, mass)
        print(f"Moles in {mass} grams of {formula}: {moles} mol")
        return moles