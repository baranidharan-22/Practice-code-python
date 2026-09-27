num = 5
attempts = 0
while True:
    attempts+=1
    print(f"\n {attempts} attempts")
    a = int (input("enter your number :"))
    if num>a:
        print (a,"lesser than",num)
    elif num<a:
        print (a,"greater than ",num)
    else:
        print ("The number 5 is found")
        print (f"You Found in {attempts} attempts")
        break