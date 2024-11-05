#Write a program that prints the name of the day of the week for a given day number. 
# Then, using the defined function, 
# print the name of the day of the week for the following 
# day numbers: 1, 4, 7.
def weekday(n):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[(n - 1) % 7]
if __name__ == "__main__":
    print(weekday(1))
    print(weekday(4))
    print(weekday(7))