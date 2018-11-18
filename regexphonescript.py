# regexphonescript.py
import re

# Grouped Regex
phoneNo = re.compile(r'(\d{3}) (\d{7})')
match = phoneNo.search("Article name here, please contact 021 0118291 for more details.")
print(match.group(1))
print(match.group(2))
print(match.group(0))
print(match.group())

print(match.groups())
prefix, remainder = match.groups()
print(prefix + " " + remainder)

# Pipe matching, or
orRegex = re.compile(r'are|you|sure|this|is|programming')
match = orRegex.search("Haha this isn't programming..")
print(match.group())

# Question mark matching, optional
optionalRegex = re.compile(r'Grape(fruit)?juice')
match = optionalRegex.search('That is some nice Grapefruitjuice')
match2 = optionalRegex.search('I\'ll just have Grapejuice thanks.')
print(match.group())
print(match2.group())

# Asterisk matching, zero or more
repeatedRegex = re.compile(r'cheese(cake)*')
match = repeatedRegex.search('Now that\'s a nice cheesecake.')
match2 = repeatedRegex.search('Now that\'s a nice cheesecakecakecakecakecakecakecake.')
match3 = repeatedRegex.search('This ain\'t cheese')
print(match.group())
print(match2.group())
print(match3.group())

# Plus matching, one or more
additionRegex = re.compile(r'protect(ion)+')
match = additionRegex.search('I don\'t need protection..')
match2 = additionRegex.search('I may or may not need protectionionionionion')
match3 = additionRegex.search('This should throw an error')
print(match.group())
print(match2.group())
if (match3 == None):
    print('AttributeError exception due to None')

# Curley braces matching, specific repetition - matches longest string (greedy)
rangeRegex = re.compile(r'(ha){3}')
match = rangeRegex.search('hahaha')
rangeRegex = re.compile(r'(ha){,5}')
match2 = rangeRegex.search('hahahahahahahahahahahahahahahhahahahaha')
match3 = rangeRegex.search('hahaha')
rangeRegex = re.compile(r'(ha){3,}')
match4 = rangeRegex.search('haha')
match5 = rangeRegex.search('hahahahahahahahahaha')
print(match.group())
print(match2.group()) # Only goes up to (five)
print(match3.group())
if (match4 == None):
    print('match4 exception, under 3 repeitions')
print(match5.group())

# Greedy and Nongreedy matching, specific repetition - matches shortest string (nongreedy)
# Combine curley braces matching with optional matching
nongreedyRegex = re.compile(r'(ha){3,5}?')
match = nongreedyRegex.search('hahahahaha')
print(match.group())

# Regex Findall
phoneNo = re.compile(r'(\d{3}) (\d{7})')
match = phoneNo.search("Home: 021 0118291 Work: 091 1235439 Fax: 123 1234567")
match2 = phoneNo.findall("Home: 021 0118291 Work: 091 1235439 Fax: 123 1234567")
print(match.group())
print(match2)

# Use caret like ^[test] to exclude 'test' or ^Hello to ensure the first string always starts with Hello
# Dollar sign \d+$ ensures the end will always be a numeric
# ^\d+$ starts and ends with a numeric number
# Wildcard . match any character except new line, .* to match all
# re.compile('.*', re.DOTALL) - gets new lines