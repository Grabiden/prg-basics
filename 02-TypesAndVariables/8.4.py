###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = (input('wprowadź kod SWIFT '))

BC = swift[:4]
CC = swift[4:6]
LC = swift[6:8]
BRC = swift[8:11]

print(f'Bank Code: {BC}')
print(f'Country Code: {CC}')
print(f'Location Code: {LC}')
print(f'Branch Code: {BRC}')