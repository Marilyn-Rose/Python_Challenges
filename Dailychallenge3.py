#Write a function in Python that accepts a decimal number 
#and returns the equivalent binary number. 
#To make this simple, the decimal number will always be less than 1,024, 
#so the binary number returned will always be less than ten digits long.

# The code below was done without using the binary inbuilt function python
def decimal_to_binary(dec_num):
    if dec_num == 0:
        return "0"
    
    bin_digits = []
    while dec_num > 0:
        remainder = dec_num % 2
        bin_digits.append(str(remainder))
        dec_num //= 2
        
    bin_num = ''.join(bin_digits[::-1])
    return bin_num

dec_num = int(input("Enter decimal number: ",  ))
bin_output = decimal_to_binary(dec_num)
print(f"The binary representation of {dec_num} is : {bin_output}")

# The code below uses the binary inbuilt function in python 
#def decimal_to_binary(dec_num):
 #   bin_num = bin(dec_num)[2:]
 #   return bin_num

#dec_num = int(input("Enter decimal number: "))
#bin_output = decimal_to_binary(dec_num)
#print(f"The binary representation of {dec_num} is : {bin_output}")