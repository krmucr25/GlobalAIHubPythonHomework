first = input("first name ")
last = input("last name ")
age = int(input("Age"))
data = int(input("Data of birtday "))

userlist = [first, last, age, data]

for i in (userlist):
    print(i)

if age < 18:
    print("You can't go out because it's too dangerous")
else:
    print("you can go out to the street")
