from ..Constants.Common import Common
from ..Constants.PresentVerbIndicators import PresentVerbIndicators

class PresentVerbGenerator:
    def get_forms(self, root):
        prefixes = PresentVerbIndicators.prefixes
        suffixes = PresentVerbIndicators.suffixes 

        # Remove the last char if present
        if root[-1] in (Common.KASRA + Common.FATHA + Common.DAMMA):
            root = root[:-1]
    
        # Generate conjugations
        conjugations = []
        for i in range(len(suffixes)):
            conjugated = f"{prefixes[i]}{root}{suffixes[i]}"
            conjugations.append(f"{conjugated}")
    
        return conjugations
