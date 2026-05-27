#sera realizo a tabuada do 1 ao 10 usando a estrutura for

numero = 1 

for i in range (1,11):
    print(f"tabuada do {i}: ")
    for j in (range(1,11)):
        total = i*j
        print(f"{i} x {j} = {total}")
        print("-" * 40)
