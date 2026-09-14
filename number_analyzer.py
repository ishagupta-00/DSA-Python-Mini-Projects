# NUMBER ANALYZER 

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def calculate_subtraction(numbers):
    result = numbers[0]

    for number in numbers[1:]:
        result -= number

    return result


def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def find_smallest(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


def main():

    print("========== NUMBER ANALYZER ==========")

    try:
        count = int(input("How many numbers do you want to enter? "))

        if count <= 0:
            print("Enter at least one number.")
            return

        numbers = []

        for i in range(count):
            number = float(input("Enter number " + str(i + 1) + ": "))
            numbers.append(number)

        total = calculate_sum(numbers)
        subtraction = calculate_subtraction(numbers)
        average = total / len(numbers)
        largest = find_largest(numbers)
        smallest = find_smallest(numbers)

        even_count = 0
        odd_count = 0

        for number in numbers:
            if number.is_integer() and int(number) % 2 == 0:
                even_count += 1
            elif number.is_integer():
                odd_count += 1

        print("\n========== RESULT ==========")
        print("Numbers:", numbers)
        print("Sum:", total)
        print("Subtraction:", subtraction)
        print("Average:", round(average, 2))
        print("Largest Number:", largest)
        print("Smallest Number:", smallest)
        print("Even Numbers:", even_count)
        print("Odd Numbers:", odd_count)

    except ValueError:
        print("Please enter valid numbers.")


main()