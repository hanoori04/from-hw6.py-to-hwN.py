def display_multiplication_table() :


    for i in range(1, 10):
        for j in range(2, 6):
            print(f"{j} x {i} = {j*i}".ljust(10), end="  ")
            if j == 5:
                print()
            

    print(" " )

    for i in range(1, 10):
        for j in range(6, 10):
            print(f"{j} x {i} = {j*i}".ljust(10), end="  ")
            if j == 9:
                print()


display_multiplication_table()