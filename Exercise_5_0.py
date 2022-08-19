# while loops


n = 100

while n > 0:
    print(n)
    n -= 2

print("Blastoff!")
print(n)

# deliberately indefinite loop using break and continue statements to control the loop!
m = 0
while n == 0:
    print("idling!")
    print(m)
    m += 1

    if m == 10:
        print("Almost there!")
        continue

    if m == 20:
        break

print("We did it!")
