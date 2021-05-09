import json
from Connection import getConnection
try:
    db = getConnection()
    cursor = db.cursor()
except:
    print("Please start the XAMPP server and make sure it is running on port 3306")
    input("Press enter and restart this setup after fixing the problems...")
else:
    q = '''CREATE DATABASE IF NOT EXISTS quiz'''
    cursor.execute(q)

    q = '''\
    CREATE TABLE IF NOT EXISTS quiz.contestants
    (id INT(5) PRIMARY KEY AUTO_INCREMENT,
    fname VARCHAR(100) DEFAULT 'DUMB',
    sname VARCHAR(100) DEFAULT 'KAKA',
    age INT(5) DEFAULT 18,
    result INT(5),
    outof INT(5)
    )'''
    cursor.execute(q)

    q = '''\
    CREATE TABLE IF NOT EXISTS quiz.questions
    (id INT(5) PRIMARY KEY AUTO_INCREMENT,
    question varchar(500),
    options varchar(100),
    answer varchar(100))
    '''
    cursor.execute(q)

    q = '''TRUNCATE TABLE quiz.questions'''
    cursor.execute(q)

    with open('./questions.json') as f:
        databse = json.load(f)

        for question in databse['results']:
            q = question['question']
            ans = question['correct_answer']
            opt = question['incorrect_answers']
            opt.append(ans)
            
            qury = \
            f'''
            INSERT INTO quiz.questions(question, options, answer)
            VALUES ("{q}", "{str(opt)[1:-1]}", "{ans}")
            '''
            

            cursor.execute(qury)
        




    db.commit()
    print("[Done]")
    input("Now, your installation is done.\nPress enter to complete this... ")


