class MassConverter:
    # Convert mass from one unit to another
    def convert(self, value: float, fromUnit: str, toUnit: str) -> str:
        fromFactor = self.getMassConversionFactor(fromUnit) # Need to collect which unit you're leaving behind
        toFactor = self.getMassConversionFactor(toUnit) # Need to collect which unit you're arriving at
        return f"{value * (fromFactor / toFactor)} {toUnit}" # Returns the converted value for mass
    
    # Gets conversion factor for mass units
    def getMassConversionFactor(self, unit: str) -> float:
        conversionFactors = { # Instead of if statements, we'll utilize dictionary mapping
            "mg": 0.001,    # 1 mg = 0.001 g
            "g": 1.0,       # 1 g = 1 g
            "kg": 1000.0,   # 1 kg = 1000.0 g
            "lbs": 453.592  # 1 lbs = 453.592 g
        }

        if unit in conversionFactors:
            return conversionFactors[unit]
        else:
            raise ValueError(f"\nUnknown mass unit: {unit}.\nConvert to either mg, g, kg, or lbs.")