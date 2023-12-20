#1.Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
list = []
def countdown(num):
  for num in range(num, -1, -1):
    list.append(num)
  print(list)
countdown(20)

print("#" * 50)

#2.Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_and_return(my_list):
  print(my_list[0])
  return my_list[1]
print_and_return([4,5])

print("#" * 50)


#3.First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(list_length):
  print(list_length[0] + len(list_length))
first_plus_length([1,2,3,4,5,6,8])

print("#" * 50)

#4.Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
new_list = []
def  values_greater_than_second(list):
  for x in list:
    if len(list) < 2:
      print("false")
    elif list[1] < x:
      new_list.append(x)
  print(new_list)
values_greater_than_second([5,2,3,2,1,4])

print("#" * 50)

#5.This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(size, value):
    return [value] * size
print(length_and_value(4, 7))  