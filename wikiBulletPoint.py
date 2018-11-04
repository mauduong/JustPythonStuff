# Adds bullet points using wiki markup
#! python3
# wikiBulletPoint.py

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # WIKI MARK UP [* text_here] 

text = '\n'.join(lines)
pyperclip.copy(text)