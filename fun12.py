def histogram(lst):
    for i in lst:
        for j in range(i):
            print("*", end="")
        print()