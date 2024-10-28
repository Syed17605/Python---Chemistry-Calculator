from enum import Enum
import re
import periodictable
from nicegui import ui


class Selection(Enum):
    MASS_TO_MOLES = 1
    MOLES_TO_MASS = 2
    GET_MASS = 3


class ChemistryCalculator:
    def __init__(self, container: ui.row):
        self.container = container
        self.moles = 0.0
        self.mass = 0.0
        self.formula = ""
        self.end_value_label = None
        self.selcetion_ui = None
        self.elements = {element.symbol: element for element in periodictable.elements}
        self.selection_map = {
            Selection.MASS_TO_MOLES: ("Mass (g)", self.update_mass, "Convert", f'Moles in {self.moles} grams of {self.formula} is ', ' mol', self.calculate_mass_to_moles),
            Selection.MOLES_TO_MASS: ("Number of Moles", self.update_moles, "Convert", f'Mass of {self.moles} moles of {self.formula} is ', ' grams', self.calculate_moles_to_mass),
            Selection.GET_MASS: ("", None, "Get Mass", f'Molar Mass of {self.formula} is ', ' g/mol', self.calculate_molar_mass)
        }

    def update_formula(self, formula: str):
        self.formula = formula

    def update_moles(self, moles: float):
        self.moles = moles

    def update_mass(self, mass: float):
        self.mass = mass

    def chemistry_ui(self, selection: Selection):
        self.selcetion_ui.clear()

        number_input_message, number_function, button_message = self.selection_map.get(selection)[:-3]

        with self.selcetion_ui:
            ui.input(label="Chemical Formula", placeholder="ex. CO2, H2O",
                     on_change=lambda e: self.update_formula(e.value))
            
            if selection != Selection.GET_MASS:
                ui.number(label=number_input_message, placeholder="1234",
                          on_change=lambda e: number_function(e.value))
                
            ui.button(button_message, on_click=lambda: self.button_function(selection))

        
    def button_function(self, selection: Selection): # UI WORKS BUT PRINTS 0.0 FOR EVERY VARIABLE
        end_label_message_start, end_label_message_end, calculate_method = self.selection_map.get(selection)[-3:]

        final_value = calculate_method()
        end_label_message = end_label_message_start + f'{final_value}' + end_label_message_end

        # Removes current label from screen if there is one
        if self.end_value_label:
            self.container.remove(self.end_value_label)
        # Adds label to screen; limits decimal to 3 places
        with self.container:
            self.end_value_label = ui.label(end_label_message)

    def calculate_mass_to_moles(self):
        return self.mass / self.get_molar_mass()
    
    def calculate_moles_to_mass(self): 
        return self.moles * self.get_molar_mass()

    def calculate_molar_mass(self):
        return self.get_molar_mass()

     # Gets the molar mass of a chemical compound
    def get_molar_mass(self) -> float:
        pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
        molar_mass = 0.0

        for match in pattern.finditer(self.formula):
            element_symbol = match.group(1)
            count_str = match.group(2)
            count = int(count_str) if count_str else 1 # Count the number of times a specific element appears

            element = self.elements.get(element_symbol)
            if element is None:
                raise ValueError(f"Element with symbol '{element_symbol}' not found.")
            molar_mass += element.mass * count

        return molar_mass
    
    def handle_molar_mass_conversion(self) -> None:
        self.container.clear()
        with self.container:
            with ui.button_group():
                ui.button("Get Molar Mass", on_click=lambda: self.chemistry_ui(Selection.GET_MASS))
                ui.button("Convert Moles to Mass", on_click=lambda: self.chemistry_ui(Selection.MOLES_TO_MASS))
                ui.button("Convert Mass to Moles", on_click=lambda: self.chemistry_ui(Selection.MASS_TO_MOLES))
            self.selcetion_ui = ui.row()