import random

rand=random.randint(1000,9999)

random=[]

for i in range(len(str(rand))):
    random.append(str(rand)[i])

Repeat='Yes'
Guess=0

while Repeat=='Yes':
    
    user_input=int(input("enter a number"))
    user_input_list=[]
    cows=0
    bulls=0
    for j in range(len(str(user_input))):
        user_input_list.append(str(user_input)[j])
        
    for i in range(len(user_input_list)):
        if user_input_list[i]==random[i]:
            cows=cows+1
        elif user_input_list[i] not in random[i] and user_input_list[i] in random:
            bulls=bulls+1


    print("bulls=",bulls,"   cows=",cows)
    

    if user_input_list==random:
        Repeat='No'
    else:
        Repeat='Yes'
    Guess=Guess+1
else:
    print("YOU GUESSED IT CORRECT in",Guess,"Guess")
