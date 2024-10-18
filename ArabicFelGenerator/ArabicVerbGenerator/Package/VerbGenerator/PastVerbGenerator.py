from ..Constants.Diacritic import Diacritic
from ..Constants.PastVerbIndicators import PastVerbIndicators

class PastVerbGenerator:
    def get_forms(self, root):
        suffixes = PastVerbIndicators.suffixes 

        # Remove the last diacritic char if present
        if root[-1] in (Diacritic.KASRA + Diacritic.FATHA + Diacritic.DAMMA):
            root = root[:-1]
    
        # Generate conjugations
        conjugations = []
        
        for i in range(len(suffixes)):
            if i == 0:
                conjugated = f"{root}{Diacritic.FATHA}{suffixes[i]}"
            else:
                conjugated = f"{root}{Diacritic.SUKUN}{suffixes[i]}"
            
            conjugations.append(f"{conjugated}")

        return conjugations
