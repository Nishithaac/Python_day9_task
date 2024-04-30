"""
Write a python code using Lambda function to check every element of a list is an integer or string

"""
#Method1
# Defining a list containing a mix of integers and strings
data=[1,"orange","kiwi",5]

# Use map and lambda to check if each element in data is a string
# `isinstance(x, str)` returns True if x is a string, otherwise False
# Apply lambda function to each element in data
result1=list(map(lambda x:isinstance(x,str),data))
# Printing  the result1 list
print(result1)

# Initialising an empty list to store strings from data
strings=[]

# Initialising an empty list to store integers from data
integers=[]

# Looping through the result1 list
for i in range(len(result1)):

    # If the result1 element at index i is True (indicating the corresponding data element is a string)
    if result1[i]==True:

        # Appending  the corresponding data element to the strings list
        strings.append(data[i])
# Printing the strings list
print(f"Strings: {strings}")


# Use map and lambda to check if each element in data is an integer
# `isinstance(x, int)` returns True if x is an integer, otherwise False
# Apply lambda function to each element in data
result2=list(map(lambda x:isinstance(x,int),data))
# Printing the result2 list
print(result2)

# Looping through the result2 list
for i in range(len(result2)):
    # If the result2 element at index i is True (indicating the corresponding data element is an integer)
    if result2[i]==True:
        # Appending the corresponding data element to the integers list
        integers.append(data[i])
# Printing the integers list
print(f"Integers: {integers}")


#Method2

data = [1, "orange", "kiwi", 5]  # Defining  a list containing a mix of integers and strings

# Use map and lambda to check if each element in data is either an integer or a string
# `isinstance(x, int) or isinstance(x, str)` returns True if x is an integer or a string, otherwise False
result = all(map(lambda x: isinstance(x, int) or isinstance(x, str), data))

if result:  # If every element in the list is either an integer or a string
    print("Every element of the list is either an integer or a string.")
else:  # If there are elements in the list that are not integers or strings
    print("There are elements in the list that are not integers or strings.")
