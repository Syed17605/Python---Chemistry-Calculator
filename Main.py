# IMPORTANT!
# Since this module houses functions and not a specific class the order of declaration matters here
# Run the main.py file to use this program
# Another note, this entire program needs to be optimize but I'm too lazy to optimize this right now

# Importing classes
from TemperatureConverter import TemperatureConverter
from MassConverter import MassConverter
from VolumeConverter import VolumeConverter
from ChemistryCalculator import ChemistryCalculator

def displayMainMenu():
    print("===== Menu =====")
    print("1. Converting temperature?")
    print("2. Converting mass?")
    print("3. Converting volume?")
    print("4. Molar Mass and Moles Conversion")
    print("5. Exit.")
    return input("Please enter your choice (1-5): ")

def displayMolarMassMenu():
    print("===== Molar Mass and Moles Conversion =====")
    print("1. Get Molar Mass")
    print("2. Convert Moles to Mass")
    print("3. Convert Mass to Moles")
    print("4. Return to Main Menu")
    return input("Please enter your choice (1-4): ")

def handleTemperatureConversion():
    temperatureObject = TemperatureConverter()
    value = float(input("enter the temperature value: "))
    fromUnit = input("From unit (C/F/K): ").upper()
    toUnit = input("To unit (C/F/K): ").upper()

    result = temperatureObject.convert(value, fromUnit, toUnit)
    print(f"Converted Temperature: {result}")

def handleMassConversion():
    massObject = MassConverter()
    value = float(input("Enter the mass value: "))
    fromUnit = input("From unit (kg/g/lbs): ")
    toUnit = input("To unit (kg/g/lbs): ")

    result = massObject.convert(value, fromUnit, toUnit)
    print(f"Converted Mass: {result}")

def handleVolumeConversion():
    volumeObject = VolumeConverter()
    value = float(input("Enter the volume value: "))
    fromUnit = input("From unit (L/mL/gal/cc): ")
    toUnit = input("To unit (L/mL/gal/cc): ")

    result = volumeObject.convert(value, fromUnit, toUnit)
    print(f"Converted Volume: {result}")

def handleMolarMassConversion():
    molarObject = ChemistryCalculator()
    while True:
        subChoice = displayMolarMassMenu()

        if subChoice == '1':
            formula = input("Enter the chemical formula: ")
            molarObject.getMolarMass(formula)
        elif subChoice == '2':
            formula = input("Enter the chemical formula: ")
            moles = float(input("Enter the number of moles: "))
            molarObject.getMolesToMass(formula, moles)
        elif subChoice == '3':
            formula = input("Enter the chemical formula: ")
            mass = float(input("Enter the mass of the element/compound in grams: "))
            molarObject.getMassToMoles(formula, mass)
        elif subChoice == '4':
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def main(): # Main method, where the entire program will execute from
    while True:
        choice = displayMainMenu()

        if choice == '1':
            handleTemperatureConversion()
        elif choice == '2':
            handleMassConversion()
        elif choice == '3':
            handleVolumeConversion()
        elif choice == '4':
            handleMolarMassConversion()
        elif choice == '5':
            print("Have a nice day! :)")
            break
        else:
            print("invalid choice. PLease try again.")

if __name__ == "__main__": # Checks if the module is being run directly or imported
    main()