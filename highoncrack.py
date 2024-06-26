rows = int(input("how many rows do you want?"))
columns = int(input("how many columns do you want?"))
symbol = input("what symbol do you want?")

for i in range(rows):
    for n in range(columns):
        print(symbol, end=" ")
    print()