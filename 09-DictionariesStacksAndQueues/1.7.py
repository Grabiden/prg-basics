def fun(dict):
    sum = 0
    for name in dict:
        
        print(name, dict[name])
        sum += dict[name]
    print(sum)    
       
fun({
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
})
