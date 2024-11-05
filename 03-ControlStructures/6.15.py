kod = input("Wprowadź kod EAN-13: ")

# Sprawdzamy, czy wprowadzony kod ma długość 13 i czy składa się tylko z cyfr
if len(kod) == 13 and kod.isdigit():
    print("Kod jest poprawny")
    
    # Sprawdzamy, czy kod zaczyna się od "590"
    if kod.startswith("590"):
        print("Produkt jest z Polski")
else:
    print("Kod jest niepoprawny")
