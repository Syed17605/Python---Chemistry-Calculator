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
from concentration_calculator import ConcentrationCalculator

def display_main_menu() -> str:
    print() # Formatting reasons (when ran in cmd)
    print("===== Menu =====")
    print("1. Converting temperature?")
    print("2. Converting mass?")
    print("3. Converting volume?")
    print("4. Converting pressure?")
    print("5. Molar Mass and Moles Conversion")
    print("6. Molarity Calculations")
    print("7. Exit.")
    return input("Please enter your choice (1-7): ")

def main() -> None: # Main method, where the entire program will execute from
    while True:
        choice = display_main_menu()

        if choice == '1':
            temperature_conversion = TemperatureConverter() # Instantiating TemperatureConverter object
            temperature_conversion.handle_temperature_conversion() # Calling the temperature conversion function
        elif choice == '2':
            mass_conversion = MassConverter() # Instantiating MassConverter object
            mass_conversion.handle_mass_conversion() # Calling the mass conversion function
        elif choice == '3':
            volume_conversion = VolumeConverter() # Instantiating VolumeConverter object
            volume_conversion.handle_volume_conversion # Calling the volume conversion function
        elif choice == '4':
            pressure_conversion = PressureConverter() # Instantiating PressureConverter object
            pressure_conversion.handle_pressure_conversion() # Calling the pressure conversion function
        elif choice == '5':
            molar_object = ChemistryCalculator() # Instantiating ChemistryCalculator object
            molar_object.handle_molar_mass_conversion() # Calling the molar mass conversion function
        elif choice == '6':
            concentration_calculations = ConcentrationCalculator(0.0, 0.0, 0.0) # Instantiating ConcentrationCalculator object; passing default values into the constructor; it's just how the constructor is instantiated
            concentration_calculations.handle_concentration_calculations() # Calling the molar mass conversion function
        elif choice == '7':
            print("Have a nice day! :)")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": # Checks if the module is being run directly or imported
    main()