def get_all_substrings(s):
    substrings = []
    for start in range(len(s) + 1):
        for end in range(start+1, len(s) + 1):
            substrings.append(s[start:end])
    return substrings

print(get_all_substrings("abc"))

def sherlockAndAnagrams(s):
    substring_dict = {}
    for start in range(len(s) + 1):
        for end in range(start + 1, len(s) + 1):
            key = tuple(sorted(s[start:end]))
            substring_dict[key] = substring_dict.get(key, 0) + 1

    print(substring_dict)
    num_anagrams = 0
    for c in substring_dict.values():
        num_anagrams += (c * (c -1)) // 2
    return num_anagrams

print(sherlockAndAnagrams("abba"))


# (c * (c -1)) // 2