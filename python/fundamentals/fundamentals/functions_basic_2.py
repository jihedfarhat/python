# 1.Countdown
def countdown(n):
    return list(range(n, -1, -1))
print(countdown(5))  

# 2.Print and Return
def print_and_return(nums):
    print(nums[0])
    return nums[1]
print(print_and_return([1, 2])) 

# 3.First Plus Length
def first_plus_length(nums):
    return nums[0] + len(nums)
print(first_plus_length([1, 2, 3, 4, 5]))  

# 4.Values Greater than Second
new_list = []
def values_greater_than_second(nums):
    if len(nums) < 2:
        return False
    second_value = nums[1]
    greater_values = [num for num in nums if num > second_value]
    print(len(greater_values))
    return greater_values
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))  


# 5.This Length, That Value
def length_and_value(size, value):
    return [value] * size

print(length_and_value(4, 7))  
