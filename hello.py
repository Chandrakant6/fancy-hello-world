import time

def hello(s):
  s = s or 'hello world'
  for i in range(len(s)):
      l = 'abcdefghijklmnopqrstuvwxyz '
      for j in l:
          print(s[:i] + j)
          time.sleep(.1) # seconds
          if s[i] == j:
              time.sleep(.5)
              break