#Write a program that calculates a dog's age in dog's years. For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years. Sample result:

#Enter the dog's age in human years: 15
#The dog's age in dog's years is 73 years.

A = int(input("wprowadź wiek swojego psa w ludzkich latach "))

if A <= 2:
    DA = A * 10.5
else:
    DA = 2 * 10.5 + (A - 2) * 4

