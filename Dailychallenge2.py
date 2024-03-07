#Create a function in Python that accepts two parameters. The first will be a list of numbers. 
#The second parameter will be a string that can be one of the following values:
#asc, desc, and none.
#If the second parameter is “asc,” then the function should 
#return a list with the numbers in ascending order.
#If it’s “desc,” then the list should be in descending order, and if it’s “none,” 
#it should return the original list unaltered.

def sorting_list(num_list, str_order):
    sorted_list = num_list[:]
    if str_order == "asc":
        sorted_list.sort()
    elif str_order == "desc":
        sorted_list.sort(reverse=True)
    elif str_order != "none":
        print("Invalid String Order specified")
        return None
    return sorted_list

num_list = [3, 2, 4, 8, 10, 5]
print("Ascneding order: ", sorting_list(num_list, "asc"))

print("Descending order: ", sorting_list(num_list, "desc"))

print("Orginal list: ",sorting_list(num_list,"none" ))


#a second version of the solution
#list_num = []
#list_num = [3,7,32,8,4,97]

#def sorting_list(list_num,str_order):
 #   if str_order == "asc":
  #      return sorted(list_num)
   # elif str_order == "desc":
    #    return sorted(list_num,reverse=True)
    #elif str_order == "none":
     #   return list_num
    #else:
     #   print("Entered wrong sorting order")
 
#str_order = "asc"      
#print(sorting_list(list_num,str_order))