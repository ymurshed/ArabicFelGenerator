from ..Constants.Diacritic import Diacritic

class Bab:
    FATAHA_YAFTAHU       = "فَتَحَ - يَفْتَحُ"
    NASARA_YANSURU       = "نَصَرَ- يَنْصُرُ"
    DARABA_YADRIBU       = "ضَرَبَ - يَضْرِبُ"
    SAMIA_YASMAU         = "سَمِعَ - يَسْمَعُ"

    def set_past_verb_aen_kalima(self, root, bab_name):
        # 3 character root 
        if len(root) == 6: 
            match bab_name:
                case Bab.FATAHA_YAFTAHU:
                   root = root[0:3] + Diacritic.FATHA + root[4:6]

                case Bab.NASARA_YANSURU:
                    root = root[0:3] + Diacritic.FATHA + root[4:6]

                case Bab.DARABA_YADRIBU:
                    root = root[0:3] + Diacritic.FATHA + root[4:6]

                case Bab.SAMIA_YASMAU:
                    root = root[0:3] + Diacritic.KASRA + root[4:6]
        return root