'''
A quiz that asks questions and determines whether the user would survive Jumanji
'''
print("Welcome to the Jumanji Quiz!", "\nThis quiz will test whether you could survive Jumanji.")
character_choice = input("Which character do you want to play as (Choose a letter)?:\nA)Dr.Smoulder Bravestone\nB)Ruby Roundhouse\nC)Professor Shelly Oberon\nD)Franklin Finbar 'Mouse'\n").upper()

#Characters to choose from and their characteristics
def characters(choice):
    if character_choice== "A":
        strengths = "Fearless\nClimbing\nSpeed\nBoomerang\nSmoldering Intensity"
        weakness = "None"
        print("You are Dr.Smoulder Bravestone")
        print("Strengths:\tWeakness:")
        print(strengths, "\t", weakness)
    elif character_choice == "B":
        strengths = "Karate\nT*ai Chi\nAikido\nDance Fighting"
        weakness = "Venom"
        print("You are Ruby Roundhouse")
        print("Strengths:\tWeakness:")
        print(strengths, "\t", weakness)
    elif character_choice == "C":
        strengths = "Cartography\nArchaeology\nPaleontology"
        weakness= "Endurance"
        print("You are Professor Shelly Oberon")
        print("Strengths:\tWeakness:")
        print(strengths, "\t", weakness)
    elif character_choice == "D":
        strengths= "Zoology\nWeapons Valet"
        weakness= "Cake\nSpeed\nStrength"
        print("You are Franklin Finbar 'Mouse'")
        print("Strengths:\tWeakness: ")
        print(strengths, "\t", weakness)
characters(character_choice)
