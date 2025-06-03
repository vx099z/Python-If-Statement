raqam = input()

kod = raqam[:2]

if kod in ["90", "91"]:
    print("Ucell")
elif kod in ["93", "94"]:
    print("Beeline")
elif kod in ["95", "97"]:
    print("Uzmobile")
elif kod in ["88", "99"]:
    print("Mobiuz")
else:
    print("Noma'lum operator")