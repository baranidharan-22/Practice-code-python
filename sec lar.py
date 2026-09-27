a = [100,400,660,500,320,600,700]
largest = 0
secondlargest = 0

for i in a:
    if i>largest:
        secondlargest = largest
        largest = i
    elif i>secondlargest:
        secondlargest = i
print(f"Largest :{largest}")
print(f"Secondlargest :{secondlargest}")
