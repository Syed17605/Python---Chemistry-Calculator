from enum import Enum
import re
import periodictable
from nicegui import ui

# Enum for which button is pressed
class Selection(Enum):
    MASS_TO_MOLES = 1
    MOLES_TO_MASS = 2
    GET_MASS = 3


class ChemistryCalculator:
    def __init__(self, container: ui.row) -> None:
        self.container = container # Container for screen display
        self.moles = 0.0 # Number of moles
        self.mass = 0.0 # Mass in grams
        self.formula = "" # Chemical formula
        self.result_label = None # Product ui label
        # self.selcetion_ui = None # Selection ui row
        self.elements = {element.symbol: element for element in periodictable.elements} # All elements in periodic table

        # {Slection: (input_message, update_function, button_message, end_unit, calculation_function)}
        self.selection_map = { # Map for each enum to values written as a tuple
            Selection.MASS_TO_MOLES: ("Mass (g)", self.update_mass, "Convert", ' mol', self.calculate_mass_to_moles),
            Selection.MOLES_TO_MASS: ("Number of Moles", self.update_moles, "Convert", ' grams', self.calculate_moles_to_mass),
            Selection.GET_MASS: ("", None, "Get Mass", ' g/mol', self.calculate_molar_mass)
        }

    def mass_to_moles(self):
        if self.result_label is not None:
             self.result_label = None
        self.chemistry_ui(Selection.MASS_TO_MOLES)

    def moles_to_mass(self):
        if self.result_label is not None:
             self.result_label = None
        self.chemistry_ui(Selection.MOLES_TO_MASS)

    def molar_mass(self):
        if self.result_label is not None:
             self.result_label = None
        self.chemistry_ui(Selection.GET_MASS)

    # Handles the ui for each button
    def chemistry_ui(self, selection: Selection) -> None:
        # Clears selction display
        self.container.clear()

        # Gets variables from dictionary
        number_input_message, number_function, button_message = self.selection_map.get(selection)[:-2]

        # Adds elements to selection display
        with self.container:
            ui.input(label="Chemical Formula", placeholder="ex. CO2, H2O",
                     on_change=lambda e: self.update_formula(e.value))
            
            if selection != Selection.GET_MASS:
                ui.number(label=number_input_message, placeholder="1234",
                          on_change=lambda e: number_function(e.value))
                
            ui.button(button_message, on_click=lambda: self.calculate(selection))

    # Handles the calculations
    def calculate(self, selection: Selection):
        # Gets variables from dictionary
        unit, calculate_function = self.selection_map.get(selection)[-2:]

        # Calculates result
        result = calculate_function()
        result_message =  f'{result}' + unit

        # Removes current label from screen if there is one
        if self.result_label is not None:
            self.container.remove(self.result_label)
        # Adds label to screen; limits decimal to 3 places
        with self.container:
            self.result_label = ui.label(result_message)

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
    
     # Updates formula variable
    def update_formula(self, formula: str):
        self.formula = formula

    # Updates moles variable
    def update_moles(self, moles: float):
        self.moles = moles

    # Updates mass variable
    def update_mass(self, mass: float):
        self.mass = mass

    # Returns moles of given mass and formula
    def calculate_mass_to_moles(self):
        return self.mass / self.get_molar_mass()
    
    # Returns mass of given moles and formula
    def calculate_moles_to_mass(self): 
        return self.moles * self.get_molar_mass()

    # Returns molar mass of given formula
    def calculate_molar_mass(self):
        return self.get_molar_mass()