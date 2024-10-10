# IMPORTANT!
# Since this module houses functions and not a specific class the order of declaration matters here
# Run the main.py file to use this program
# Another note, this entire program needs to be optimize but I'm too lazy to optimize this right now

# Importing classes
from temperature_converter import TemperatureConverter
from mass_converter import MassConverter
from volume_converter import VolumeConverter
from pressure_converter import PressureConverter
from chemistry_calculator import ChemistryCalculator

def display_main_menu() -> str:
    print("===== Menu =====")
    print("1. Converting temperature?")
    print("2. Converting mass?")
    print("3. Converting volume?")
    print("4. Converting pressure?")
    print("5. Molar Mass and Moles Conversion")
    print("6. Exit.")
    return input("Please enter your choice (1-6): ")

def display_molar_mass_menu() -> str:
    print("===== Molar Mass and Moles Conversion =====")
    print("1. Get Molar Mass")
    print("2. Convert Moles to Mass")
    print("3. Convert Mass to Moles")
    print("4. Return to Main Menu")
    return input("Please enter your choice (1-4): ")

def handle_temperature_conversion() -> None:
    temperature_object = TemperatureConverter()
    value = float(input("Enter the temperature value: "))
    from_unit = input("From unit (C/F/K): ").upper()
    to_unit = input("To unit (C/F/K): ").upper()

    result = temperature_object.convert(value, from_unit, to_unit)
    print(f"Converted Temperature: {result}")

def handle_mass_conversion() -> None:
    mass_object = MassConverter()
    value = float(input("Enter the mass value: "))
    from_unit = input("From unit (kg/g/lbs): ").lower()
    to_unit = input("To unit (kg/g/lbs): ").lower()

    result = mass_object.convert(value, from_unit, to_unit)
    print(f"Converted Mass: {result}")

def handle_volume_conversion() -> None:
    volume_object = VolumeConverter()
    value = float(input("Enter the volume value: "))
    from_unit = input("From unit (L/mL/gal/cc): ").lower()
    to_unit = input("To unit (L/mL/gal/cc): ").lower()

    result = volume_object.convert(value, from_unit, to_unit)
    print(f"Converted Volume: {result}")

def handle_pressure_conversion() -> None:
    pressure_object = PressureConverter()
    value = float(input("Enter the pressure value: "))
    from_unit = input("From unit (Pa/atm/mmHg/inHg/torr)").lower()
    to_unit = input("To unit (Pa/atm/mmHg/inHg/torr)").lower()

    result = pressure_object.convert(value, from_unit, to_unit)
    print(f'Converted Pressure: {result}')

def handle_molar_mass_conversion() -> None:
    molar_object = ChemistryCalculator()
    while True:
        sub_choice = display_molar_mass_menu()

        if sub_choice == '1':
            formula = input("Enter the chemical formula: ")
            molar_object.get_molar_mass(formula)
        elif sub_choice == '2':
            formula = input("Enter the chemical formula: ")
            moles = float(input("Enter the number of moles: "))
            molar_object.get_moles_to_mass(formula, moles)
        elif sub_choice == '3':
            formula = input("Enter the chemical formula: ")
            mass = float(input("Enter the mass of the element/compound in grams: "))
            molar_object.get_mass_to_moles(formula, mass)
        elif sub_choice == '4':
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def main() -> None: # Main method, where the entire program will execute from
    while True:
        choice = display_main_menu()

        if choice == '1':
            handle_temperature_conversion()
        elif choice == '2':
            handle_mass_conversion()
        elif choice == '3':
            handle_volume_conversion()
        elif choice == '4':
            handle_pressure_conversion()
        elif choice == '5':
            handle_molar_mass_conversion()
        elif choice == '6':
            print("Have a nice day! :)")
            break
        else:
            print("invalid choice. PLease try again.")

if __name__ == "__main__": # Checks if the module is being run directly or imported
    main()
