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

print("Now let the quiz begin.", "\nChoose a letter for each question.")
print("Choose wisely!")

#Quiz questions
def questions ():
    question_1= input("There's a hippo coming up out of the water. What should you do?:\nA)Scream for help\nB)Run and hide\nC)Stay as still as possible\nD)Fight it")
    question_2= input("You get three lives in Jumanji. What happens if you lose all the lives?:\nA)You die in the game and real life\nB)You get to leave the game\nC)You win the game\nD)Nothing happens")
    question_3= input("A gang of motorcyclers starts chasing you and throwing grenades. What do you do?:\nA)Dodge the grenades\nB)Run\nC)Hide\nD)All of the above")
    question_4= input("The motorcyclers have you cornered on the edge of a cliff by a waterfall. Do you:\nA)Surrender\n)Try to hide\nC)Jump into the water\nD)Try to fight them")
    question_5= input("")
    question_10= input("Good job! You've completed your quest. What must you do to leave the game?:\nA)Jump off the mountain\nB)Call out 'Jumanji'\nC)Nothing, you leave as soon as you get the Jumanji jewel\nD)Throw the jumanji jewel in the air")

