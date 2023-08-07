posl = "110101010"
a, b = 0, 1

for num in posl:
    med = (a + b) / 2
    if num == "1":
        a = med
    else:
        b = med
    print(f"[{a}; {b}]")
