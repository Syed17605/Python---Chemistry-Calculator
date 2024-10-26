from nicegui import ui

from converter import Converter
from chemistry_calculator import ChemistryCalculator
from concentration_calculator import ConcentrationCalculator
from equation_balancer import EquationBalancer

# Simple display class
class Display():
    # Inits all objects and then displays menu
    def __init__(self):
        self.display_container = ui.column()
        self.choice_container = ui.row()
        self.temperature_converter = Converter(self.choice_container, "Temperature")
        self.mass_converter = Converter(self.choice_container, "Mass")
        self.volume_converter = Converter(self.choice_container, "Volume")
        self.pressure_converter = Converter(self.choice_container, "Pressure")
        self.molar_calculator = ChemistryCalculator(self.choice_container) # Need to do
        self.concentration_calculator = ConcentrationCalculator(self.choice_container) # Need to do
        self.equation_balancer = EquationBalancer(self.choice_container)
        self.display_menu()

    # Displays menu and buttons all working
    # When button is clicked it runs the code associated with said button
    # This still occurs in console but will convert to gui
    def display_menu(self):
        with self.display_container:
            ui.label("What would you like to do?")
            with ui.button_group():
                ui.button(text="Convert Temperature", on_click=lambda: self.temperature_converter.handle_conversion())
                ui.button(text="Convert Mass", on_click=lambda: self.mass_converter.handle_conversion())
                ui.button(text="Convert Volume", on_click=lambda: self.volume_converter.handle_conversion())
                ui.button(text="Convert Pressure", on_click=lambda: self.pressure_converter.handle_conversion())
                ui.button(text="Convert Mass and Molar Mass", on_click=lambda: self.molar_calculator.handle_molar_mass_conversion())
                ui.button(text="Molarity Calculations", on_click=lambda: self.concentration_calculator.handle_concentration_calculations())
                ui.button(text="Equation Balancer", on_click=lambda: self.equation_balancer.handle_equation_balancer())
            self.choice_container