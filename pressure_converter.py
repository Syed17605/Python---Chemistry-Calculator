from converter import Converter

class PressureConverter(Converter):
    # Gets conversion factor for pressure units
    def get_conversion_factor(self, unit: str) -> float:
        conversion_factors = { # Instead of if statements, we'll utilize dictionary mapping
            "pa": 0.0075,   # 1 Pa = 0.0075 mmHg
            "atm": 760.0,   # 1 atm = 760.0 mmHg
            "mmhg": 1.0,    # 1 mmHg = 1 mmHg
            "inhg": 25.4,   # 1 inHg = 25.4 mmHg
            "torr": 1       # 1 torr = 1 mmHg
        }

        if unit in conversion_factors:
            return conversion_factors[unit]
        else:
            raise ValueError(f"\nUnknown mass unit: {unit}.\nConvert to either pa, atm, mmhg, inhg, or torr.")