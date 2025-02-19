import re
txt = 'The rain in Spain'
x = re.search('\s', txt)
print(x.start())