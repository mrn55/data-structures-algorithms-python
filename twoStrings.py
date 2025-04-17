def twoStrings(s1, s2):
    set1 = set(s1)
    # print(set1)
    for ch in s2:
        if ch in set1:
            return "YES"
    return "NO"


print(twoStrings("hello", "world"))