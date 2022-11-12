# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as file_name:
    names = file_name.readlines()
for name in names:
    name = name.rstrip()
    with open("input/Letters/starting_letter.txt") as letter:
        new_letter = letter.read()
    new_letter = new_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(new_letter)
