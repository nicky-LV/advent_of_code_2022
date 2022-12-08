import re


def solution():
    letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
    stacks = {
        1: ['R', 'Q', 'G', 'P', 'C', 'F'],
        2: ['P', 'C', 'T', 'W'],
        3: ['C', 'M', 'P', 'H', 'B'],
        4: ['R', 'P', 'M', 'S', 'Q', 'T', 'L'],
        5: ['N', 'G', 'V', 'Z', 'J', 'H', 'P'],
        6: ['J', 'P', 'D'],
        7: ['R', 'T', 'J', 'F', 'Z', 'P', 'G', 'L'],
        8: ['J', 'T', 'P', 'F', 'C', 'H', 'L', 'N'],
        9: ['W', 'C', 'T', 'H', 'Q', 'Z', 'V', 'G']
    }

    with open('./input.txt') as f:
        exp = r'move ([0-9]+) from ([0-9]+) to ([0-9]+)'
        for line in f.readlines():
            line = line.strip('\n')

            matches = re.findall(exp, line)
            print(matches)
            if matches:
                num_crates, from_stack, to_stack = int(matches[0][0]), int(matches[0][1]), int(matches[0][2])

                # crates to move
                crates = stacks[from_stack][0:num_crates]
                # remove crates from from_stack
                stacks[from_stack] = stacks[from_stack][num_crates::]

                # add crates to to_stack
                stacks[to_stack] = crates + stacks[to_stack]

        f.close()

    output = ''
    for stack in stacks.values():
        if stack:
            output += stack[0]

    return output



print(solution())
