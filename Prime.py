N =11
  
if N <=1000: 
      
   for i in range(2, N//2): 
         
       if (N % i) == 0: 
           print(N, "no") 
           break
   else: 
       print(N, "yes") 
  
else: 
   print(N, "no") 
