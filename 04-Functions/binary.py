def binary_number(a):
   dick = str(a)
   nig = ["0","1"]
   for char in dick:
      if char in nig:
         return True
      else:
         return False
      
result = binary_number(56876)
print(result)      

   