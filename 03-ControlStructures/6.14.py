#An influencer is a person who can influence other people's behaviour.
#An influencer communicates with other people using social networking sites. 
#Write a program that checks whether a given person is a good influencer, that is,
#whether the person has at least two of the following accounts: Facebook, Twitter or Instagram. Use logical type variables:
#facebook, twitter, instagram, the value of which indicates whether the person has an account on the social networking site. Sample result:
#If the person has at least two of the accounts, the program prints "Good influencer",
#otherwise it prints "Not a good influencer".

print("na wszystkie pytania odpowiadaj tak bądź nie")
f = input("czy masz konto FaceBook? ").lower
t = input("czy masz konto Twitter? ").lower
i = input("czy masz konto Instagram? ").lower
chuj1 = False
chuj2 = False
chuj3 = False
if f == "tak":
    chuj1 = True
else:
    chuj1 = False
if t == "tak":
    chuj2 = True
else:
    chuj2 = False
if i == "tak":
    chuj3 = True
else:
    chuj3 = False
    if chuj1 == True and chuj2 == True:
        print("Good influencer")
    elif chuj1 == True and chuj3 == True:
        print("Good influencer")
    elif chuj2 == True and chuj3 == True:
        print("Good influencer")
    elif chuj1 == True and chuj2 == True and chuj3 == True:
        print("good influencer")
    else:
        print("Not a good influencer")

