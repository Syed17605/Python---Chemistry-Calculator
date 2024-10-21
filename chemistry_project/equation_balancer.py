import re
import csv
import sympy as sym
import numpy as np


class EquationBalancer:
    def __init__(self): # Constructor, loads the CSV file
        self.equation = "" # Current equation
        self.elements = [] # Elements in current equation
        self.coefficients = [] # Array of the coefficients
        self.all_elements = []
        self.load_elements("Periodic Table of Elements.csv")

    def load_elements(self, file_path: str) -> None: # Extracts csv File data
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # Skip the header
            for row in reader:
                symbol = row[2].strip() # Extract the symbol (3rd column)
                self.all_elements.append(symbol)

    # Used for output and input, can change if you want it to look different
    def handle_equation_balancer(self):
        print()
        print("Enter an equation you would like to balance with no spaces")
        print("and no prefixes. Use (->) as the yeild arrow")
        self.equation = input("Enter equation:")
        self.balanced_equation = self.balance()
        print(f'Balanced equation is: {self.balanced_equation}')

    # Returns true if its a valid equation
    def is_valid(self) -> bool:
        # Checks that string is a valid equation
        if self.equation.count("->") != 1:
            print("Too many yeild arrows or no yeild arrows")
            return False

        # Using re to make sure string contains only charcters it is supposed to contain
        # ^ asserts the start of the string, $ asserts the end of the string
        # [A-Za-z\d->], array of characters allowed in the string. A-Z, a-z, /d is all numbers, '-' and '>' and '+' and '(' and ')'
        # * indicates that the preceding character class can appear zero or more times, aka can be empty or full of those characters
        if re.search(r'[^A-Za-z0-9->+()]', self.equation) is not None:
            print("Contains characters not allowed")
            return False

        # Splits the equation into two strings, the products and the reactants
        reactants, products = self.equation.split("->")

        # Checks if either string are empty
        if not reactants or not products:
            print("Either no reactants or no products")
            return False
        
        self.reactants_list = reactants.split("+")
        self.products_list = products.split("+")
        self.reactants_and_products = self.reactants_list + self.products_list
        self.last_reactant = len(self.reactants_list)-1
        return True
        
    # Returns false if elements in products and reactants dont match
    def find_elements(self) -> bool:
         # Get all elements
        reactant_elements = []
        product_elements = []

        for index, compound in enumerate(self.reactants_and_products):
            compound = re.sub(r'[()]', '', compound)

            pattern = '|'.join(sorted(self.all_elements, key=lambda x: -len(x)))  # Sort by length to match multi-letter elements first
            matches = re.findall(pattern, compound)
            if index <= self.last_reactant:
                reactant_elements += matches
            else:
                product_elements += matches

        if set(product_elements) != set(reactant_elements):
            print("Elements in reactants and product do not match")
            return False
        
        self.elements = list(set(reactant_elements))
        return True
    
    # Returns true if equation is already balanced
    def get_coefficients(self) -> bool:
         # Make matrix for each element
        matrix = [[0] * (len(self.reactants_list) + len(self.products_list)) for _ in range(len(self.elements))]

        for row_index, element in enumerate(self.elements):
            for index in range(len(matrix[0])):
                if element in self.reactants_and_products[index]:
                    count = self.element_count(self.reactants_and_products[index], element)[element]
                    if index >= self.last_reactant+1:
                        count *= -1
                    matrix[row_index][index] = count

        matrix = np.array(matrix)

        row_sums = np.sum(matrix, axis=1)
        if np.all(row_sums==0):
            return True

        # Solve using Sympy for absolute-precision math
        matrix = sym.Matrix(matrix)    
        # find first basis vector == primary solution
        self.coefficients = matrix.nullspace()[0]    
        # find least common denominator, multiply through to convert to integer solution
        self.coefficients *= sym.lcm([term.q for term in self.coefficients])
        return False

    # Balances the equation
    def balance(self) -> str:
        # Check if equation is a valid equation and splits the reactants and products
        if not self.is_valid():
            return ""

        # Get all elements
        if not self.find_elements():
            return ""
        
        # Returns if already balanced
        if self.get_coefficients():
            return self.equation


        # Put coefficients back into the equation
        solution = ""
        for index, compound in enumerate(self.reactants_and_products):
            if index == self.last_reactant:
                end = "->"
            elif index != len(self.reactants_and_products)-1:
                end = "+"
            else:
                end = ""

            coefficient = self.coefficients[index] if self.coefficients[index] != 1 else ""

            solution += f'{coefficient}{compound}{end}'
        return solution
    
    def element_count(self, formula, elem):
        # \([A-Za-z\d]+\)\d* matches anything in parantheses plus the number following it
        # [A-Z][a-z]?\d*) matches any element not in parenthesis
        pattern = r'(\([A-Za-z\d]+\)\d*|[A-Z][a-z]?\d*)'
        # This is a list of each indicidual element, or the group in paranthesis like (H2)2 for example
        tokens = re.findall(pattern, formula)

        element_counts = {}

        for token in tokens:
            if elem in token:
                if token.startswith('('):
                    # using (H2)2 as example, inner_formula would be H2 and count would be 2
                    inner_formula, count = re.match(r'\((.*?)\)(\d*)', token).groups()
                    count = int(count) if count else 1 # count could be nothing ex. (H2O), no value after paranthesis

                    # recusivly get the inner counts
                    inner_counts = self.element_count(inner_formula, elem)

                    # gets the actual count by multiplying outside by inside. ex. (H2)2 would be 4 bc 2 * 2
                    for element, inner_count in inner_counts.items():
                        element_counts[element] = element_counts.get(element, 0) + inner_count * count
                else:
                    element, count = re.match(r'([A-Z][a-z]*)(\d*)', token).groups()
                    count = int(count) if count else 1
                    element_counts[element] = element_counts.get(element, 0) + count

        return element_counts