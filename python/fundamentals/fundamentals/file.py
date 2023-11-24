# variable declaration
my_variable = True

# log statement
print("Hello, world!")

# type check
if isinstance(my_variable, bool):
    print("my_variable is a boolean.")

# length check
my_list = [1, 2, 3]
if len(my_list) == 3:
    print("my_list has a length of 3.")

# comment - single line

# comment - multiline

# Data Types

# Primitive

# Boolean
my_boolean = True

# Numbers
my_number = 42

# Strings
my_string = "Hello, world!"

# Composite

# List
# initialize
my_list = [1, 2, 3]

# access value
print(my_list[0])

# change value
my_list[0] = 10

# add value
my_list.append(4)

# delete value
del my_list[1]

# Tuples
# initialize
my_tuple = (1, 2, 3)

# access value
print(my_tuple[0])

# change value (Not possible, tuples are immutable)

# add value (Not possible, tuples are immutable)

# delete value (Not possible, tuples are immutable)

# Dictionary
# initialize
my_dict = {"key1": "value1", "key2": "value2"}

# access value
print(my_dict["key1"])

# change value
my_dict["key1"] = "new value1"

# add value
my_dict["key3"] = "value3"

# delete value
del my_dict["key2"]

# conditional
# if
if my_boolean:
    print("my_boolean is True.")

# else if
elif my_number > 0:
    print("my_number is positive.")

# else
else:
    print("my_boolean is False and my_number is non-positive.")

# for loop
# start, stop, increment
for i in range(0, 10, 2):
    print(i)

# break
for i in range(0, 10):
    if i == 5:
        break
    print(i)

# continue
for i in range(0, 10):
    if i == 5:
        continue
    print(i)

# sequence
my_sequence = [1, 2, 3]
for item in my_sequence:
    print(item)

# while loop
# start
i = 0

# stop
while i < 10:
    print(i)
    i += 1

# increment

# function
# parameter
def my_function(parameter1, parameter2):
    print(parameter1, parameter2)

# argument
my_function("Hello", "world!")

# return
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)
print(result)