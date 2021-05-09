# Quizz.ly

> NOTE:  
> This requires MySQL (XAMPP installed and running on 3306 port) 

--

1. Please do not delete / modify the database file name - Questions.json
2. Before starting the main `quiz.ly` application, running `setup` is 
   required.
3. Make sure you have XAMPP opened and MySQL server running on port 3306
   ( Yes, that could be done automatically but as it is my personal mini
     program, I didn't focus on that )

Summary:

1. Run `Setup.py` (It will prepare the database)
2. Run `First Page.py` (It will run actual program)

Done! And other files are interconnected.
--

More:
The database is also maintained in the back.
To see, log in with root and select... well let me show you the steps.

- mysql -u root -p
- USE quiz;
- SHOW TABLES;
(There are two tables)

Apply SELECT query for each table if you want to see the data.
--

Errors:
There, you may get an error if... 1) The application can't access root user ( which it uses without a password )
   				  2) XAMPP is not running (MySQL) on port 3306
				  3) The application throws an StopIterationError <--- Restarting an application will solve this.

--

Thanks and other words...
This is my small try for the first section in learning python - I know there are many bugs in the system and can be so irritating.
But hey, it still works right! 

Thanks for reading this far and pardon my dust.
∞ Aayush Shah
