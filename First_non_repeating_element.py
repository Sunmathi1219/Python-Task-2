# find first non repeating elelments  in the given list of integer in  python


def non_repeating(first):
    counts={}  #dictionary(key:value pair combination like maps)

    for number in first:
        counts[number]=counts.get(number,0)+1  # get returns the particular key value of element
        
    for i in first:
        if counts[i]==1:
            return i

    return -1   #non-repeating number in list

list_num=[15,20,30,15,20,28,30,81,34]
first_non_repeating=non_repeating(list_num)
print("First Non-Repeating element in the list of integer is :", first_non_repeating)         