num_rows = int(input("Enter no. of rows: "))
row = 0
col = 0
while row < num_rows:
    col = 0
    while col <= row:
        print("*", end=" ")
        col += 1
    print()
    row += 1
