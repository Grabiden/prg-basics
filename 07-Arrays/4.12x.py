def unique(arr):
    count = {}
    for item in arr:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1

    result = [item for item in arr if count[item] == 1]
    
    return result

print(unique([7, 3, 8, 3, 1, 5]))        
          

               