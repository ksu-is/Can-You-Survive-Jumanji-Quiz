'''
A quiz that asks questions and determines whether the user would survive Jumanji
'''
print("Welcome to the Jumanji Quiz!", "\nThis quiz will test whether you could survive Jumanji.")
character_choice = input("Which character do you want to play as (Choose a letter)?:\nA)Dr.Smoulder Bravestone\nB)Ruby Roundhouse\nC)Professor Shelly Oberon\nD)Franklin Finbar 'Mouse'\n").upper()

#Characters to choose from and their characteristics
def characters(choice):
    if character_choice== "A":
        strengths = "Fearless, Climbing, Speed, Boomerang, Smoldering Intensity"
        weakness = "None"
        print("You are Dr.Smoulder Bravestone")
        print("Strengths:", strengths, "\nWeakness: ", weakness)
    elif character_choice == "B":
        strengths = "Karate, T*ai Chi, Aikido, Dance Fighting"
        weakness = "Venom"
        print("You are Ruby Roundhouse")
        print("Strengths:", strengths, "\nWeakness: ", weakness)
    elif character_choice == "C":
        strengths = "Cartography, Archaeology, Paleontology"
        weakness= "Endurance"
        print("You are Professor Shelly Oberon")
        print("Strengths:", strengths, "\nWeakness: ", weakness)
    elif character_choice == "D":
        strengths= "Zoology, Weapons Valet"
        weakness= "Cake, Speed, Strength"
        print("You are Franklin Finbar 'Mouse'")
        print("Strengths:", strengths, "\nWeakness: ", weakness)       
characters(character_choice)
#Quiz questions and answers
print("Now let the quiz begin.", "\nChoose a letter for each question.")
print("Choose wisely!")
def questions ()