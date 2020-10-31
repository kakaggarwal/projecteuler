import sys

facts = [1, 1]
factCounts = [1]


def getFacts(n):
    while True:
        facts.append(facts[-1] + facts[-2])

        if len(str(facts[-1])) == n:
            factCounts.append(len(facts))
            return factCounts[-1]


def euler(n):
    if len(factCounts) >= n:
        return factCounts[n - 1]

    return getFacts(n)


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(euler(n))
