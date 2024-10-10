from abc import ABC, abstractmethod

class Converter(ABC):

    def convert(self, value: float, from_unit: str, to_unit: str) -> str:
        from_factor = self.get_conversion_factor(from_unit) # Need to collect which unit you're leaving behind
        to_factor = self.get_conversion_factor(to_unit) # Need to collect which unit you're arriving at
        return f"{value * (from_factor / to_factor)} {to_unit}" # Returns the converted value

    # Gets conversion factor for units
    @abstractmethod
    def get_conversion_factor(self, unit: str) -> float:
        pass