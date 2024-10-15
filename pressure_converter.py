from converter import Converter

class PressureConverter(Converter):
    # Gets conversion factor for pressure units
    def get_conversion_factor(self, unit: str) -> float:
        conversion_factors = { # Instead of if statements, we'll utilize dictionary mapping
            "pa": 0.0075,   # 1 Pa = 0.0075 mmHg, the "p" is lowercase as well since in the main() file we're lowering all string inputs
            "atm": 760.0,   # 1 atm = 760.0 mmHg
            "mmhg": 1.0,    # 1 mmHg = 1 mmHg, the "h" has to be lowercase since in the main() file we're lowering all string inputs
            "inhg": 25.4,   # 1 inHg = 25.4 mmHg, the "h" has to be lowercase since in the main() file we're lowering all string inputs
            "torr": 1       # 1 torr = 1 mmHg
        }

        if unit in conversion_factors:
            return conversion_factors[unit]
        else:
            raise ValueError(f"\nUnknown pressure unit: {unit}.\nConvert to either Pa, atm, mmHg, inHg, or torr.")