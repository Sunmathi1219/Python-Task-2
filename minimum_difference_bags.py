def min_difference_between_bags(mangoes, students):
    mangoes.sort()  # Sort the number
    min_difference = float('inf')  

    

    for i in range(len(mangoes) - students + 1):
        difference = mangoes[i + students - 1] - mangoes[i]
        min_difference = min(min_difference, difference)

    return min_difference


mangoes = [10, 7, 11, 12, 8, 4,3,15]
students =3

result = min_difference_between_bags(mangoes, students)
print("Minimum difference between bags:", result)
