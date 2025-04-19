def solve(s):
    return ''.join([c.capitalize() if i == 0 or s[i-1] == ' ' else c for i, c in enumerate(s)])

print(solve('   asdf Aas  df'))