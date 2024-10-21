from converter import Converter

class VolumeConverter(Converter):    
    # Gets conversion factor for volume units
    def get_conversion_factor(self, unit: str) -> float:
        conversion_factors = { # Instead of if statements, we'll utilize dictionary mapping
            "ml": 0.001,    # 1 mL = 0.001 L
            "l": 1.0,       # 1 L = 1 L
            "gal": 1000.0,  # 1 gal = 3.78541 L
            "cc": 453.592   # 1 cc = 0.001 L
        }

        if unit in conversion_factors:
            return conversion_factors[unit]
        else:
            raise ValueError(f"\nUnknown volume unit: {unit}.\nConvert to either mL, L, gal, or cc.")
    
    @staticmethod # This is a static function; not using any instance variables
    def handle_volume_conversion() -> None:
        volume_object = VolumeConverter()
        print() # Formatting reasons (when ran in cmd)
        value = float(input("Enter the volume value: "))
        from_unit = input("From unit (L/mL/gal/cc): ").lower()
        to_unit = input("To unit (L/mL/gal/cc): ").lower()

        result = volume_object.convert(value, from_unit, to_unit)
        print(f"Converted Volume: {result}")