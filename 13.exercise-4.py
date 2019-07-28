# Create a function that return the largest number in the list


#def get_largest_number():
   # largest_number = 0
    #return largest_number

   # largest = None
def get_largest_number(input):
    maxnumber = input[0]
    for number  in input:
       if number > maxnumber:
        maxnumber = number
        
    return maxnumber  


    


result=get_largest_number([1,2,3,4,5,12,1,6,99,2])
 

print(result)      




