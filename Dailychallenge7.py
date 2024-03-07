# Write a Python function that accepts three parameters.
# The first parameter is an integer. The second is one of the following
# mathematical operators: +, -, /, or . The third parameter will also be 
# an integer.
# The function should perform a calculation and return the results.
# For example, if the function is passed 6 and 4, it should return 24.

first_par = int(input("Enter First value: ",))
second_par = input("Enter the mathematical operator: ")
third_par = int(input("Enter Third Value: "))

def calculation(first_par,second_par,third_par):
    if second_par == "+" :
        return first_par + third_par
    elif second_par == "-" :
        return first_par - third_par
    elif second_par == "/" :
        return first_par / third_par
    elif second_par == "*" :
        return first_par * third_par
    else:
        print("Wrong operator inputed")
         
print(calculation(first_par,second_par,third_par))