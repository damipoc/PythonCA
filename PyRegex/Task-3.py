import re

pattern = r'https://(.*)'
text = "https://cloudacademy.com"
print(re.findall(pattern, text))

# Example text to search:
# 'https://cloudacademy.com'

# Should match:
# ['cloudacademy.com']

