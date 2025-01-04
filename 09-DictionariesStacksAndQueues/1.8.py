price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
<<<<<<< HEAD

sum = 0 
for item in price_list:
    print(item, price_list[item])
    sum += price_list[item]

print(round(sum, 2))  
#dodajemy zniżke
discounted = 0.9
for item in price_list:
    price_list[item] *= discounted
    price_list[item] = round(price_list[item], 2)
for item in price_list:
    print(item, price_list[item])    

sum_after_discount = 0 
for item in price_list:
    sum_after_discount += price_list[item]
print(round(sum_after_discount, 2))    




=======
for ciuch,cena in price_list.items():
    price_list[ciuch] = cena*0.9

print(price_list)  
#sigmaaaaaa  
>>>>>>> 11cd2cebed6eda48bd3f9bc9be5b72ae7019f7cf
