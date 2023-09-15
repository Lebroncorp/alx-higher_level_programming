my_list = (1, 2, 4, 2, 5, 3, 3, 1)

print(my_list)

clean = set(my_list)
print(clean)

new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)
