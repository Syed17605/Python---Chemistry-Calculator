from nicegui import ui

from converter import Converter

class MassConverter(Converter):    
    def __init__(self, container: ui.row) -> None:
        super().__init__(container)

    # Gets conversion factor for mass units
    def get_conversion_factor(self, unit: str) -> float:
        # If someone enters lb is still works
        unit = "lbs" if unit == "lb" else unit

        conversion_factors = { # Instead of if statements, we'll utilize dictionary mapping
            "mg": 0.001,    # 1 mg = 0.001 g
            "g": 1.0,       # 1 g = 1 g
            "kg": 1000.0,   # 1 kg = 1000.0 g
            "lbs": 453.592  # 1 lbs = 453.592 g
        }

        if unit in conversion_factors:
            return conversion_factors[unit]
        else:
            raise ValueError(f"\nUnknown mass unit: {unit}.\nConvert to either mg, g, kg, or lbs.")

    @staticmethod # This is a static function; not using any instance variables
    def handle_mass_conversion() -> None:
        mass_object = MassConverter()
        print() # Formatting reasons (when ran in cmd)
        value = float(input("Enter the mass value: "))
        from_unit = input("From unit (mg/kg/g/lbs): ").lower()
        to_unit = input("To unit (mg/kg/g/lbs): ").lower()

        result = mass_object.convert(value, from_unit, to_unit)
        print(f"Converted Mass: {result}")