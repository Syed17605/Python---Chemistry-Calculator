import json
from nicegui import ui


# Class for a single unit containing the name, symbol, conversion formula to and from base unit
class Unit:
    def __init__(self, name: str, symbol: str, to_base: str, from_base: str) -> None:
        self.name = name
        self.symbol = symbol
        self.to_base = to_base
        self.from_base = from_base

    # Returns the string for textbox display
    def get_display(self) -> str:
        return f'{self.name} ({self.symbol})'
    
    # Returns the symbol
    def get_symbol(self) -> str:
        return self.symbol
    
    # Returns string that contains the formula to convert to base unit
    def get_to_base(self) -> str:
        return self.to_base
    
    # Returns string that contains the formula to convert from base unit
    def get_from_base(self) -> str:
        return self.from_base



# Converter class for each measurement; is expandable to more measurements or more units
class Converter():
    def __init__(self, container: ui.row, measurement: str="None") -> None:
        self.container = container # Container for the display
        self.measurement = measurement # Measurement being used
        self.start_unit: Unit = None # Starting unit
        self.start_value = 0.0 # Starting value
        self.end_unit: Unit = None # Ending unit
        self.end_value = 0.0 # Ending value/whats calculated
        self.end_value_label = None # UI label for calculated value
        self.base_unit = "" # Name of base unit
        
        # Gets data from json file
        with open('converter_info.json', 'r') as file:
            data = json.load(file)

        # Makes a dictionary of all measurements {Measurement : list of Units}
        units = {}
        for item in data:
            unit_type = item['unitType']
            units[unit_type] = [Unit(unit['name'], unit['symbol'], unit['toBase'], unit['fromBase']) for unit in item['units']]
            
            # Gets the base unit for the current measurement
            if unit_type == self.measurement:
                self.base_unit = item['baseUnit']
        
        # Dictionary of the units for the measurement {Unit Display : Unit}
        self.unit_map = {unit.get_display(): unit for unit in units[self.measurement]}

    # Convert one unit to another unit
    def convert(self):
        ui.notify("Converted", position="center")

        # Converts from start unit to end unit, skips conversion if they are the same
        if self.start_unit == self.end_unit:
            self.end_value = self.start_value
        else:
            x = eval(self.start_unit.get_to_base().replace("{x}", str(self.start_value)))
            self.end_value = eval(self.end_unit.get_from_base().replace("{x}", str(x)))

        # Removes current label from screen if there is one
        if self.end_value_label:
            self.container.remove(self.end_value_label)
        # Adds label to screen; limits decimal to 3 places
        with self.container:
            self.end_value_label = ui.label(f'Converted Value: {self.end_value:.3f} {self.end_unit.get_symbol()}')
    
    # Sets the starting unit
    def set_start_unit(self, start_unit_key: str):
        self.start_unit = self.unit_map[start_unit_key]
    
    # Sets the ending unit
    def set_end_unit(self, end_unit_key: str):
        self.end_unit = self.unit_map[end_unit_key]

    # Sets the starting value
    def set_start_value(self, start_value: float):
        self.start_value = start_value

    # Handles the conversion display
    def handle_conversion(self) -> None:
        # Clears the display
        self.container.clear()

        # Adds elements to the display
        with self.container:
            ui.label(f'Convert {self.measurement}: ')

            # Statring values elements
            with ui.column():
                ui.select(list(self.unit_map.keys()), label="From unit", with_input=True,
                          on_change=lambda e: self.set_start_unit(e.value))
                ui.number(label="From value", placeholder="1234", value=0.0, 
                          on_change=lambda e: self.set_start_value(e.value))
            
            # Converter button
            ui.button("Convert", on_click=lambda: self.convert())

            # Final value elements
            with ui.column():
                ui.select(list(self.unit_map.keys()), label="To unit", with_input=True,
                          on_change=lambda e: self.set_end_unit(e.value))