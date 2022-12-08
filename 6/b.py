def solution():
    """
    Naive solution, O(4n) checks all 4 length long substrings
    """

    with open('./input.txt') as f:
        data = f.read()

        for i in range(len(data)):
            # 4 different characters
            if len(set(data[i:i+14])) == 14:
                return i + 14

print(solution())