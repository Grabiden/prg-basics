arr = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
#Create a program that replaces the values of the main diagonal with 1.
#Use a loop statement. 
#Print the modified array. Sample result:
n = 0
while n < 3:
    arr[n][n] = 1
    n += 1
#0 1 0
#0 0 1


print(arr)
