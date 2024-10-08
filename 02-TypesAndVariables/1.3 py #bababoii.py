 = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')
height = int(height)
weight = int(weight)
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Your BMI is', bmi)
if bmi > 25:
    print('you are obese'height)
if bmi < 19:
    print(too skinny)    
