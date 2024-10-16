from ..Constants.Common import Common
from ..Constants.PastVerbIndicators import PastVerbIndicators

class PastVerbGenerator:
    def get_forms(self, root):
        suffixes = PastVerbIndicators.suffixes 

        # Remove the last diacritic char if present
        if root[-1] in (Common.KASRA + Common.FATHA + Common.DAMMA):
            root = root[:-1]
    
        # Generate conjugations
        conjugations = []
        
        for i in range(len(suffixes)):
            if i == 0:
                conjugated = f"{root}{Common.FATHA}{suffixes[i]}"
            else:
                conjugated = f"{root}{Common.SUKUN}{suffixes[i]}"
            
            conjugations.append(f"{conjugated}")

        return conjugations
