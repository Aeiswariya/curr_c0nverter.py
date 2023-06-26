with open("currency.txt") as f:
    a = f.readlines()
    
dict = {}
for lines in a:
    data = lines.split("\t")

    dict[data[0]] = data[1]

amount = int(input("enter the amount to convert"))
currencies = input("enter currency to which we want to convert")
print(f"{amount} USD = {amount * float(dict[currencies])} {currencies}")


