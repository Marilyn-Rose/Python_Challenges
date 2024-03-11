# Create a Python function that accepts a string.
# The function should return a string, with each character in the original 
# string doubled.
# If you send the function “now” as a parameter, it should return “nnooww,”
# and if you send “123a!”, it should return “112233aa!!”.

string_input = input(str("Enter string: "))

def double_char(string_input):
    double_string = ""
    
    for char in string_input:
        double_string +=  char * 2
    return double_string
    
print(double_char(string_input))
        