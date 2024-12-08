def calculate_transmitted_data(original_data, polynomial):
    # Append zeros to the end of the original data
    extended_data = original_data + '0' * (len(polynomial) - 1)
    remainder = binary_division(extended_data, polynomial)
    transmitted_data = original_data + remainder
    return transmitted_data


def verify_transmitted_data(transmitted_data, polynomial):
    remainder = binary_division(transmitted_data, polynomial)
    return all(bit == '0' for bit in remainder)


def binary_division(dividend, divisor):
    # Convert strings to lists for easier manipulation
    dividend = list(dividend)
    divisor = list(divisor)
    # Perform binary division (XOR operation)
    for i in range(len(dividend) - len(divisor) + 1):
        if dividend[i] == '1':
            for j in range(len(divisor)):
                dividend[i + j] = str(int(dividend[i + j]) ^ int(divisor[j]))
    # Remove leading zeros from the remainder
    remainder = ''.join(dividend)[-len(divisor) + 1:]
    return remainder


# Test the functions
original_data = "110101"
polynomial = "110"

# Part 1: Calculate the Transmitted Data
transmitted_data = calculate_transmitted_data(original_data, polynomial)
print("Transmitted Data:", transmitted_data)

# Part 2: Verify the Transmitted Data
is_error_free = verify_transmitted_data(transmitted_data, polynomial)
print("Is error-free?", is_error_free)
