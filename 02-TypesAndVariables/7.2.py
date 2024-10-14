password = input('Enter password: ')
password_ok = len(password) >= 8
if password_ok: 
   print(f'Password length is valid: {password_ok}')
else:
   print(f"Password length is not valid: {password_ok}")
