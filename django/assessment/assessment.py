def decode(message_file):
    with open(message_file, "r") as file:
        lines = file.readlines()

    # Dictionary to store number-word pairs
    number_word_pairs = {}
    for line in lines:
        number, word = line.split()
        number_word_pairs[int(number)] = word

    # Function to calculate the last number of each row in the pyramid
    def last_number_of_row(row):
        return row * (row + 1) // 2

    # Identifying the key numbers
    key_numbers = []
    row = 1
    while last_number_of_row(row) <= max(number_word_pairs.keys()):
        key_numbers.append(last_number_of_row(row))
        row += 1

    # Constructing the decoded message
    decoded_message = " ".join(
        [
            number_word_pairs[number]
            for number in key_numbers
            if number in number_word_pairs
        ]
    )

    return decoded_message


# Example usage
decoded_message = decode("coding_qual_input.txt")
print(decoded_message)
