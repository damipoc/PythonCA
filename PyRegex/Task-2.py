import re

pattern = r'ho{1,2}p'
text = 'hop hoop hooop hoooop hooooop'
print(re.findall(pattern,text))

# Example text to search:
# 'hop hoop hooop hoooop hooooop'

# Should match:
# ['hop', 'hoop']

