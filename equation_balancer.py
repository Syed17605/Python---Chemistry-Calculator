import re
import csv

from element import Element

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

    def balance(self, equation: str):
        formula = "C6H12O6"

        # Regular expression to find matches based on the elements list
        pattern = '|'.join(sorted(self.elements, key=lambda x: -len(x)))  # Sort by length to match multi-letter elements first
        matches = re.findall(pattern, formula)
        print(matches)

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

        print(f'Reactants list: {reactants_list}')
        print(f'Products list: {products_list}')

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

        #     list_of_chars = re.split('(\d+)', reactant)
        #     for char in list_of_chars:
        #         print(char)
        #         if re.match('.*[()]+.*', char):
        #             char = re.sub(r'[()]', '', char)
        #         if char.isdigit():
        #             continue
        #         if char == '':
        #             continue
        #         if char in self.elements:
        #             list_of_elements.append(char)
        #         else:
        #             print(f'{char} is not an element')
        #             #return

        # for product in products_list:
        #     list_of_chars = re.split('(\d+)', product)
        #     for char in list_of_chars:
        #         if char in self.elements:
        #             list_of_elements.append(char)
        
        # Removes dupes
        list_of_elements_reactant = list(set(list_of_elements_reactant))
        list_of_elements_product = list(set(list_of_elements_product))
        
        print(list_of_elements_reactant)
        print(list_of_elements_product)

        if set(list_of_elements_product) != set(list_of_elements_reactant):
            print("Elements in reactants and product do not match")
            return
        
        elements_list = list_of_elements_reactant
        print(elements_list)


        # Make matrix for each element
        matrix = [[0] * len(elements_list) for _ in range(len(elements_list))]
        print(matrix)



        # reactants_dict = {}
        # for reactant in reactants_list:
        #     count = 1
        #     if re.match('.*[()]+.*', reactant):
        #         print('has parenth')
        #         if reactant[-1].isdigit():
        #             count = int(reactant[-1])
        #             reactant = reactant[:-1]

        #         reactant = reactant[1:-1]
        #         print(reactant)
        #     print('no paranth')
        #     reactants_dict[reactant] = count
        #     print(reactants_dict)

        # for count, reactant in reactants_dict.items():
            
                




        # list_of_elements_before = {}
        # last_char = ''
        # for reactant in reactants_list:
        #     list_of_chars = re.split('(\d+)', reactant)
        #     for char in list_of_chars:
        #         if char.isdigit():
        #             list_of_elements_before[last_char] *= int(char) 
        #             continue
        #         if char in self.elements and char not in list_of_elements_before:
        #             list_of_elements_before[char] = 1
        #             last_char = char

        # list_of_elements_after = {}
        # last_char = ''
        # for product in products_list:
        #     list_of_chars = re.split('(\d+)', product)
        #     for char in list_of_chars:
        #         if char.isdigit():
        #             list_of_elements_after[last_char] *= int(char)
        #             continue
        #         if char in self.elements and char not in list_of_elements_after:
        #             list_of_elements_after[char] = 1
        #             last_char = char        
        
        
        # print(list_of_elements_before)
        # print(list_of_elements_after)

        # if list_of_elements_before.keys() != list_of_elements_after.keys():
        #     print("They no same")
        #     return

        # list_of_elements_before = dict(sorted(list_of_elements_before.items()))
        # list_of_elements_after = dict(sorted(list_of_elements_after.items()))

        # print(f'Before sorted: {list_of_elements_before}')
        # print(f'After Sorted: {list_of_elements_after}')

        # list_of_elements_before_balanced = list_of_elements_before.copy()
        # list_of_elements_after_balanced = list_of_elements_after.copy()

        # ite = 0
        # while True:
        #     for elem in list_of_elements_before_balanced:
        #         if list_of_elements_before_balanced[elem] == list_of_elements_after_balanced[elem]:
        #             continue
                
        #         if list_of_elements_before_balanced[elem] > list_of_elements_after_balanced[elem]:
        #             list_of_elements_after_balanced[elem] += list_of_elements_before_balanced[elem] - list_of_elements_after_balanced[elem]
                
        #         if list_of_elements_before_balanced[elem] < list_of_elements_after_balanced[elem]:
        #             list_of_elements_before_balanced[elem] += list_of_elements_after_balanced[elem] - list_of_elements_before_balanced[elem]

        #     if list_of_elements_before_balanced == list_of_elements_after_balanced:
        #         break
        #     ite += 1
        #     if ite > 10000:
        #         break

        # print(f'Before : {list_of_elements_before_balanced}')
        # print(f'After : {list_of_elements_after_balanced}')

        # # convert back to equation
        # # No balancing needed
        # if list_of_elements_after == list_of_elements_after_balanced:
        #     print(list_of_elements_after)
        #     print(list_of_elements_after_balanced)
        #     print("e")
        #     return equation

        # new_equ_b = ""
        # for index, elem in enumerate(list_of_elements_before):
        #     multiplier = int(list_of_elements_before_balanced[elem] / list_of_elements_before[elem])
        #     if multiplier == 1:
        #         multiplier = ""
        #     new_thing = f'{multiplier}{elem}{list_of_elements_before[elem]}'
        #     new_equ_b += new_thing
        #     if new_equ_b != len(list_of_elements_before)-1:
        #         new_equ_b += "+"

        # new_equ_a = ""
        # for index, elem in enumerate(list_of_elements_after):
        #     multiplier = int(list_of_elements_after_balanced[elem] / list_of_elements_after[elem])
        #     if multiplier == 1:
        #         multiplier = ""
        #     new_thing = f'{multiplier}{elem}{list_of_elements_after[elem]}'
        #     new_equ_a += new_thing
        #     if index != len(list_of_elements_after)-1:
        #         new_equ_a += "+"

        # return new_equ_b + "->" + new_equ_a

# {'H': 2, 'O': 2}
# After : {'H': 2, 'O': 2}







# Must enter with no spaces and correct capitalization
if __name__ == '__main__':
    equation_balancer = EquationBalancer()

    equation_balancer.balance("(H2)2+OH2->(H2O)")