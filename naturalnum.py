num = int(input("Enter the value of n: "))
hold = num
sum = 0
if num <= 0: 
   print("Enter a whole positive number!") 
else: 
   while num > 0:
        sum = sum + num
        num = num - 1;
   print("Sum of first", hold, "natural numbers is: ", sum)
