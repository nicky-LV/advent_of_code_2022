elf_sums = []

with open('./input.txt') as f:
    elf_sum = 0
    for line in f.readlines():
        if line == "\n":
            elf_sums.append(elf_sum)
            elf_sum = 0

        else:
            cal = line.strip('\n')
            elf_sum += int(cal)


print(sum(list(reversed(sorted(elf_sums)))[0:3]))