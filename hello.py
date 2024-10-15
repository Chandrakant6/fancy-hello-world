import time
from string import ascii_letters , punctuation

def hello(s = 'hello world'):
for i in range(len(s)):
	l = ascii_letters + punctuation
    for j in l:
		print(s[:i] + j)
		time.sleep(.1) # seconds
		if s[i] == j:
			time.sleep(.5)
			break
