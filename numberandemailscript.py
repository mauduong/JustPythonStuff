# Extract phone numbers and email addresses from clipboard
# numberandemailscript.py

import pyperclip, re

# Example number 021 1234 5678
phoneNo = re.compile(r'''(
    (\d{,3}|\(\d{,3}\))      # Dialing code
    (\s|-|\.)?               # Separator
    \d{4}                    
    (\s|-|\.)?               # Second separator
    (\d{,4})
    (\s*(ext|x|ext.)\s*\d{,4})?
    )''', re.VERBOSE)

# Example email aliceb@email.com
email = re.compile(r'''(
    [a-zA-Z0-9._-]+                     # Local-part user name
    @                                   # @ symbol
    [a-zA-Z0-9.-]+                      # Domain name
    (\.[a-zA-Z]{2,4}(\.)?([a-zA-Z]{2,3})?)   # e.g .com, .net, .co.hk
    )''', re.VERBOSE)

# Matching
text = str(pyperclip.paste())
matched = []
for i in phoneNo.findall(text):
    number = '-'.join([i[1], i[3], i[6]])
    if i[9] != '':
        number += ' ext' + i[9]
    matched.append(number)
for i in email.findall(text):
    matched.append(i[0])

# Copy to clipboard
if len(matched) > 0:
    pyperclip.copy('\n'.join(matched))
    print('Copied to clipboard')
    print('\n'.join(matched))
else:
    print('It\'s empty man')
