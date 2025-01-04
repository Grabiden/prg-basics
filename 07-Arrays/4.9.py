#["water","book","sky"]   ["water","book","sky"]
#[True,False]   [True,False,True]
#[5,3,1]   [5,3,1]
#[3,2,1]   [3,2]
def compare(array1, array2):
    n = 0
    if len(array1) == len(array2):
       while n < len(array1):
           if array1[n] == array2[n]:
               n += 1
               return True
               
           else:
               return False
    else:
        return False
print(compare([5,3,1], [5,3,1]))
           