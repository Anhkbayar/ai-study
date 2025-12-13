listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

odd_index_elements = []

for i in range(len(listOne)):
    if(listOne[i] % 2 != 0):
        odd_index_elements.append(listOne[i])

even_index_elements = []

for i in range(len(listTwo)):
    if(listTwo[i] % 2 == 0):
        even_index_elements.append(listTwo[i])

final_list = odd_index_elements + even_index_elements

print("Sondgoi elementuud:", odd_index_elements)
print("Tegsh elementuud:", even_index_elements)
print("Shine jagsaal:", final_list)
