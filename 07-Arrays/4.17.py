#Tuple: 50,20,40,50,30,50
#Value: 50
#Number of occurrences: 3
def f(value, tuple):
    #Count the number of occurrences of the value in the tuple
    count = tuple.count(value)
    return count
if __name__ == "__main__":
    #Test the function
    print(f(50, (50,20,40,50,30,50)))
