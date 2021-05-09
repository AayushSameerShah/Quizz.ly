import tkinter as tk
from tkinter import messagebox
import datetime
from Connection import getConnection
import random
import Results

LIMIT = 10

def initialize():
    global ques

    db = getConnection()
    cursor = db.cursor()
    cursor.execute('USE quiz')
    
    qry = f''' select * from questions order by rand() limit {LIMIT} '''
    cursor.execute(qry)
    result = cursor.fetchall()
   
    ques = {}
    for id, data in enumerate(result):
        ques[id+1] = data
    db.close()


def starttime():
    if timer.cget("text") == "00:00":
        messagebox.showwarning("Time's up", "You have consumed total time, slow!")
        finish()
        return

    currTime = datetime.datetime.strptime(timer.cget("text"), "%M:%S")
    timer.config(text= (currTime - datetime.timedelta(seconds= 1)).strftime("%M:%S"))
    timer.after(1000, starttime)

def get_next_q():
    for qid in ques.keys():
        q = ques[qid][1]
        op1, op2, op3, op4 = ques[qid][2].split(',')
        
        op1 = op1.strip()
        op2 = op2.strip()
        op3 = op3.strip()
        op4 = op4.strip()

        yield (qid, q, op1, op2, op3, op4)

answers = [""]
def submit():
    global answers
    res = var.get()

    if res == 0:
        messagebox.showerror("No!", "Don't cheat! Fill the answer! Cheater!") 
        return
    answers.append(res)

    update()


Question_gen = get_next_q()
def update():
    qid, q, op1, op2, op3, op4 = next(Question_gen)

    op1 = [op1, 1]
    op2 = [op2, 2]
    op3 = [op3, 3]
    op4 = [op4, 4]

    op1, op2, op3, op4 = random.sample([op1, op2, op3, op4], 4)

    # q.replace("&quot;", "\"")
    # q.replace("&#039;", "")
    if len(q) > 60:
        if len(q) > 110:
            _ = q.split()
            q = ' '.join(_[:5]) + "\n" + ' '.join(_[5:10]) + "\n" + ' '.join(_[10:])
        else:
            _ = q.split()
            q = ' '.join(_[:5]) + "\n" + ' '.join(_[5:])

    questof10.config(text= f"{qid}/{LIMIT}")
    QUESTION.config(text= q)

    var.set(0)
    O1.config(text= op1[0][1:-1], value= op1[1])
    O2.config(text= op2[0][1:-1], value= op2[1])
    O3.config(text= op3[0][1:-1], value= op3[1])
    O4.config(text= op4[0][1:-1], value= op4[1])

    if qid == LIMIT:
        NEXT.config(text= "Finish", command= finish)

def finish():
    
    res = var.get()
    if res == 0 and timer.cget("text") != "00:00":
        messagebox.showerror("No!", "Don't cheat! Fill the answer! Cheater!") 
        return
    answers.append(res)

    total = answers.count(4)
    root.destroy()

    db = getConnection()
    cursor = db.cursor()
    cursor.execute('USE quiz')

    q = f'''UPDATE contestants SET result = {total}, outof = {LIMIT} WHERE id = {id}'''
    cursor.execute(q)
    db.commit()
    db.close()
    
    Results.page(total, LIMIT, answers, ques)

def ExamPaper(ID):
    global timer, questof10, QUESTION, O1, O2, O3, O4, NEXT, var, root, id
    id = ID
    initialize()
    
    root = tk.Tk()
    root.title("Answer the questions")
    root.geometry('1050x500')
    root.resizable(0,0)

    timer = tk.Label(root, text= '1:30', font= ('Consolas',30))
    timer.grid(row= 0, column= 0, padx= 20, pady= 10)
    starttime()

    questof10 = tk.Label(root, text= "1/10", font= ('Consolas',30))
    questof10.grid(row= 0, column= 1, padx= 770)

    tk.Label(root, text= "_"*360).grid(row= 1, columnspan= 2)

    QUESTION = tk.Label(root, text= "?", font= ('Consolas', 20), justify= tk.LEFT)
    QUESTION.grid(row= 2, columnspan= 3, sticky= tk.W, padx= 30, pady= 50)

    var = tk.IntVar()
    O1 = tk.Radiobutton(root, variable=var, font= ('Consolas', 15))
    O2 = tk.Radiobutton(root, variable=var, font= ('Consolas', 15))
    O3 = tk.Radiobutton(root, variable=var, font= ('Consolas', 15))
    O4 = tk.Radiobutton(root, variable=var, font= ('Consolas', 15))

    O1.grid(row= 3, columnspan= 3, sticky= tk.W, padx= 30)
    O2.grid(row= 4, columnspan= 3, sticky= tk.W, padx= 30)
    O3.grid(row= 5, columnspan= 3, sticky= tk.W, padx= 30)
    O4.grid(row= 6, rowspan= 2, columnspan= 3, sticky= tk.NW, padx= 30)

    NEXT = tk.Button(root, text= 'Submit', bg= "#29ff7b", width= 10, height= 2, font= ("Consolas", 15), command= submit)
    NEXT.grid(row= 6, columnspan= 2)

    update()
    root.mainloop()