import tkinter as tk
from tkinter import messagebox
import Question_Interface
from Connection import getConnection

def register():
    first = First.get().strip()
    last = Last.get().strip()
    age = Age.get().strip()

    if first == '' or last == '' or age == '':
        messagebox.showerror("Data missing", "Please enter the data in all fields.")
    else:
        db = getConnection()
        cursor = db.cursor()
        cursor.execute('USE quiz')

        q = f'''\
            INSERT INTO contestants(fname, sname, age, result, outof) VALUES ("{first}", "{last}", "{age}", 0, 0)
            '''
        cursor.execute(q)
        db.commit()

        q = '''SELECT MAX(id) FROM contestants'''
        cursor.execute(q)
        ID = cursor.fetchone()[0]
        db.close()
        root.destroy()

        Question_Interface.ExamPaper(ID)
        
        
root = tk.Tk()
root.title("Fill the Formalities")
root.geometry('720x430')

tk.Label(root, text= 'Quizz.ly', font= ('Consolas', 50)).grid(row= 0, columnspan= 2, sticky= tk.N, padx= 200)
tk.Label(root, text= 'A N  I N I T I A T I V E by Aayush Shah', font= ('Consolas', 10)).grid(row= 1, columnspan= 2, sticky= tk.N, padx= 200)

tk.Label(root, text= 'First:', font= ('Consolas', 15)).grid(row= 2, column= 0, sticky= tk.W, pady= 20, padx= 20)
First = tk.Entry(root, font= ('Consolas', 20))
First.grid(row= 3, column= 0, sticky=tk.W, padx= 20)

tk.Label(root, text= 'Last:', font= ('Consolas', 15)).grid(row= 2, column= 1, sticky=tk.W)
Last = tk.Entry(root, font= ('Consolas', 20))
Last.grid(row= 3, column= 1, sticky=tk.W)

tk.Label(root, text= 'Age:', font= ('Consolas', 15)).grid(row= 4, column = 0, sticky=tk.W, padx= 20, pady= 20)
Age = tk.Entry(root, font= ('Consolas', 40), width= 5)
Age.grid(row= 5, columnspan= 1, sticky=tk.W, padx= 20)

tk.Label(root, text= "NOTE: By Pressing start - The quiz will start automatically and total time will be given of 1.5 minutesfor 10 questions.", fg= "#f52a67").grid(row= 6, columnspan= 2, sticky= tk.W, pady= 40, padx= 20)

tk.Button(root, text= "Start", bg= "#29ff7b", font= ('Consolas', 15), width= 15, height= 2, command= register).grid(row= 5, column= 1, sticky= tk.W)
root.mainloop()