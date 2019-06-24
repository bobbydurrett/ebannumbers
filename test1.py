# Use inflect

"""

  show all eban numbers <= 1,000 (in a horizontal format), and a count
  show all eban numbers between 1,000 and 4,000 (inclusive), and a count
  show a count of all eban numbers up and including 10,000
  show a count of all eban numbers up and including 100,000
  show a count of all eban numbers up and including 1,000,000
  show a count of all eban numbers up and including 10,000,000
  
"""

import inflect
p = inflect.engine()

print(' ')
print('eban numbers up to and including 1000:')
print(' ')

count = 0

for i in range(1,1001):
    if not 'e' in p.number_to_words(i):
        print(str(i)+' ',end='')
        count += 1
        
print(' ')
print(' ')
print('count = '+str(count))
print(' ')






