class VolumeConverter:
    # Convert volume from one unit to another
    def convert(self, value: float, fromUnit: str, toUnit: str) -> str:
        fromFactor = self.getVolumeConversionFactor(fromUnit) # Need to collect which unit you're leaving behind
        toFactor = self.getVolumeConversionFactor(toUnit) # Need to collect which unit you're arriving at
        return f"{value * (fromFactor / toFactor)} {toUnit}" # Returns the converted value for volume
    
    # Gets conversion factor for volume units
    def getVolumeConversionFactor(self, unit: str) -> float:
        conversionFactors = { # Instead of if statements, we'll utilize dictionary mapping
            "mL": 0.001,    # 1 mL = 0.001 L
            "L": 1.0,       # 1 L = 1 L
            "gal": 1000.0,  # 1 gal = 3.78541 L
            "cc": 453.592   # 1 cc = 0.001 L
        }

        if unit in conversionFactors:
            return conversionFactors[unit]
        else:
            raise ValueError(f"\nUnknown volume unit: {unit}.\nConvert to either mL, L, gal, or cc.")