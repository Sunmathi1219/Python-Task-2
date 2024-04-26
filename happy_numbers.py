# Happy numbers in python list-(sum of square of numbers which return one is called happy numbers)


list = [10,501,22,37,100,999,87,351]
target = []
def is_happy(list):
    for i in range (len(list)):
        sum = list[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2   
            sum = tempsum
        if sum == 1:
            target.append(list[i])
    return target


print("Happy numbers in the lisi is :", is_happy(list))
