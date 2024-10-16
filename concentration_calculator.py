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