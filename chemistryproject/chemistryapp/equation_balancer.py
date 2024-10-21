import re
import csv
import sympy as sym


class EquationBalancer:
    def __init__(self): # Constructor, loads the CSV file
        self.elements = []
        self.load_elements("Periodic Table of Elements.csv")

    def load_elements(self, file_path: str) -> None: # Extracts csv File data
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # Skip the header
            for row in reader:
                symbol = row[2].strip() # Extract the symbol (3rd column)
                self.elements.append(symbol)

    def handle_equation_balancer(self):
        print()
        print("Enter an equation you would like to balance with no spaces")
        print("and no prefixes. Use (->) as the yeild arrow")
        equ = self.balance(input("Enter equation:"))
        print(f'Balanced equation is: {equ}')

    def balance(self, equation: str):
        # Checks that string is a valid equation
        if equation.count("->") != 1:
            print("Too many yeild arrows or no yeild arrows")
            return

        # Using re to make sure string contains only charcters it is supposed to contain
        # ^ asserts the start of the string, $ asserts the end of the string
        # [A-Za-z\d->], array of characters allowed in the string. A-Z, a-z, /d is all numbers, '-' and '>' and '+' and '(' and ')'
        # * indicates that the preceding character class can appear zero or more times, aka can be empty or full of those characters
        if not re.match("^[A-Za-z\d>+()-]*$", equation):
            print("Contains characters not allowed")
            return

        # Splits the equation into two strings, the products and the reactants
        reactants, products = equation.split("->")

        # Checks if either string are empty
        if not reactants or not products:
            print("Either no reactants or no products")
            return

        # Splits the products and reactants lists into arrays of each product and reactants
        reactants_list = reactants.split("+")
        products_list = products.split("+")

        # Get all elements

        list_of_elements_reactant = []
        for reactant in reactants_list:
            reactant = re.sub(r'[()]', '', reactant)

            pattern = '|'.join(sorted(self.elements, key=lambda x: -len(x)))  # Sort by length to match multi-letter elements first
            matches = re.findall(pattern, reactant)
            list_of_elements_reactant += matches

        list_of_elements_product = []
        for product in products_list:
            product = re.sub(r'[()]', '', product)

            pattern = '|'.join(sorted(self.elements, key=lambda x: -len(x)))  # Sort by length to match multi-letter elements first
            matches = re.findall(pattern, product)
            list_of_elements_product += matches
        
        # Removes dupes
        list_of_elements_reactant = list(set(list_of_elements_reactant))
        list_of_elements_product = list(set(list_of_elements_product))
        
        if set(list_of_elements_product) != set(list_of_elements_reactant):
            print("Elements in reactants and product do not match")
            return
        
        elements_list = list_of_elements_reactant

        # Make matrix for each element
        matrix = [[0] * (len(reactants_list) + len(products_list)) for _ in range(len(elements_list))]

        reactants_and_products = reactants_list + products_list
        products_index_start = len(reactants_list)
        for r_i, element in enumerate(elements_list):
            for index in range(len(matrix[0])):
                if element in reactants_and_products[index]:
                    count = self.element_count(reactants_and_products[index], element)[element]
                    if index >= products_index_start:
                        count *= -1
                    matrix[r_i][index] = count

        is_balanced = True
        for row in matrix:
            if sum(row) != 0:
                is_balanced = False
                break

        if is_balanced:
            return equation
        

        # Solve using Sympy for absolute-precision math
        matrix = sym.Matrix(matrix)    
        # find first basis vector == primary solution
        coefficients = matrix.nullspace()[0]    
        # find least common denominator, multiply through to convert to integer solution
        coefficients *= sym.lcm([term.q for term in coefficients])


        # Put coefficients back into the equation
        last_reactant = len(reactants_list)-1
        last_element = len(reactants_and_products)-1
        solution = ""
        for index, elem in enumerate(reactants_and_products):
            if index == last_reactant:
                end = "->"
            elif index != last_element:
                end = "+"
            else:
                end = ""

            coefficient = coefficients[index] if coefficients[index] != 1 else ""

            solution += f'{coefficient}{elem}{end}'
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