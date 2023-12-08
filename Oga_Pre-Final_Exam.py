def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes_in_range(start, end):
    if start < 0:
        print("Enter a non-negative number.")
        return

    if end <= start:
        print(f"Enter a number greater than {start}.")
        return

    primes = [num for num in range(start, end + 1) if is_prime(num)]

    print(f"Prime numbers between {start} and {end} are: {', '.join(map(str, primes))}")


if __name__ == "__main__":
    while True:
        start_input = input("Enter a number [start]:")

        if start_input == "0":
            print("Program terminated.")
            break

        try:
            start = int(start_input)

            if start < 0:
                print("Enter a non-negative number.")
            else:
                end = int(input("Enter a number [end]: "))
                display_primes_in_range(start, end)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
