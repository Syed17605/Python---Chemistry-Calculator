class MassConverter:
    # Convert mass from one unit to another
    def convert(self, value: float, from_unit: str, to_unit: str) -> str:
        from_factor = self.get_mass_conversion_factor(from_unit) # Need to collect which unit you're leaving behind
        to_factor = self.get_mass_conversion_factor(to_unit) # Need to collect which unit you're arriving at
        return f"{value * (from_factor / to_factor)} {to_unit}" # Returns the converted value for mass
    
    # Gets conversion factor for mass units
    def get_mass_conversion_factor(self, unit: str) -> float:
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