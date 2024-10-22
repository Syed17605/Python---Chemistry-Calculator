from nicegui import ui

from temperature_converter import TemperatureConverter
from mass_converter import MassConverter
from volume_converter import VolumeConverter
from pressure_converter import PressureConverter
from chemistry_calculator import ChemistryCalculator
from concentration_calculator import ConcentrationCalculator
from equation_balancer import EquationBalancer

# Simple display class
class Display():
    # Inits all objects and then displays menu
    def __init__(self):
        self.temperature_converter = TemperatureConverter()
        self.mass_converter = MassConverter()
        self.volume_converter = VolumeConverter()
        self.pressure_converter = PressureConverter()
        self.molar_calculator = ChemistryCalculator()
        self.concentration_calculator = ConcentrationCalculator(0.0,0.0,0.0)
        self.equation_balancer = EquationBalancer()
        self.display_menu()

    # Displays menu and buttons all working
    # When button is clicked it runs the code associated with said button
    # This still occurs in console but will convert to gui
    def display_menu(self):
        ui.label("What would you like to do?")
        with ui.button_group():
            ui.button(text="Convert Temperature", on_click=lambda: self.temperature_converter.handle_temperature_conversion())
            ui.button(text="Convert Mass", on_click=lambda: self.mass_converter.handle_mass_conversion())
            ui.button(text="Convert Volume", on_click=lambda: self.volume_converter.handle_volume_conversion())
            ui.button(text="Convert Pressure", on_click=lambda: self.pressure_converter.handle_pressure_conversion())
            ui.button(text="Convert Mass and Molar Mass", on_click=lambda: self.molar_calculator.handle_molar_mass_conversion())
            ui.button(text="Molarity Calculations", on_click=lambda: self.concentration_calculator.handle_concentration_calculations())
            ui.button(text="Equation Balancer", on_click=lambda: self.equation_balancer.handle_equation_balancer())
        self.choice_container = ui.row()