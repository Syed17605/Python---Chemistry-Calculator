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