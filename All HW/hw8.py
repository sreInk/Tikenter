def int_to_roman(number):
    if not (0 < number < 4000):
        return "Invalid Input! Enter a number between 1 and 3999."

    # Mapping of Roman numerals
    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""
    for value, numeral in roman_numerals:
        while number >= value:
            result += numeral
            number -= value

    return result


# Example usage
if __name__ == "__main__":
    try:
        num = int(input("Enter a number to convert to Roman numerals: "))
        print(f"The Roman numeral for {num} is: {int_to_roman(num)}")
    except ValueError:
        print("Please enter a valid integer.")
