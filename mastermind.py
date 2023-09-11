import random
num=random.randrange(1000,10000)
chances=10
guess=int(input(f'Guess a four digit number,you have {chances} chances left:'))
if (guess==num):
    print("Congratulations!! You won")
else:
    tries=0
    while guess!= num and chances:
        tries+=1
        chances-=1
        rightdigit=0
        guess=str(guess)
        num=str(num)
        correct=['X']*4
        for i in range(0,4):
            if guess[i]==num[i]:
                rightdigit+=1
                correct[i]=num[i]
        if rightdigit<4 and rightdigit>0:
            print("NOT the right guess,but you guessed",rightdigit,"number RIGHT")
            print("Currenr status is:")
            for char in correct:
                print(char,end=" ")
            print("\n")
            print("\n")
            guess=int(input(f'Guess a four digit number,you have {chances} chances left:'))
        elif rightdigit==0 and chances:
            print("None of your guesses are RIGHT")
            guess=int(input(f'Guess a four digit number,you have {chances} chances left:'))
        if guess==num:
            print("Congratulations!! You won", tries,'gueses, now you are a MASTERMIND')
        if(chances==0):
            print('Sorry! you have ran out of chances!!')
            print('NUMBER is ',num)