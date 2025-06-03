number = input("Sonlarni kiriting: ").split()

for son in number:
    son = int(son)
    if son % 2 == 0:
        print(f"{son} - Juft son")
    else:
        print(f"{son} - Toq son")