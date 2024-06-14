sequence = input("Enter a sequence of integers separated by whitespace: ") 
#change the numbers for list and save
s_list = sequence.split(" ") 

j = 0
#change the numbers in the list into integers
while j < len(s_list): 
    s_list[j] = int(s_list[j])
    j = j + 1
#check for "larger" or "smaller"
while j < len(s_list) - 1:
    if s_list[j] <= s_list[j+1]:
        del s_list[:j+1]
    j = j + 1
#output
print("Length:", len(s_list))
print ("LICS",s_list)



















