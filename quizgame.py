import colorama
from colorama import Fore

colorama.init()  # Initialize Colorama

def give_options(x,y,z):
    print(Fore.WHITE + "a):", x)
    print(Fore.WHITE + "b):", y)
    print(Fore.WHITE + "c):", z)
    
print(Fore.WHITE + "Hello! Welcome to my Quiz" "\n" "All Questions carries 10 marks each")

ans = input(Fore.BLUE + "Are you ready to play (yes/no): ")

a ="\nNote: wrtie answers! do not write option."

score = 0

total_questions = 4

correct_ans =["python", "steve jobs", "artificial intelligence", "bitcoin"]

if ans.lower() == "yes":
    print(a)
    
    print(Fore.BLUE + "Question- What is the best Programming Language? ")
    
    give_options("Python", "C", "Java" )
    

    ans=input("Please Type Your Answer:\t")
    
    if ans.lower() == correct_ans[0]:
        score=score+1
        print(Fore.GREEN + "Correct")
    else:
        print(Fore.RED + "Incorrect")
        
    print(a)
    
    print(Fore.RED +"Question- Who is the Founder of Apple Inc? ")
    
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
    
    ans=input("Please Type Your Answer:\t")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print(Fore.GREEN + "Correct")
    else:
        print(Fore.RED + "Incorrect")

    
    print(a)
    
    print(Fore.GREEN +"Question- What is more better among these? ")
    
    give_options("Data Science", "Artificial Intelligence", "Digital Marketing")
    
    ans=input("Please Type Your Answer:\t")
    
    if ans.lower() == correct_ans[2]:
        score=score+1
        print(Fore.GREEN + "Correct")
    else:
        print(Fore.RED + "Incorrect")
        
    print(a)
    
    print(Fore.YELLOW + "Question- What is the best Investment? ")
    
    give_options("Share Capital", "Mutual Funds", "Bitcoin")
    
    ans=input("Please Type Your Answer:\t")
    
    if ans.lower() == correct_ans[3]:
        score=score+1
        print(Fore.GREEN + "Correct")
    else:
        print(Fore.RED + "Incorrect")

i = score*10

print ("score:" , i)

if i < 30:
    print(Fore.BLUE + "Ouch, your score is ",i,"/ 40 better luck next time.")
elif i ==30:
    print(Fore.BLACK + "Nice! you scored ",i,"/ 40 you are quiet smart.")
else:
    print(Fore.GREEN + "Congratulations! it's a perfect ",i,"/ 40 you are Intelligent.")
    
