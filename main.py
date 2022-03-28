
main_file = open("./Input/Letters/starting_letter.txt", "r+")
lines = main_file.read()
print(lines)
name_file = open("./Input/Names/invited_names.txt", "r+")
names = name_file.readlines()

print(names)
new_names = []
for name in names:
    new_names.append(name.replace("\n", ""))

for name in new_names:
    new_letter = open(f".\Output\ReadyToSend\letter_for_{name}", "w")
    new_lines=lines.replace("[name]", name)
    new_letter.write(new_lines)
    new_letter.close()

print(new_names)

main_file.close()
name_file.close()
