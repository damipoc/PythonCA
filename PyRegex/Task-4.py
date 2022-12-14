import re

pattern = r'(.*\d.*)'

text = '''
space
space1
apple
2apple
brush
brush3
'''

print(re.findall(pattern, text, re.MULTILINE))

# Example text to search:
'''
space
space1
apple
2apple
brush
brush3
'''

# Should match:
# ['space1', '2apple', 'brush3']

