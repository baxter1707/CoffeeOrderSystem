
entries = int(raw_input("How many entries would you like to make?"))

mathApp = {}


for i in range(1, entries + 1):
    mathApp.update({i:i*i})


print(mathApp)
