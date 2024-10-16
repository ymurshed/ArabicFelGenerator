from ..Constants.Common import Common
from ..Constants.PastVerbIndicators import PastVerbIndicators

class PastVerbGenerator:
    def get_forms(self, root):
        suffixes = PastVerbIndicators.suffixes 

        # Remove the last char if present
        if root[-1] in (Common.KASRA + Common.FATHA + Common.DAMMA):
            root = root[:-1]
    
        # Generate conjugations
        conjugations = []
        for suffix in suffixes:
            conjugated = root + suffix
            conjugations.append(f"{conjugated}")
    
        return conjugations
