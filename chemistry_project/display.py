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
        self.main_button_group = ui.button_group()
        self.converters_button_group = ui.button_group()
        self.choice_container = ui.row()
        self.temperature_converter = Converter(self.choice_container, "Temperature")
        self.mass_converter = Converter(self.choice_container, "Mass")
        self.volume_converter = Converter(self.choice_container, "Volume")
        self.pressure_converter = Converter(self.choice_container, "Pressure")
        self.molar_calculator = ChemistryCalculator(self.choice_container) # make similar to converters
        self.concentration_calculator = ConcentrationCalculator(self.choice_container) # Need to do
        self.equation_balancer = EquationBalancer(self.choice_container)
        self.display_menu()

    # Displays menu and buttons all working
    # When button is clicked it runs the code associated with said button
    # This still occurs in console but will convert to gui
    def display_menu(self):
        with self.display_container:
            ui.label("What would you like to do?")
            with self.main_button_group:
                ui.button(text="Convert", on_click=lambda: self.converters())
                ui.button(text="Moles and Molar Mass", on_click=lambda: self.molar_mass_conversion())
                ui.button(text="Molarity Calculations")#, on_click=lambda: self.concentration_calculation())
                ui.button(text="Equation Balancer", on_click=lambda: self.equation_balancing())
            self.converters_button_group
            self.choice_container

    def converters(self):
        self.converters_button_group.clear()
        self.choice_container.clear()
        with self.converters_button_group:
            ui.button(text="Convert Temperature", on_click=lambda: self.temperature_converter.handle_conversion())
            ui.button(text="Convert Mass", on_click=lambda: self.mass_converter.handle_conversion())
            ui.button(text="Convert Volume", on_click=lambda: self.volume_converter.handle_conversion())
            ui.button(text="Convert Pressure", on_click=lambda: self.pressure_converter.handle_conversion())
    
    def molar_mass_conversion(self):
        self.converters_button_group.clear()
        self.choice_container.clear()
        with self.converters_button_group:
            ui.button("Get Molar Mass", on_click=lambda: self.molar_calculator.molar_mass())
            ui.button("Convert Moles to Mass", on_click=lambda: self.molar_calculator.moles_to_mass())
            ui.button("Convert Mass to Moles", on_click=lambda: self.molar_calculator.mass_to_moles())
            
    
    def concentration_calculation(self):
        self.converters_button_group.clear()
        self.concentration_calculator.handle_concentration_calculations()

    def equation_balancing(self):
        self.converters_button_group.clear()
        self.equation_balancer.handle_equation_balancer()