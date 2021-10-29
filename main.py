#First creating variables and storing the questions and the options of the questions in that variable
# The triple quotes(""") are used to store multiple lines of string :-
q1 = """How many time zones are there in Russia?
a. 16
b. 11 
c. 6
d.3"""

q2 = """What's the national flower of Japan?
a. Cherry blossoms
b. Sunflowers
c. Japanese Apricot
d. Red Rose"""

q3 = """How many stripes are there on the US flag?
a. 20
b. 11
c. 13
d. none of the above"""

q4 = """What's the national animal of Australia?
a. kangaroo
b. Lion
c. Tiger
d. Snake"""

q5 = """How many days does it take for the Earth to orbit the Sun?
a. 265 days
b. 355 days
c. 300 days
d. 365 days"""

questions = {q1:"b", q2:"a", q3:"c", q4:"a", q5:"d"} # creating a dictionary to store the (questions + options) and correct answer to the question

name = input("Enter your name: ") # taking the input for the name:-
print() # using print function to leave a line:-
print("hello " + name + ", welcome to my quiz game") # printing "Hello (the name as input from user), welcome to my quiz world":-

score = 0 # declaring variable score and assigning the value 0 to the variable (score):-

for key in questions: # creating a loop to display all the questions, options and ask the user ans
    print() # using print to leave a line:-
    print("----------------------------------------------------") # printing "-----------" just for convenience:-
    print(key) # printing the key from the dictionary we had created:-
    skip = input("Do you want to skip this question? (yes/no)") # taking the input from the user, whether they want to skip the question or not
    skip = skip.lower() # converting the input given by the user into lower case
    if skip == "yes": # if the user enters skip, the loop will start over again
        continue

    ans = input("enter the answer (a/b/c/d): ") # asking the user to enter the answer
    ans = ans.lower() # converting the ans entered by the user into lower case

    if ans == questions[key]:# if the ans entered by the user is equal to the value in the dictionary,
    # we will print "correct! you got 1 point" and increase the value of the score variable by 1
        print("Correct!, you got 1 point")
        score += 1
        print("Your current score is " + str(score)) # printing the current score

    else: # if the answer entered by the user is not equal to the value in the dictionary,
    # we will print "wrong!, you lost 1 point" and decrease the score by 1
        print("Wrong!, you lost 1 point")
        score -= 1
        print("Your current score is " + str(score)) # printing the current score

    quit = input("Do you want to quit the quiz? (yes/no)") # asking the user whether they want to quit the game or not. It will only be asked after the 1st question
    quit = quit.lower() # converting the input given by the user into lower case

    if quit == "yes": # if the input given by the user is equal to yes then the loop will stop
        break

print("Your Final score is " + str(score)) # printing the final score
