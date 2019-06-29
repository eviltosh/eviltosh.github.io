import random
rng=random.Random()
while True:
    plays=int(input("How many times do you want to play the Lottery ?"))
    for i in range(plays):
        print("\nNumber ",i+1)
        for e in range(6):
            number=rng.randrange(10)
            print(number,end=" ")
    again=input("\nPlay Again? input yes ")
    if again !="yes":
        break
print("Thanks for Playing!!!")    
