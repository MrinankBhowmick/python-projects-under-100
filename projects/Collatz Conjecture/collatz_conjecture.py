
current_num = int(input("Enter the number to start from: ")) #accept user input
checker = False
num_list = []

even = lambda current_num: current_num/2 #lambda function for the even results
odd = lambda current_num: 3*current_num + 1 #lambda function for the odd results

while (checker == False):
    if (current_num != 1):#check if the number equals 1
        if (current_num%2 == 0): #check if the number is even
            num_list.append(int(even(current_num))) #add the operation value to the tree
            current_num = even(current_num) #set the new value of the current_num
            
        elif (current_num%2 == 1): #check if the number is odd
            num_list.append(int(odd(current_num))) #add the operation value to the tree
            current_num = odd(current_num) #set the new value of the current_num

    else: #if the number equals 1
        num_list.append(int(current_num))
        checker = True #loop breaker
print(f"\nTree: {num_list}") #print tree
print(f"The operation took {len(num_list)} steps to complete and the peak was {max(num_list)}.\n") #operation summary

