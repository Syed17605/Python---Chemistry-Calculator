class Element: # Will extend later for other variables
    def __init__(self, symbol: str, atomic_mass: float): # Constructor
        self.symbol = symbol
        self.atomic_mass = atomic_mass
    
    def get_symbol(self) -> str:
        return self.symbol
    
    def get_atomic_mass(self) -> float:
        return self.atomic_mass
