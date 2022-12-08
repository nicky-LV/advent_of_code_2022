def solution():
    output = 0
    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')

            elf1, elf2 = line.split(',')
            elf1_start, elf1_end = int(elf1.split('-')[0]), int(elf1.split('-')[1])
            elf2_start, elf2_end = int(elf2.split('-')[0]), int(elf2.split('-')[1])

            # elf1 contained in elf2
            if elf1_start >= elf2_start and elf1_end <= elf2_end:
                output += 1
                print(f'elf 1 {elf1} in elf2 {elf2}')

            # elf2 contained in elf1
            elif elf2_start >= elf1_start and elf2_end <= elf1_end:
                output += 1
                print(f'elf2 {elf2} in elf1 {elf1}')

        f.close()

    return output

print(solution())