print("Ivesime 10 skaitmenu ir stebesime magija!")
numbers = []
for i in range(10, 0, -1):
    numbers.append(int(input(f"Liko ivesti {i} skaitmenu: ")))
print(f"Visu skaiciu suma yra: {sum(numbers)}")
print(f"Visu skaiciu vidurkis yra: {sum(numbers) / len(numbers)}")
