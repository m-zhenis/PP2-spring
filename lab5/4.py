#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

text = "AhsjduhduiwhudhuwhdihwAidhiwhn"
x = re.findall('[A-Z][a-z]+', text)
print(x)