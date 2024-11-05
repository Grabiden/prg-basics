test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]
pytania = len(test_results)
dobre = sum(test_results)
złe = pytania = dobre
print(f"number of questions is {len(test_results)}")
print(f"number of corresct answears is {sum(test_results)}")
print(f"number of incorrect answears is {złe}")
print(f"percent of correct answears is {sum(test_results)/len(test_results)*100}%")