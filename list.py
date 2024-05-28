# derived data types
'''
1. list (mutable) modify
2. Tuples immutable
3. Set
4. Dictionary
'''
my_list = [1,2,3, "Nepal", "Hello", 3+4j]
#slicing of list - printing list in range
print(my_list[2:5])  # [2]3, [3]nepal, [5]hello

print(len(my_list))  # 6 elements 

# -----------------------------------------

#list
my_list = [1,2,"Nepal"]
print(my_list)
print(my_list[2])

#[-3,-2,-1]
print("Negative indexing")
print(my_list[-3])

#adding elements to the list using append function
my_list.append("Country")
print(my_list)

#removing the element from list using element name
my_list.remove("Country")
print(my_list)

#removing element using index
del my_list[0]   #0 index deleting
print(my_list)

# adding element using insert function
my_list.insert(1, "India")   #inserting  index 1 
print(my_list)
print("-------------------")

#printing elements using for loop
for element in my_list:
    print(element)


#making 2D list
my_2D_list = [[1,1,1],[2,2,2],[3,3,3]]
print(my_2D_list)


