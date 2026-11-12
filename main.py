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
    u = UC + LC + DIG
elif choice == "2":
    l = 12
    u = UC + LC + DIG + SPE
else:
    print("Invalid choice!")
    exit()
p = ""
for i in range(l):
    c  =  secrets.choice(u)
    p += c
print ("generated password : ",p)
