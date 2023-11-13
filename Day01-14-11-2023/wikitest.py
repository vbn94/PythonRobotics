import wikipedia    
import re

try:
 result = wikipedia.summary("Sofia", sentences = 2)
 result = re.sub(r'\([^)]*\)', '', result)
 print(result)
except wikipedia.exceptions.PageError:
 print('Not found')