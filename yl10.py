name = input("Sinu nimi: ")
print("tere", name)
home = input("Elukoht: ")
if "saaremaa" in home.lower():
    print("Suht lahe")
age = input("Vanus: ")
age = int(age)
if age < 18:
    print("oled liiga noor")
else:
    print("võid autot juhtida")