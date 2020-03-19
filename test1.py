
list1 = ['Enrique','Iliana','Enrique','Armando','Enrique','Sebastian','Andrea',10,8,10]
#count = list1.count('Enrique')

unique_list = []
for i in list1:
    if i not in unique_list:
        unique_list.append(i)

for i in unique_list:
    count = list1.count(i)
    print(str(i) +' '  +str(count))

print("Unique values: ")
print(unique_list)




