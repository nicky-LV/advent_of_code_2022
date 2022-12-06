def solution():
    # Opponent: A = rock, B = paper, C = scissors
    # You: X = rock, Y = paper, Z = scissors

    mapping = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    wins, lose, points = {
        'A': mapping['B'],
        'B': mapping['C'],
        'C': mapping['A'],
    }, {
        'A': mapping['C'],
        'B': mapping['A'],
        'C': mapping['B'],
    }, {
        'X': 1,
        'A': 1,
        'Y': 2,
        'B': 2,
        'Z': 3,
        'C': 3
    }

    score = 0

    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')

            opponent, you = line.split(" ")

            # have to draw
            if you == 'Y':
                score += (3 + points[opponent])

            # win
            elif you == 'Z':
                you = wins[opponent]
                score += (6 + points[you])

            # lose
            else:
                you = lose[opponent]
                score += points[you]

        f.close()

    return score


print(solution())