# find sum of first and last digit of an integer

list_num=[101,254,879,546]

for number in list_num:
    last_digit=number%10
    first_digit=number
    while first_digit>9:
        first_digit=first_digit//10

    result=first_digit+last_digit
    
    print("number is:", number)
    print("First digit is :",first_digit)
    print("Last digit  is :", last_digit)
    print("Sum of first and last digit is :", result)



