from nicegui import ui

from periodic_table import PeriodicTable # Importing the PeriodicTable class

class ChemistryCalculator:
    def __init__(self, container: ui.row):
        self.container = container
        self.periodic_table = PeriodicTable("Periodic Table of Elements.csv")

    def display_molar_mass_menu() -> str:
        print() # Formatting reasons (when ran in cmd)
        print("===== Molar Mass and Moles Conversion =====")
        print("1. Get Molar Mass")
        print("2. Convert Moles to Mass")
        print("3. Convert Mass to Moles")
        print("4. Return to Main Menu")
        return input("Please enter your choice (1-4): ")

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
    
    @staticmethod # This is a static function; not using any instance variables
    def handle_molar_mass_conversion() -> None:
        molar_object = ChemistryCalculator()
        while True:
            sub_choice = ChemistryCalculator.display_molar_mass_menu()

            if sub_choice == '1':
                print() # Formatting reasons (when ran in cmd)
                formula = input("Enter the chemical formula: ")
                molar_object.get_molar_mass(formula)
            elif sub_choice == '2':
                print() # Formatting reasons (when ran in cmd)
                formula = input("Enter the chemical formula: ")
                moles = float(input("Enter the number of moles: "))
                molar_object.get_moles_to_mass(formula, moles)
            elif sub_choice == '3':
                print() # Formatting reasons (when ran in cmd)
                formula = input("Enter the chemical formula: ")
                mass = float(input("Enter the mass of the element/compound in grams: "))
                molar_object.get_mass_to_moles(formula, mass)
            elif sub_choice == '4':
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please try again.")