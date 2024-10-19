class TemperatureConverter(): # Temperature conversions are relative so this class is written different from mass and volume

    # Convert temperature from one unit to anothewr
    def convert(self, value: float, from_unit: str, to_unit: str) -> str:
        if from_unit == to_unit:
            return f"{value} {to_unit}" # Returns the input since no conversion is required
            
        # Get temperature offsets for both units
        from_factor = self.get_temperature_conversion_factor(from_unit) # Need to collect which unit you're leaving behind
        to_factor = self.get_temperature_conversion_factor(to_unit) # Need to collect which unit you're arriving at

        # Convert to Celsius
        celsius_value = self.to_celsius(value, from_unit, from_factor)

        # Convert from Celsius to the target unit
        converted_value = self.from_celsius(celsius_value, to_unit, to_factor)

        return f"{converted_value} {to_unit}" # Returns the converted value for temperature
    
    def get_temperature_conversion_factor(self, unit: str) -> float:
        conversion_factors = { # Instead of if statements, we'll utilize dictionary mapping
            "C": 0,         # Celsius has no offset
            "F": 32,        # Fahrenheit offset
            "K": 273.15     # Kelvin offset
        }
        if unit in conversion_factors:
            return conversion_factors[unit]
        else:
            raise ValueError(f"\nUnknown temperature unit: {unit}.\nConvert to either C, F, or K.")
        
    def to_celsius(self, value: float, from_unit: str, from_factor: float) -> float:
        conversions = {
            "C": lambda v: v,                               # No adjustment required for Celsius
            "F": lambda v: (v - from_factor) * (5.0 / 9.0),  # Fahrenheit to Celsius
            "K": lambda v: v - from_factor                   # Kelvin to Celsius
        }
        return conversions[from_unit](value)
    
    def from_celsius(self, celsius_value: float, to_unit: str, to_factor: float) -> float:
        conversions = {
            "C": lambda v: v,                            # No adjustment required for Celsius
            "F": lambda v: (v * (9.0 / 5.0)) + to_factor, # Fahrenheit to Celsius
            "K": lambda v: v + to_factor                  # Kelvin to Celsius
        }
        return conversions[to_unit](celsius_value)
    
    @staticmethod # This is a static function; not using any instance variables
    def handle_temperature_conversion() -> None:
        temperature_object = TemperatureConverter()
        print() # Formatting reasons (when ran in cmd)
        value = float(input("Enter the temperature value: "))
        from_unit = input("From unit (C/F/K): ").upper()
        to_unit = input("To unit (C/F/K): ").upper()

        result = temperature_object.convert(value, from_unit, to_unit)
        print(f"Converted Temperature: {result}")