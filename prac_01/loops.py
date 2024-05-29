for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

star = int(input("Number of stars:"))
for rows in range(star+1):
    for columns in range(rows):
        print("*", end=' ')
    print()
