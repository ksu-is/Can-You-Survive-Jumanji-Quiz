from tkinter import *
#from tkinter import filedialog
#from PIL import ImageTk, Image
#from tkinter import messagebox
#import os
#cmd = "curl https://github.com/ksu-is/Can-You-Survive-Jumanji-Quiz/blob/main/Nigel.png -o Nigel.png "
#os.system(cmd)

#Nigel_img = open('Nigel.png', 'r+')

root = Tk()
root.title("Can You Survive?: Jumanji Quiz")
#root.iconbitmap('jewel.jpg')
root.geometry("300x300")

results =3

def results_clicker():
    global pop
    pop = Toplevel(root)
    pop.title("Game Results")
    pop.geometry("250x150")
    pop.config(bg= "green")

    if results >= 5:
        global nigel
        nigel = PhotoImage(file= 'Nigel.png') #"https://github.com/ksu-is/Can-You-Survive-Jumanji-Quiz/blob/main/Nigel.png")
        nigel_label = Label(image= nigel)
        nigel_label.pack()
        pop_label = Label (pop, text="Congratulations!\nYou survived Jumanji.", bg= "green", fg= "white", font= ("arial", 12))
        pop_label.pack(pady=10)

        my_frame = Frame(pop, bg= "green")
        my_frame.pack(pady=5)

        nigel_pic = Label(my_frame, image= nigel, borderwidth=0)
        nigel_pic.grid(row=0, column=0, padx=10)

        okay= Button(my_frame, text= "Okay", command = my_frame.quit)
        okay.grid(row= 0, column=1, padx=10)
    elif results < 5:
        global russell
        russell = PhotoImage(file= 'Russell.jpg') 
        russell_label = Label(image= russell)
        russell_label.pack()
        pop_2_label = Label (pop, text="Oh no! You didn't survive.\nBetter luck next time.", bg= "green", fg= "white", font= ("arial", 12))
        pop_2_label.pack(pady=10)

        my_2_frame = Frame(pop, bg= "green")
        my_2_frame.pack(pady=5)

        russell_pic = Label(my_2_frame, image= russell, borderwidth=0)
        russell_pic.grid(row=0, column=0, padx=10)

        okay_2= Button(my_2_frame, text= "Okay", command = my_2_frame.quit)
        okay_2.grid(row= 0, column=1, padx=10)







results_button= Button(root, text= "Results", command= results_clicker)
results_button.pack(pady=50)

my_label = Label(root, text= "")
my_label.pack(pady=20)




root.mainloop()





























#print("Welcome to the Jumanji Quiz!", "\nThis quiz will test whether you could survive Jumanji.")
#root = Tk()
#root.title("Can You Survive?: Jumanji Quiz")
#main_img= ImageTk.PhotoImage(Image.open("maincharacters.jpg"))
#my_label= Label(image= main_img)
#my_label.pack()
#button_quit= Button(root, text= "Press Exit and return to quiz in terminal", command= root.quit)
#button_quit.pack()

#character_choice = input("Which character do you want to play as (Choose a letter)?:\nA)Dr.Smoulder Bravestone\nB)Ruby Roundhouse\nC)Professor Shelly Oberon\nD)Franklin Finbar 'Mouse'\n").upper()

#correct = 3
#def results_click():
    #if correct >= 5:
        #print(correct, "/10")
       # win= messagebox.showinfo("Results","Congratulations! You survived Jumanji.")
        
   # if correct <5:
        #print(correct, "/10")
        #lose= messagebox.showinfo("Results","Oh no! You didn't survive.\nBetter luck next time.")
        
#results_button= Button(root, text= "Results", command= results_click).pack()
#results_button.geometry("350x350")
#mainloop()
    
















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