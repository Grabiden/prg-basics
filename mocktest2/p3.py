#[3,7,2]
#[4,2,5]
#[5,2,1]
def f(array2D):
    n = len(array2D)

    for i in range(n):
        row_sum = sum(array2D[i])
        col_sum = sum(array2D[j][i] for j in range(n))
        if row_sum != col_sum:
            return False
        else:
            return True
array2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]       
print(f(array2D))
        

        
