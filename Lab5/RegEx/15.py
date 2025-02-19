import re
txt = 'The rain in Spain'
x = re.search('a', txt)
print(x.start())