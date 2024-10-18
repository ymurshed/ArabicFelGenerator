from Package.VerbGenerator.PastVerbGenerator import PastVerbGenerator
from Package.VerbGenerator.PresentVerbGenerator import PresentVerbGenerator

def main():
    print("Welcome to the arabic verb generator!")
    
    main_form = 'قَرَأَ'
    bab_name = 'فَتَحَ - يَفْتَحُ'

    past_verb_generator = PastVerbGenerator()
    past_forms = past_verb_generator.get_forms(main_form, bab_name)
    past_forms.insert(0, main_form)
    print(f"Possible Past Forms: {' | '.join(past_forms)}")

    present_verb_generator = PresentVerbGenerator()
    present_forms = present_verb_generator.get_forms(main_form)
    print(f"Possible Present/Future Forms: {' | '.join(present_forms)}")

if __name__ == "__main__":
    main()
