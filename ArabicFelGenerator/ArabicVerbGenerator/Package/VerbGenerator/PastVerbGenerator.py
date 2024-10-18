from ..Constants.Bab import Bab
from ..Constants.Diacritic import Diacritic
from ..Constants.PastVerbIndicators import PastVerbIndicators

class PastVerbGenerator:
    def get_forms(self, root, bab_name):
        bab = Bab()
        root = bab.set_past_verb_aen_kalima(root, bab_name)

        #test
        for i in range(len(root)):
            print(root[i])

        # Remove the last diacritic char if present
        if root[-1] in (Diacritic.KASRA + Diacritic.FATHA + Diacritic.DAMMA):
            root = root[:-1]
    
        # Generate conjugations
        conjugations = []
        suffixes = PastVerbIndicators.suffixes 

        for i in range(len(suffixes)):
            if i == 0:
                conjugated = f"{root}{Diacritic.FATHA}{suffixes[i]}"
            else:
                conjugated = f"{root}{Diacritic.SUKUN}{suffixes[i]}"
            
            conjugations.append(f"{conjugated}")

        return conjugations
