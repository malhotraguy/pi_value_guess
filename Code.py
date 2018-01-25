! curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o pi.txt
pi_txt=open('pi.txt','r')
user_name=input("Enter your Name please!!: ")
print("Hello",user_name,"!!")
seed=len(user_name)
pi_txt.seek(seed)
digit=pi_txt.read(1)
correct=0
fail=0
while digit!="":
    if digit==".":
        digit=pi_txt.read(1)
    elif digit=="\n":
        seed=seed+1
        pi_txt.seek(seed)
    else:
        
        guess=input("Enter your guess for the number or 'quit' to end: ")
        print("The digit in the file was",digit)
    
        if guess=="quit":
            print("Thats the end of your trails")
            break
        
        elif guess==digit:
            print("Your guess is correct: Yippie!!")
            correct=correct+1
        else:
            print("No!! your guess is not correct!!")
            fail=fail+1
        digit=pi_txt.read(1)

print("Correct Guesses:",correct,"\nIncorrect Guesses:",fail)
pi_txt.close()
