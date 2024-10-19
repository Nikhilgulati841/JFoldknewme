 
print('''\n----Instructions to play----
Get the BAR value to 3, to win the Game.\n
- Two types of Points --> PowerFull | Powerless
- PowerFull will give the sum of all 3 Points
- PowerLess will only give it for the first 2 Points''')

def game(a,b,c,attempt,bar):

    a=int(input("\nPoint 1: "))
    b=int(input("Point 2: "))
    c=int(input("Point 3: "))
 
    if a+b>c:

        score=a+b+c

        print("\n")
        print(f"{msgnew} | SCORE : {score} |\t(as the sum of Point 1 & 2 is more than Point 3)")

        attempt+=1
        bar+=1

        print(f"ATTEMPT: {attempt} | BAR: {bar}")

        

    elif a+b==c:

        score=a+b+c

        print("\n")

        print(f"{msgnew} | SCORE : {score} |\t(as the sum of Point 1 & 2 is Equal to Point 3)")

        attempt+=1
        bar+=1

        print(f"ATTEMPT: {attempt} | BAR: {bar}")

        

    else: 

        score=a+b

        print("\n")

        print(f"{msgold} | SCORE : {score} |\t(as the sum of Point 1 & 2 is Less than Point 3)")

        attempt+=1
        bar-=1

        print(f"ATTEMPT: {attempt} | BAR: {bar}")

    return attempt,bar
        

 
x=0
attempt=0
bar=0

msgnew="PowerFull Points"
msgold="PowerLess Points"
barmsg="\nACHIEVED"

 
while True:

    if bar==3:

        print(barmsg,f" (as the BAR:{bar} is reached on Attempt:{attempt})\n")

        break
    

    else:
        attempt,bar=game(1,1,1,attempt,bar)

if attempt==bar:     
    print(f"LUCKY YOU\nBAR:{bar} Achieved with the same number of ATTEMPT:{attempt}\n")

   
input()