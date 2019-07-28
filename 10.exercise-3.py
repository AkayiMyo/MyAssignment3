#Request a name of the file
file_name=input("Enter name of the file")
#Read the inputted file
handle = open(file_name,'r')


mylist=list()
#display the content line by line with while loop
for line in handle:

  print(line)
  mylist.append(line)
 
#save the line into list by using append function

print(mylist)









