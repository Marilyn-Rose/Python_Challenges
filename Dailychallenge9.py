# Write a function in Python that accepts a list of any length that 
# contains a mix of non-negative integers and strings. 
# The function should return a list with only the integers in the original list in the same order.


mixed_list = [10, 'apple', 20, 'banana', 30]

def extract_int(input_list):
    list_int = []
    
    for element in input_list:
        if isinstance(element, int) and element >= 0:
            list_int.append(element)
    return list_int


print (extract_int(mixed_list))