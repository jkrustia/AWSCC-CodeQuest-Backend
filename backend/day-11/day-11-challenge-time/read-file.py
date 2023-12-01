fileName = "List of Names.txt"

with open(fileName, 'r') as file:
    lines = file.readlines()

    print(f"This is the content of \"{fileName}\":")
    for line in lines:
        print("\t" + line.strip())

sortedLines = sorted(lines)

with open(fileName, 'w') as file:
    file.writelines(sortedLines)

print(f"\nThe content of \"{fileName}\" has been updated with names in alphabetical order.")
