def convert_to_base(number, base):
    """
    Convert a number to any base from 2 to 36

    Args:
        number (int): The number to convert
        base (int): The target base (2-36)

    Returns:
        str: The number representation in the target base
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")

    if number == 0:
        return "0"

    # Handle negative numbers
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number = number // base

    if is_negative:
        result = "-" + result

    return result


def convert_from_base(value_str, from_base):
    """
    Convert a string representation in any base to decimal (base 10)

    Args:
        value_str (str): The string to convert (e.g., "food", "1010", "1A3")
        from_base (int): The source base (2-36)

    Returns:
        int: The decimal value
    """
    if from_base < 2 or from_base > 36:
        raise ValueError("Base must be between 2 and 36")

    value_str = value_str.upper().strip()
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Handle negative numbers
    is_negative = False
    if value_str.startswith('-'):
        is_negative = True
        value_str = value_str[1:]

    result = 0
    power = 1

    # Process from right to left (least significant digit to most significant)
    for i in range(len(value_str) - 1, -1, -1):
        char = value_str[i]
        if char not in digits[:from_base]:
            raise ValueError(f"Invalid digit '{char}' for base {from_base}")

        digit_value = digits.index(char)
        result += digit_value * power
        power *= from_base

    if is_negative:
        result = -result

    return result


def convert_between_bases(value_str, from_base, to_base):
    """
    Convert directly from one base to another

    Args:
        value_str (str): The value to convert
        from_base (int): Source base
        to_base (int): Target base

    Returns:
        str: The converted value in target base
    """
    # First convert to decimal
    decimal_value = convert_from_base(value_str, from_base)
    # Then convert to target base
    return convert_to_base(decimal_value, to_base)


def main():
    print("Advanced Number Base Converter")
    print("=" * 40)
    print("Supports bases 2-36 with digits 0-9 and A-Z")
    print("Examples: '1010' (binary), 'FF' (hex), 'food' (hex)")
    print()

    try:
        # Get the value to convert (can be numbers or letters)
        value_input = input("Enter the value to convert: ").strip()

        # Get source and target bases
        from_base = int(input("Enter the source base (2-36): "))
        to_base = int(input("Enter the target base (2-36): "))

        # Validate bases
        if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
            print("Error: Both bases must be between 2 and 36")
            return

        # Convert between bases
        result = convert_between_bases(value_input, from_base, to_base)

        print(f"\nConversion Result:")
        print(f"{value_input} (base {from_base}) = {result} (base {to_base})")

        # Show intermediate decimal value for understanding
        if from_base != 10:
            decimal_val = convert_from_base(value_input, from_base)
            print(f"Intermediate decimal value: {decimal_val}")

    except ValueError as e:
        print(f"Error: {e}")
        print("Please check your inputs:")
        print("- Value should contain valid digits for the source base")
        print("- Bases should be integers between 2 and 36")


def show_examples():
    """Display some example conversions"""
    print("\n" + "=" * 40)
    print("Example Conversions:")
    print("=" * 40)

    examples = [
        ("1010", 2, 10, "Binary to Decimal"),
        ("255", 10, 16, "Decimal to Hexadecimal"),
        ("FF", 16, 10, "Hexadecimal to Decimal"),
        ("food", 16, 10, "Hex 'food' to Decimal"),
        ("food", 16, 2, "Hex 'food' to Binary"),
        ("1A3", 16, 8, "Hexadecimal to Octal"),
        ("100", 10, 5, "Decimal to Base 5"),
        ("ZZ", 36, 10, "Base 36 to Decimal"),
    ]

    for value, from_base, to_base, description in examples:
        try:
            result = convert_between_bases(value, from_base, to_base)
            print(f"{description:25} | {value} (base {from_base:2}) → {result:>10} (base {to_base})")
        except ValueError as e:
            print(f"{description:25} | Error: {e}")


def interactive_mode():
    """Interactive mode for multiple conversions"""
    print("\nInteractive Mode - Enter 'quit' to exit")
    print("-" * 40)

    while True:
        try:
            value_input = input("\nEnter value (or 'quit' to exit): ").strip()
            if value_input.lower() == 'quit':
                break

            from_base = int(input("Enter source base (2-36): "))
            to_base = int(input("Enter target base (2-36): "))

            if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
                print("Error: Bases must be between 2 and 36")
                continue

            result = convert_between_bases(value_input, from_base, to_base)
            print(f"Result: {value_input} (base {from_base}) = {result} (base {to_base})")

        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    # Run main conversion
    main()

    # Show examples
    show_examples()

    # Optional: Start interactive mode
    print("\n" + "=" * 40)
    start_interactive = input("Start interactive mode? (y/n): ").lower()
    if start_interactive == 'y':
        interactive_mode()