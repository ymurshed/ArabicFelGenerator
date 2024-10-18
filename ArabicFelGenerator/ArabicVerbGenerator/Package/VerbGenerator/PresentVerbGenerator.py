from ..Constants.Diacritic import Diacritic
from ..Constants.PresentVerbIndicators import PresentVerbIndicators

class PresentVerbGenerator:
    def get_forms(self, root):
        prefixes = PresentVerbIndicators.prefixes
        suffixes = PresentVerbIndicators.suffixes 

        # Replace the first diacritic char with SUKUN
        root = root[0] + Diacritic.SUKUN + root[2:]

        # Remove the last diacritic char if present
        if root[-1] in (Diacritic.KASRA + Diacritic.FATHA + Diacritic.DAMMA):
            root = root[:-1]
    
        # Generate conjugations
        conjugations = []

        for i in range(len(suffixes)):
            if i == 3:
                conjugated = f"{prefixes[i]}{root}{Diacritic.KASRA}{suffixes[i]}"
            else:
                conjugated = f"{prefixes[i]}{root}{suffixes[i]}"
            
            conjugations.append(f"{conjugated}")
    
        return conjugations
