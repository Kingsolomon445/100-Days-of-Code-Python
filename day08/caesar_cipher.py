# A caesar cipher encryption

from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(text_given, shift_number, direction_given):
    new_text = ""
    if direction_given == "decode":
        shift_number *= -1
    for ch in text_given:
        if ch.isalpha():
            shift_number %= 26
            val = ord(ch) + shift_number
            if val > 122:
                val -= 26
            elif val < 97:
                val += 26
            new_text += chr(val)
        else:
            new_text += ch
    print(f"The {direction_given}d text is {new_text}")


restart = 1
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction != "decode":
        print("Invalid choice")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    if input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower() == "no":
        print("Goodbye!")
        restart = 0
