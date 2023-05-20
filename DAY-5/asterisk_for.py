num_rows = int(input("Number of rows: "))

for i in range(num_rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()
