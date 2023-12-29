count = []

while True:
    try:
        numbers = int(input("How many numbers do you wish to calculate? >>> "))
        for _ in range(numbers):
            count.append(int(input("Enter number >>> ")))
        print("Total:", sum(count), "\n")
    except ValueError:
        print('')
