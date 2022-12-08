def solution():
    output = 0
    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')

            elf1, elf2 = line.split(',')
            elf1_start, elf1_end = int(elf1.split('-')[0]), int(elf1.split('-')[1])
            elf2_start, elf2_end = int(elf2.split('-')[0]), int(elf2.split('-')[1])

            # elf1 and elf2 overlap
            if elf1_start <= elf2_start:
                if elf1_end >= elf2_start:
                    output += 1
                    print(f'elf 1 {elf1} overlaps elf2 {elf2}')

            elif elf2_start <= elf1_start:
                if elf2_end >= elf1_start:
                    output += 1
                    print(f'elf2 {elf2} overlaps elf1 {elf1}')

        f.close()

    return output

print(solution())