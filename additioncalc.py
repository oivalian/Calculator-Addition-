while True:
    try:
        count = []
        numbers = int(input("How many numbers do you wish to calculate? >>> "))
        [count.append(int(input("Enter number >>> "))) for _ in range(numbers)]
        print("Total:", sum(count), "\n")
        count = 0
    except ValueError:
        print('')
