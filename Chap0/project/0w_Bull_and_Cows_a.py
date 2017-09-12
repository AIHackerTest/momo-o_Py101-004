import random

random_num_list=random.sample(range(1000,10000),1)
print(random_num_list)

print("Guess a four digit number.")
n=0


random_num_str=str(random_num_list[0])


while n<10:
    guess_num_str=input(">")

    if guess_num_str.isdigit():
        guess_num=int(guess_num_str)
        random_num=int(random_num_list[0])

        if guess_num>=10000 or guess_num<1000:
            n+=1
            print("Make sure that you enter a 'four digit' number.You still have %d chance."%(10-n))
        else:
            if random_num==guess_num:
                print("AWESOME! The anwser is %d. You guessed %d time(s)."%(random_num,n+1))
            else:
                a=0
                b=0

                for i in range(4):
                    if guess_num_str[i]==random_num_str[i]:
                        a=a+1
                    elif guess_num_str[i] in random_num_str:
                        b=b+1
                    else:
                        pass
                print("Sorry. You still have %d chance. Hint:%dA%dB"%(9-n,a,b))
                n+=1

    else:
        n+=1
        print("Make sure that you enter a four digit 'number'3.You still have %d chance."%(10-n))
        
print("Time's up! Bad luck today:(")
