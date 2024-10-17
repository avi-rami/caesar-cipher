# Caesar Cipher Program

# The alphabet list includes each letter twice to handle shifts that wrap around.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    """
    Function to encode or decode a message using the Caesar cipher.

    Parameters:
    - start_text (str): The input text to be encoded or decoded.
    - shift_amount (int): The number of positions to shift each letter.
    - cipher_direction (str): Either 'encode' to encrypt or 'decode' to decrypt the message.
    """
    end_text = ""

    # If the direction is 'decode', reverse the shift by multiplying by -1.
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        # TODO-3: Preserve numbers, symbols, and spaces in the final message.
        if char in alphabet:
            # Find the position of the character in the alphabet list.
            position = alphabet.index(char)

            # Calculate the new position by adding the shift amount.
            new_position = position + shift_amount

            # Add the character at the new position to the end_text.
            end_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet (e.g., a space, number, or symbol), keep it unchanged.
            end_text += char

    # Display the final encoded or decoded message.
    print(f"Here's the {cipher_direction}d result: {end_text}")


# Prompt the user to input the direction, message, and shift amount.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Ensure that the shift value is within the range of 0-25 by applying modulus operation.
shift = shift % 26

# Call the caesar function with the user's inputs.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# Use a while loop to keep the program running if the user chooses to continue.
