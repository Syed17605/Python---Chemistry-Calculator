class TemperatureConverter: # Temperature conversions are relative so this class is written different from mass and volume

    # Convert temperature from one unit to anothewr
    def convert(self, value: float, fromUnit: str, toUnit: str) -> str:
        if fromUnit == toUnit:
            return f"{value} {toUnit}" # Returns the input since no conversion is required
        
        fromFactor = self.getTemperatureConversionFactor(fromUnit) # Need to collect which unit you're leaving behind
        toFactor = self.getTemperatureConversionFactor(toUnit) # Need to collect which unit you're arriving at
    
        # Get temperature offsets for both units
        fromFactor = self.getTemperatureConversionFactor(fromUnit) # Need to collect which unit you're leaving behind
        toFactor = self.getTemperatureConversionFactor(toUnit) # Need to collect which unit you're arriving at

        # Convert to Celsius
        celsiusValue = self.toCelsius(value, fromUnit, fromFactor)

        # Convert from Celsius to the target unit
        convertedValue = self.fromCelsius(celsiusValue, toUnit, toFactor)

        return f"{convertedValue} {toUnit}" # Returns the converted value for temperature
    
    def getTemperatureConversionFactor(self, unit: str) -> float:
        conversionFactors = { # Instead of if statements, we'll utilize dictionary mapping
            "C": 0,         # Celsius has no offset
            "F": 32,        # Fahrenheit offset
            "K": 273.15     # Kelvin offset
        }
        if unit in conversionFactors:
            return conversionFactors[unit]
        else:
            raise ValueError(f"\nUnknown temperature unit: {unit}.\nConvert to either C, F, or K.")
        
    def toCelsius(self, value: float, fromUnit: str, fromFactor: float) -> float:
        conversions = {
            "C": lambda v: v,                               # No adjustment required for Celsius
            "F": lambda v: (v - fromFactor) * (5.0 / 9.0),  # Fahrenheit to Celsius
            "K": lambda v: v - fromFactor                   # Kelvin to Celsius
        }
        return conversions[fromUnit](value)
    
    def fromCelsius(self, celsiusValue: float, toUnit: str, toFactor: float) -> float:
        conversions = {
            "C": lambda v: v,                            # No adjustment required for Celsius
            "F": lambda v: (v * (9.0 / 5.0)) + toFactor, # Fahrenheit to Celsius
            "K": lambda v: v + toFactor                  # Kelvin to Celsius
        }
        return conversions[toUnit](celsiusValue)