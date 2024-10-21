class ConcentrationCalculator:
    def __init__(self, solute_mass: float, solvent_mass: float, volume: float) -> None:
        self.solute_mass = solute_mass  # in grams
        self.solvent_mass = solvent_mass  # in grams
        self.volume = volume  # in liters

    def molarity(self, molar_mass: float) -> float:
        moles = self.solute_mass / molar_mass  # Calculate moles of solute
        return moles / self.volume  # Molarity = moles/volume (L)
    
    def molality(self, molar_mass: float) -> float:
        moles = self.solute_mass / molar_mass  # Calculate moles of solute
        return moles / (self.solvent_mass / 1000)  # Molality = moles/kg of solvent
    
    # I will deal with this later, do not touch this function
    # 
    # def normality(self, equivalence_factor: float, molar_mass: float) -> float:
    #     moles = self.solute_mass / molar_mass  # Calculate moles of solute
    #     equivalents = moles * equivalence_factor  # Calculate equivalents
    #     return equivalents / self.volume  # Normality = equivalents/volume (L)

    @staticmethod # This is a static function; not using any instance variables
    def handle_concentration_calculations() -> None:
        print() # Formatting reasons (when ran in cmd)
        solute_mass = float(input("Enter the mass of the solute (g): ")) # Used for molarity calculation
        solvent_mass = float(input("Enter the mass of the solvent (g): ")) # Used for molality calculation
        volume = float(input("Enter the volume of the solution (L): ")) # Used for molarity calculation
        molar_mass = float(input("Enter the molar mass of the solute (g/mol): ")) # Used for molarity and molality calculation
        concentration_object = ConcentrationCalculator(solute_mass, solvent_mass, volume)

        print(f"Molarity: {concentration_object.molarity(molar_mass)} M")
        print(f"Molality: {concentration_object.molality(molar_mass)} m")