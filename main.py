import secrets
import string
UC = string.ascii_uppercase
LC = string.ascii_lowercase
DIG = string.digits
SPE = string.punctuation
print ("\nChoose Passwrod complexity")
print ("1. Simple ")
print ("2. Complex")
choice = input("Enter your choice (1/2): ")
if choice == "1":
    l = 8
    u = UC + LC+ DIG
    p = secrets.choice(UC) + secrets.choice(LC) + secrets.choice(DIG)

elif choice == "2":
    l = 12
    u = UC + LC + DIG + SPE
    p = secrets.choice(UC) + secrets.choice(LC) + secrets.choice(DIG) + secrets.choice(SPE)
else:
    print("Invalid choice!")
    exit()

for i in range(l-len(p)):
    p +=  secrets.choice(u)

password_list = list(p)
secrets.SystemRandom().shuffle(password_list)
p = ''.join(password_list)

    
print ("generated password : ",p)
