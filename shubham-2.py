import random
print("choose your password complexity: \n1. SuperStrong \n2. Strong \n3. Medium \n4. Weak")
lower="qwertyuiopasdfghjklzxcvbnm"
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
num="1234567890"
spch="!@#$%^&*()~[]}{<>?/"
buc=lower+upper
total=lower + upper + spch + num
cum=lower+upper+num
type=input("Enter your password complexity: ")
m=type.lower()
length=int(input("Enter the length of your password: "))
if m=="weak":
    password="".join(random.sample(num,length))
    print(f"your {type} password is :{password}")
elif m=="medium":
    password = "".join(random.sample(buc, length))
    print(f"your {type} password is :{password}")
elif m=="strong":
    password = "".join(random.sample(cum, length))
    print(f"your {type} password is :{password}")
elif m=="superstrong" or m=="super strong":
    password="".join(random.sample(all,length))
    print(f"your {type} password is :{password}")
else:
    print("invalid option!")