def minion_game(s):
    subV = {}
    subC = {}
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i] in 'AEIOU':
                subV[s[i:j]] = subV.get(s[i:j], 0) + 1
            else:
                subC[s[i:j]] = subC.get(s[i:j], 0) + 1

    # print(subC)
    # print(subV)

    kevinScore = 0
    stuartScore = 0
    for n in subC.values():
        stuartScore += n

    for n in subV.values():
        kevinScore += n

    if kevinScore > stuartScore:
        print(f"Kevin {kevinScore}")
    elif kevinScore < stuartScore:
        print(f"Stuart {stuartScore}")
    else:
        print("Draw")

def minion_game2(s):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    n = len(s)

    for i in range(n):
        if s[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

minion_game('BANANA')