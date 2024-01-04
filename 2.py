# 102803008
from typing import List


def calculate_platforms(weights: List[int], limit: int) -> int:
    weights.sort()
    i = 0
    j = len(weights) - 1
    platforms = 0
    while i <= j:
        if weights[i] + weights[j] <= limit:
            i += 1
        j -= 1
        platforms += 1
    return platforms


if __name__ == '__main__':
    weights = [int(num) for num in input().split()]
    limit = int(input())
    result = calculate_platforms(weights, limit)
    print(result)
