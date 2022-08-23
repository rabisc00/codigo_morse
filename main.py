import json

MORSE_CODE_DICT = {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.", 'H': "....", 'I': "..",
    'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.",
    'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--..", '1': ".----",
    '2': "..---", '3': "...--", '4': "....-", '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----.",
    '0': "-----", '.': ".-.-.-", ',': "--..--", '?': "..--..", "'": ".----.", '/': "-..-.", ':': "---...",
    ';': "-.-.-.", '+': ".-.-.", '-': "-....-", '=': "-...-"
}
valid_options = ['enc', 'dec', 'data', 'quit']


def encode(message: str) -> str:
    """
    Turn a string into morse code

    :param message: The message to be encoded
    :return: The encoded message
    """

    coded_message = ""
    for c in message:
        # Check for white spaces
        if c == " ":
            coded_message += " / "

        # Add encoded letters to final string
        else:
            try:
                coded_message += f"{MORSE_CODE_DICT[c]} "

            except KeyError:
                coded_message += f"{c} "

    return coded_message


def decode(message: str) -> str:
    """
    Turn a morse code input into a readable string

    :param message: The morse code
    :return: The decrypted message
    """

    # Separate the words from one another
    split_input = message.split("/")

    decoded_message = ""
    for c in split_input:
        # Split the words into letters
        split_word = c.strip().split(" ")

        for letter in split_word:
            # Add decrypted letter to final string
            try:
                decoded_message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(letter)]

            # Avoids the program from crashing if given an invalid morse code letter
            except ValueError:
                print(f"\nNão temos '{letter}' em nosso banco de dados. Reescreva sua mensagem e tente novamente.")
                break

        decoded_message += " "

    return decoded_message


def choose_option() -> str:
    """
    Validate the user option input

    :return: A valid option string
    """

    option = input("Digite [enc] para codificar uma mensagem ou [dec] para decodificar.\n> ")

    while option not in valid_options:
        option = input("Opção inválida. Digite [enc] para codificar uma mensagem ou [dec] para decodificar.\n> ")

    return option


def show_data() -> None:
    """
    Prints the available morse code signs

    :return: None
    """
    print(f"\n{json.dumps(MORSE_CODE_DICT, sort_keys=True, indent=4)}\n")


def run_program():
    """
    Makes the morse code program run properly
    :return:
    """

    chosen_option = choose_option()

    if chosen_option == "enc":
        user_input = input("Digite a mensagem a ser codificada:\n> ").upper()
        print(f"\n{encode(user_input)}\n")

    elif chosen_option == "dec":
        user_input = input("Digite a mensagem a ser decodificada:\n> ")
        print(f"\n{decode(user_input)}\n")

    elif chosen_option == "data":
        show_data()

    elif chosen_option == "quit":
        return

    run_program()


run_program()
