height = 0
while height <= 0 or height > 23:
    try:
        height = int(input("height: "))
    except ValueError:
        continue

hashInLine = 2
i = height
while i > 0:
    print(" " * (i-1), "#" * hashInLine)
    hashInLine += 1
    i -= 1
