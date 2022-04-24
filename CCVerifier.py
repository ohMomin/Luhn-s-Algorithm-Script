print('Enter Credit Card Number Without Spaces:')
CC = int(input())

splitted_CC_lst = [int(i) for i in str(CC)] #splits input into a list, seperating each number.

for i in range(len(splitted_CC_lst)): #creates a range between 0 and the length of the list

    if i % 2 == 0: 
        splitted_CC_lst[i] *= 2 #if the indicies is odd, it will multiply the CC digit by 2

    if splitted_CC_lst[i] >= 10: #Since the weight of the product is maximum 9, if the product between the CC digit and weight '2 or 1' is > 10, add the numbers. ex: 14 = 5
        first = splitted_CC_lst[i] % 10
        second = splitted_CC_lst[i] // 10
        splitted_CC_lst[i] = first + second

total = sum(splitted_CC_lst) # sum list after

if total % 10 == 0: #Accordnig to Luhn's algorithm, if the sum of the list ends with a 0, it's a valid CC
    print('This is a valid CC number')
else:
    print('This is an invalid CC number') #Accordnig to Luhn's algorithm, if the sum of the list does not end with a 0, it's an invalid CC

#Try your own CC number... >:)

