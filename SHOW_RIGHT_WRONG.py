import tkinter as tk
from tkinter import *

def PRINT(answers, ques):
    root = tk.Tk()
    root.title("Right ones")
    root.geometry('1500x1000')

    for i,key in enumerate(ques):
        if answers[key] != 4:
            color = 'red'
        else: color = 'green'

        tk.Label(root, text= str(i+1) + '. ' + ques[key][1], fg= color, font= ("Consolas", 15)).pack(side=TOP, anchor=NW)
        tk.Label(root, text= "Answer: ", font= ("Consolas", 15)).pack(side=TOP, anchor=NW)
        tk.Label(root, text= ques[key][3], fg= '#00c76a', font= ("Consolas", 15)).pack(side=TOP, anchor=NW)
        tk.Label(root, text= ' ', font= ("Consolas", 4)).pack(side=TOP, anchor=NW)
    
    root.mainloop()
    
