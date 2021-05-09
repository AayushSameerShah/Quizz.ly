import tkinter as tk
from Connection import getConnection
import SHOW_RIGHT_WRONG


def showWrongs():
    root.destroy()
    SHOW_RIGHT_WRONG.PRINT(ANSWERS, QUES)


def page(total, LIMIT, answers, ques):
    global root, ANSWERS, QUES
    ANSWERS = answers
    QUES = ques

    root = tk.Tk()
    root.geometry("1000x500")
    root.title("Results")

    if total <= LIMIT * 0.4: color = 'red'
    else: color = 'green'

    TOTALlab = tk.Label(root, text= str(total), font=('Consolas', 200), fg= color)
    TOTALlab.place(x= 100, y= 0)

    LINElab = tk.Label(root, text= "_"*200, font=('Consolas', 20))
    LINElab.place(x= 100, y= 250)

    FROMlab = tk.Label(root, text= str(LIMIT), font=('Consolas', 100))
    FROMlab.place(x= 100, y= 300)

    if total <= LIMIT * 0.3:
        result = "Poor"
    elif total <= LIMIT * 0.5:
        result = "Average"
    elif total != LIMIT:
        result = "Okay"
    else:
        result = "Perfect"

    PERFORMANCElab = tk.Label(root, text= f"{result} performance", font= ('Consolas', 30))
    PERFORMANCElab.place(x= 500, y= 130)

    ANSbut = tk.Button(root, text= "Show Answers", bg= "#29ff7b", width= 15, height= 2, font= ("Consolas", 15), command= showWrongs)
    ANSbut.place(x= 700, y= 350)

    root.mainloop()