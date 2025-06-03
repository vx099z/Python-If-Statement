input_str = input()

son1_str, son2_str = input_str.split(" va ")
son1 = int(son1_str)
son2 = int(son2_str)

if son1 > son2:
    print(son1)
elif son2 > son1:
    print(son2)
else:
    print("Teng")