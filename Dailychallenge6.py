# Create a Python function that accepts a string.
# This function should count the number of Xs and the number of
# Os in the string. It should then return a boolean value of either True or False.
# If the count of Xs and Os are equal,
# then the function should return True. 
# If the count isn’t the same, it should return False. 
# If there are no Xs or Os in the string, 
# it should also return True because 0 equals 0. 
# The string can contain any type and number of characters.

string = input(str("Enter string: "))

def count_string(string):
    string_x = "x"
    string_o = "o"
    x_count = 0
    o_count = 0
    
    for char in string:
        if char == string_x:
                x_count += 1
                print("x_count: ", x_count)
        elif char == string_o:
                o_count += 1
                print("o_count: ", o_count)
        
        #num_x = string_x.count(string)
        #num_o = string_o.count(string)
    if x_count == o_count:
            return True
    elif x_count != o_count:
            return False

print(count_string(string))  
    
    