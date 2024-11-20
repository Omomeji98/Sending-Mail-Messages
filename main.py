PLACEHOLDER = "[name]"

with open("../../../Desktop/project24/Mail Merge Project Start/Input/Names/invited_names.txt") as invited_names:
    open_names = invited_names.readlines()
    print(open_names)


with open("../../../Desktop/project24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as starting_letter:
    open_letter = starting_letter.read()
    for name in open_names:
        stripped_name = name.strip()
        new_letter = open_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"../../../Desktop/letter/letter_for_{stripped_name}.txt", mode="w") as completed_form:
            completed_form.write(new_letter)

