from tkinter import *
from PIL import ImageTk, Image
#To use code, you must install Pillow and check to make sure tkinter is on your system


print("Welcome to the Jumanji Quiz!", "\nThis quiz will test whether you could survive Jumanji.")
root = Tk()
root.title("Can You Survive?: Jumanji Quiz")
main_img= ImageTk.PhotoImage(Image.open("maincharacters.jpg"))
my_label= Label(image= main_img)
my_label.pack()
button_quit= Button(root, text= "Press Exit and return to quiz in terminal", command= root.quit)
button_quit.pack()
mainloop()
character_choice = input("Which character do you want to play as (Choose a letter)?:\nA)Dr.Smoulder Bravestone\nB)Ruby Roundhouse\nC)Professor Shelly Oberon\nD)Franklin Finbar 'Mouse'\n").upper()

#Characters to choose from and their characteristics
















#e= Entry(root, width= 100, borderwidth= 5)
#e.pack()
#question_1= "There's a hippo coming up out of the water. What should you do?:\nA)Scream for help\nB)Run and hide\nC)Stay as still as possible\nD)Fight it\n"
#e.insert(0,question_1)


#def next_click():
    #question= Label(root, text = e.get())
    #question.pack()
    
#myLabel1= Label(root, text = "hello world").grid(row= 0, column= 0)
#myLabel2 = Label(root, text= "my name is janai").grid(row=1, column= 0)
#next_button= Button(root, text= "Next", padx= 5, pady= 5, command= next_click)
#next_button.pack()

#myLabel1.grid(row= 0, column= 0)
#myLabel2.grid(row=1, column= 0)

#root.mainloop()