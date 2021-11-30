def main():
    with open("./Input/Letters/starting_letter.txt", mode="r") as file:
        template = file.read()
    with open("./Input/Names/invited_names.txt", mode="r") as file:
        lst = file.readlines()
        lst_person = [x.strip("\n ") for x in lst]
    for person in lst_person:
        letter = template.replace("[name]", person)
        with open(f"./Output/ReadyToSend/{person}.txt", mode="w") as file:
            file.write(letter)


if __name__ == '__main__':
    main()
