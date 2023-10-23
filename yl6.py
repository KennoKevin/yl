a = input("sisesta a: ")
b = input("sisesta b: ")
c = input("sisesta c: ")

if int(a)> int(b) and int(a)> int(c):
    print("a: ", a)
elif int(b) > int(c):
    print("b: ", b)
else:
 print("c:", c)