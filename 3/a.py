def solution():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    upper_chars = chars.upper()
    output = 0

    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')

            m = len(line) // 2

            comp1, comp2 = line[0:m], line[m::]

            assert len(comp1) == len(comp2)

            print(comp1)
            for char in comp1:
                if char in comp2:
                    if char in chars:
                        output += chars.index(char) + 1
                        break

                    elif char in upper_chars:
                        output += upper_chars.index(char) + 27
                        break

        f.close()

    return output

print(solution())