class Element: # Will extend later for other variables
    def __init__(self, symbol: str, atomicMass: float): # Constructor
        self.symbol = symbol
        self.atomicMass = atomicMass
    
    def getSymbol(self) -> str:
        return self.symbol
    
    def getAtomicMass(self) -> float:
        return self.atomicMass