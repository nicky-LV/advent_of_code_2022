def solution():
    # Opponent: A = rock, B = paper, C = scissors
    # You: X = rock, Y = paper, Z = scissors

    wins = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X',
    }
    
    draws = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    score = 0

    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')

            opponent, you = line.split(" ")

            # win
            if you == wins[opponent]:
                score += (6 + points[you])

            # draw
            elif you == draws[opponent]:

                score += (3 + points[you])

            # lose
            else:
                score += points[you]

        f.close()

    return score

print(solution())