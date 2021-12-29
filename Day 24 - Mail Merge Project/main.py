with open("./Input/Letters/starting_letter.txt") as file1:
    content = file1.read()

with open("./Input/Names/invited_names.txt") as file2:
    name_list = file2.readlines()
    for name in name_list:
        new_name = name.strip('\n')
        with open(f"./Output/{new_name}.txt", 'w') as file3:
            new_content = content.replace("[name]", new_name)
            file3.write(new_content)