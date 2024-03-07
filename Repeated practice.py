#Write a function in Python that accepts a decimal number 
#and returns the equivalent binary number. 
#To make this simple, the decimal number will always be less than 1,024, 
#so the binary number returned will always be less than ten digits long.

# The code below was done without using the binary inbuilt function python

dec_num = int(input("Enter value: "))

def decimal_to_binary(dec_num):
    if dec_num == 0:
        return "0"
    bin_digit = []
    while dec_num > 0:
        remainder = dec_num % 2
        bin_digit.append(str(remainder))
        dec_num //= 2
        
    bin_num = ''.join(bin_digit[::-1])    
    return bin_num

print(decimal_to_binary(dec_num))

