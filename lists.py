my_list = []

my_list += [10, 20, 30, 40]

my_list = my_list[:1] + [15] + my_list[1:]

my_list.extend([50, 60, 70])

my_list.pop(-1)

my_list.sort()

index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")

# Output 
print("final sorted list is:", my_list)
