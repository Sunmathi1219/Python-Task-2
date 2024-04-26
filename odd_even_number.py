# Even number and odd number in pthon list

list_number=[55,64,87,99,42,27,35,46,12]
odd_number=[]
even_number=[]

for target in list_number:
    if target%2==0:
        even_number.append(target)

    else:
        odd_number.append(target)

print("Given number list is :",list_number)
print("Odd number list is :", odd_number)
print("even_number list is:", even_number)        