b = int(input())
sum = 0
temp = b
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if b== sum:
   print("yes")
else:
   print("no")
