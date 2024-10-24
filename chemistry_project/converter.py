import json
from nicegui import ui

class Unit:
    def __init__(self, name: str, symbol: str, conversion: float) -> None:
        self.name = name
        self.symbol = symbol
        self.conversion_factor = conversion

    def get_display(self) -> str:
        return f'{self.name} ({self.symbol})'
    
    def get_conversion_factor(self) -> float:
        return self.conversion_factor
    
    def get_symbol(self) -> str:
        return self.symbol


class Converter():
    def __init__(self, container: ui.row, measurement: str="None") -> None:
        self.container = container
        self.measurement = measurement
        self.end_unit: Unit = None
        self.start_value = 0.0
        self.start_unit: Unit = None
        self.end_value = 0.0
        self.units_map = {}
        self.end_value_label = None
        
        with open('converter_info.json', 'r') as file:
            data = json.load(file)

        units = {}
        for item in data:
            units[item['unitType']] = [Unit(unit['Name'], unit['Symbol'], unit['Conversion']) for unit in item['units']]
        
        self.unit_map = {unit.get_display(): unit for unit in units[self.measurement]}

    # Convert one unit to another unit
    def convert(self):
        ui.notify("Converted", position="center")
        from_factor = self.start_unit.get_conversion_factor()
        to_factor = self.end_unit.get_conversion_factor()
        self.start_value = self.end_value * (from_factor / to_factor)
        if self.end_value_label:
            self.container.remove(self.end_value_label)
        # Adds label to screen
        with self.container:
            self.end_value_label = ui.label(f'Converted Value: {self.start_value} {self.end_unit.get_symbol()}')
    
    def set_start_unit(self, start_unit_key: str):
        self.start_unit = self.unit_map[start_unit_key]
    
    def set_end_unit(self, end_unit_key: str):
        self.end_unit = self.unit_map[end_unit_key]

    def set_start_value(self, end_value: float):
        self.end_value = end_value

    def handle_conversion(self) -> None:
        self.container.clear()
        with self.container:
            ui.label(f'Convert {self.measurement}: ')
            with ui.column():
                ui.select(list(self.unit_map.keys()), label="From unit", with_input=True,
                          on_change=lambda e: self.set_start_unit(e.value))
                ui.number(label="From value", placeholder="1234", value=0.0, 
                          on_change=lambda e: self.set_start_value(e.value))
            ui.button("Convert", on_click=lambda: self.convert())
            with ui.column():
                ui.select(list(self.unit_map.keys()), label="To unit", with_input=True,
                          on_change=lambda e: self.set_end_unit(e.value))