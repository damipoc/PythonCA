import re

pattern = r'[6-8]'
text = "0987654321234567890"

print(re.findall(pattern, text))
# Example text to search:
# 0987654321234567890

# Should match:
# ['8', '7', '6', '6', '7', '8'] 

