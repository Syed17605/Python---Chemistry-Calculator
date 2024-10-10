class VolumeConverter:
    # Convert volume from one unit to another
    def convert(self, value: float, from_unit: str, to_unit: str) -> str:
        from_factor = self.get_volume_conversion_factor(from_unit) # Need to collect which unit you're leaving behind
        to_factor = self.get_volume_conversion_factor(to_unit) # Need to collect which unit you're arriving at
        return f"{value * (from_factor / to_factor)} {to_unit}" # Returns the converted value for volume
    
    # Gets conversion factor for volume units
    def get_volume_conversion_factor(self, unit: str) -> float:
        conversion_factors = { # Instead of if statements, we'll utilize dictionary mapping
            "mL": 0.001,    # 1 mL = 0.001 L
            "L": 1.0,       # 1 L = 1 L
            "gal": 1000.0,  # 1 gal = 3.78541 L
            "cc": 453.592   # 1 cc = 0.001 L
        }

        if unit in conversion_factors:
            return conversion_factors[unit]
        else:
            raise ValueError(f"\nUnknown volume unit: {unit}.\nConvert to either mL, L, gal, or cc.")