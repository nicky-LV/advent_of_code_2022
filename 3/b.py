def solution():
    elf_count = 0
    groups = []

    letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = letters.upper()
    output = 0

    # extract groups
    with open('./input.txt', 'r') as f:
        group = []

        for line in f.readlines():
            group.append(line.strip('\n'))

            if len(group) == 3:
                groups.append(group)
                group = []

    for group in groups:
        # find the character that is common between all three elves
        for char in group[0]:
            if char in group[1] and char in group[2]:
                if char in letters:
                    output += letters.index(char) + 1

                elif char in upper_letters:
                    output += upper_letters.index(char) + 27
                break

    return output

print(solution())