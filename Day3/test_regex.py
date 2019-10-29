import re

string = 'Jan 1987'

pattern = r"(\w+ (\d+))"

res = re.search(pattern, string)

print(res.group())
