from Package.VerbGenerator.PastVerbGenerator import PastVerbGenerator
from Package.VerbGenerator.PresentVerbGenerator import PresentVerbGenerator

def main():
    print("Welcome to the arabic verb generator!")
    
    past_verb_generator = PastVerbGenerator()
    past_forms = past_verb_generator.get_forms('فَعَلَ')
    print(f"Possible Past Forms: {' | '.join(past_forms)}")

    present_verb_generator = PresentVerbGenerator()
    present_forms = present_verb_generator.get_forms('فَعَلَ')
    print(f"Possible Present/Future Forms: {' | '.join(present_forms)}")

if __name__ == "__main__":
    main()
